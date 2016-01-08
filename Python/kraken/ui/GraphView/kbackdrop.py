
#
# Copyright 2010-2015
#

import math

from PySide import QtGui, QtCore

from kraken.ui.backdrop_inspector import BackdropInspector


class KBackdropTitle(QtGui.QGraphicsWidget):

    __color = QtGui.QColor(255, 255, 255)
    __font = QtGui.QFont('Helvetica', 11)
    __font.setLetterSpacing(QtGui.QFont.PercentageSpacing, 120)
    __fontMetrics = QtGui.QFontMetrics(__font)
    __labelBottomSpacing = 4

    def __init__(self, text, parent=None):
        super(KBackdropTitle, self).__init__(parent)

        self.parentWidget = parent

        self.__textItem = QtGui.QGraphicsTextItem(text, self)
        self.__textItem.setDefaultTextColor(self.__color)
        self.__textItem.setFont(self.__font)
        self.__textItem.setPos(0, 1)
        option = self.__textItem.document().defaultTextOption()
        self.__textItem.document().setDefaultTextOption(option)
        self.__textItem.adjustSize()
        self.__textItem.setTextWidth(120)

        self.setPreferredSize(self.textSize())

    def setText(self, text):
        self.__textItem.setPlainText(text)
        # self.__textItem.adjustSize()
        self.nodeResized(self.parentWidget.parentWidget.size().width())

    def setTextColor(self, color):
        self.__color = color
        self.update()

    def textSize(self):
        return QtCore.QSizeF(self.__textItem.textWidth(), self.textHeight())

    def textHeight(self):
        return self.__textItem.document().documentLayout().documentSize().height() + self.__labelBottomSpacing

    def nodeResized(self, width=None):

        fmWidth = self.__fontMetrics.width(self.__textItem.toPlainText())
        newWidth = min(fmWidth, width)
        if width > fmWidth:
            newWidth = width

        self.__textItem.setTextWidth(newWidth)
        self.setPreferredSize(newWidth, self.textHeight())

    def getBackdropWidget(self):
        return self.parent().parent()


class KBackdropHeader(QtGui.QGraphicsWidget):

    def __init__(self, text, parent=None):
        super(KBackdropHeader, self).__init__(parent)

        self.parentWidget = parent

        layout = QtGui.QGraphicsLinearLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(3)
        layout.setOrientation(QtCore.Qt.Horizontal)
        self.setLayout(layout)

        self._titleWidget = KBackdropTitle(text, self)
        layout.addItem(self._titleWidget)
        layout.setAlignment(self._titleWidget, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)

    def getTitleWidget(self):
        return self._titleWidget

    def setText(self, text):
        self._titleWidget.setText(text)


class KBackdrop(QtGui.QGraphicsWidget):

    nameChanged = QtCore.Signal(str, str)
    sizeChanged = QtCore.Signal(float)

    __defaultColor = QtGui.QColor(65, 120, 122, 255)
    __unselectedPen = QtGui.QPen(__defaultColor.darker(125), 1.6)
    __selectedPen = QtGui.QPen(__defaultColor.lighter(175), 1.6)
    __hoveredPen = QtGui.QPen(__defaultColor.lighter(110), 1.6)
    __linePen = QtGui.QPen(QtGui.QColor(25, 25, 25, 255), 1.25)

    __resizeDistance = 16.0
    __setCustomCursor = False
    __hoveredOver = False

    def __init__(self, graph, name):
        super(KBackdrop, self).__init__()
        self.setAcceptHoverEvents(True)

        self.__name = name
        self.__comment = None

        self.__graph = graph
        self.__color = self.__defaultColor
        self.__color.setAlpha(25)
        self.__inspectorWidget = None

        self.setMinimumWidth(120)
        self.setMinimumHeight(80)
        self.setZValue(-100)

        # Set defaults for interactions
        self.__selected = False
        self.__dragging = False
        self.__resizing = False
        self.__resizeCorner = -1

        self.createLayout()
        self.createConnections()

        # Initialize the comment with the name
        self.setComment(name)


    def createLayout(self):

        layout = QtGui.QGraphicsLinearLayout()
        layout.setContentsMargins(5, 0, 5, 7)
        layout.setSpacing(7)
        layout.setOrientation(QtCore.Qt.Vertical)
        self.setLayout(layout)

        self.__headerItem = KBackdropHeader(self.__name, self)
        self.__titleWidget = self.__headerItem.getTitleWidget()
        layout.addItem(self.__headerItem)
        layout.setAlignment(self.__headerItem, QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        layout.addStretch(1)

    def createConnections(self):

        self.sizeChanged.connect(self.__titleWidget.nodeResized)


    def getName(self):
        return self.__name

    def setName(self, name):
        if name != self.__name:
            origName = self.__name
            self.__name = name
            # self.__headerItem.setText(self.__name)

            # Emit an event, so that the graph can update itsself.
            self.nameChanged.emit(origName, name)

            # Update the node so that the size is computed.
            self.adjustSize()


    def getComment(self):
        return self.__comment

    def setComment(self, comment):
        self.__comment = comment
        self.__headerItem.setText(comment)

        # Resize the width of the backdrop based on title width
        titleWidget = self.__headerItem.getTitleWidget()
        titleWidth = titleWidget.textSize().width()
        self.resize(titleWidth, self.size().height())

        # Update the node so that the size is computed.
        self.adjustSize()


    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color
        self.__color.setAlpha(25)
        self.update()


    def getGraph(self):
        return self.__graph

    def getHeader(self):
        return self.__headerItem


    # ==========
    # Selection
    # ==========
    def isSelected(self):
        return self.__selected

    def setSelected(self, selected=True):
        self.__selected = selected
        self.update()


    # ==========
    # Graph Pos
    # ==========
    def getGraphPos(self):
        transform = self.transform()
        size = self.size()
        return QtCore.QPointF(transform.dx()+(size.width()*0.5), transform.dy()+(size.height()*0.5))

    def setGraphPos(self, graphPos):
        self.prepareConnectionGeometryChange()
        size = self.size()
        self.setTransform(QtGui.QTransform.fromTranslate(graphPos.x()-(size.width()*0.5), graphPos.y()-(size.height()*0.5)), False)

    def translate(self, x, y):
        self.prepareConnectionGeometryChange()
        super(KBackdrop, self).translate(x, y)


    # Prior to moving the node, we need to tell the connections to prepare for a geometry change.
    # This method must be called preior to moving a node.
    def prepareConnectionGeometryChange(self):
        pass

    def paint(self, painter, option, widget):
        rect = self.windowFrameRect()
        painter.setBrush(self.__color)

        painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0, 0), 0))

        roundingY = 20.0 / (rect.height() / 80.0)
        roundingX = rect.height() / rect.width() * roundingY

        painter.drawRoundRect(rect, roundingX, roundingY, mode=QtCore.Qt.AbsoluteSize)

        # Title BG
        titleHeight = self.__headerItem.size().height() - 3

        darkerColor = self.__color.darker(125)
        darkerColor.setAlpha(255)
        painter.setBrush(darkerColor)
        roundingYHeader = rect.width() * roundingX / titleHeight
        painter.drawRoundRect(0, 0, rect.width(), titleHeight, roundingX, roundingYHeader)
        painter.drawRect(0, titleHeight * 0.5 + 2, rect.width(), titleHeight * 0.5)

        painter.setBrush(QtGui.QColor(0, 0, 0, 0))
        if self.__selected:
            painter.setPen(self.__selectedPen)
        elif self.__hoveredOver:
            painter.setPen(self.__hoveredPen)
        else:
            painter.setPen(self.__unselectedPen)

        painter.drawRoundRect(rect, roundingX, roundingY, mode=QtCore.Qt.AbsoluteSize)

        super(KBackdrop, self).paint(painter, option, widget)

    # =======
    # Events
    # =======
    def mousePressEvent(self, event):
        if event.button() is QtCore.Qt.MouseButton.LeftButton:

            resizeCorner = self.getCorner(event.pos())
            if resizeCorner != -1 and self.isSelected():
                self.__resizing = True
                self.__resizeCorner = resizeCorner
                self._resizedBackdrop = False
            else:
                modifiers = event.modifiers()
                if modifiers == QtCore.Qt.ControlModifier:
                    if not self.isSelected():
                        self.__graph.selectNode(self, clearSelection=False)
                    else:
                        self.__graph.deselectNode(self)

                elif modifiers == QtCore.Qt.ShiftModifier:
                    if not self.isSelected():
                        self.__graph.selectNode(self, clearSelection=False)
                else:
                    if not self.isSelected():
                        self.__graph.selectNode(self, clearSelection=True)

                    if self.__headerItem.contains(event.pos()):
                        self.setCursor(QtCore.Qt.ClosedHandCursor)
                        self.__dragging = True
                        self._nodesMoved = False

            self._mouseDownPoint = self.mapToScene(event.pos())
            self._mouseDelta = self._mouseDownPoint - self.getGraphPos()
            self._lastDragPoint = self._mouseDownPoint

            self._initPos = self.pos()
            self._initScenePos = self.mapToScene(self.pos())
            self._initBoundingRect = self.boundingRect()
            self._initSceneBoundingRect = self.sceneBoundingRect()

        else:
            super(KBackdrop, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.__dragging:
            newPos = self.mapToScene(event.pos())

            graph = self.getGraph()
            if graph.getSnapToGrid() is True:
                gridSize = graph.getGridSize()

                newNodePos = newPos - self._mouseDelta

                snapPosX = math.floor(newNodePos.x() / gridSize) * gridSize;
                snapPosY = math.floor(newNodePos.y() / gridSize) * gridSize;
                snapPos = QtCore.QPointF(snapPosX, snapPosY)

                newPosOffset = snapPos - newNodePos

                newPos = newPos + newPosOffset

            delta = newPos - self._lastDragPoint
            self.__graph.moveSelectedNodes(delta)
            self._lastDragPoint = newPos
            self._nodesMoved = True

        elif self.__resizing:

            newPos = self.mapToScene(event.pos())
            delta = newPos - self._mouseDownPoint
            self._resizedBackdrop = True

            newPosX = 0
            newPosY = 0
            newWidth = self._initBoundingRect.width()
            newHeight = self._initBoundingRect.height()

            if self.__resizeCorner == 0:

                newWidth = self._initBoundingRect.width() + (delta.x() * -1.0)
                newHeight = self._initBoundingRect.height() + (delta.y() * -1.0)

                if newWidth <= self.minimumWidth():
                    newWidth = self.minimumWidth()
                else:
                    newPosX = self._initPos.x() + delta.x()

                if newHeight <= self.minimumHeight():
                    newHeight = self.minimumHeight()
                else:
                    newPosY = self._initPos.y() + delta.y()

            elif self.__resizeCorner == 1:

                newWidth = self._initBoundingRect.width() + delta.x()
                newHeight = self._initBoundingRect.height() + (delta.y() * -1.0)

                if newWidth <= self.minimumWidth():
                    newWidth = self.minimumWidth()
                else:
                    newPosX = self._initPos.x()

                if newHeight <= self.minimumHeight():
                    newHeight = self.minimumHeight()
                else:
                    newPosY = self._initPos.y() + delta.y()

            elif self.__resizeCorner == 2:

                newWidth = self._initBoundingRect.width() + (delta.x() * -1.0)
                newHeight = self._initBoundingRect.height() + delta.y()

                if newWidth <= self.minimumWidth():
                    newWidth = self.minimumWidth()
                else:
                    newPosX = self._initPos.x() + delta.x()

                if newHeight <= self.minimumHeight():
                    newHeight = self.minimumHeight()
                else:
                    newPosY = self._initPos.y()

            elif self.__resizeCorner == 3:
                newPosX = self._initPos.x()
                newPosY = self._initPos.y()
                newWidth = self._initBoundingRect.width() + delta.x()
                newHeight = self._initBoundingRect.height() + delta.y()

                if newWidth <= self.minimumWidth():
                    newWidth = self.minimumWidth()

                if newHeight <= self.minimumHeight():
                    newHeight = self.minimumHeight()

            self.setPos(newPosX, newPosY)
            self.resize(newWidth, newHeight)

            self.sizeChanged.emit(newWidth)

            self.prepareGeometryChange()

        else:
            super(KBackdrop, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__dragging:
            if self._nodesMoved:

                newPos = self.mapToScene(event.pos())

                delta = newPos - self._mouseDownPoint
                self.__graph.endMoveSelectedNodes(delta)

            self.setCursor(QtCore.Qt.ArrowCursor)
            self.__dragging = False

        elif self.__resizing:

            self.setCursor(QtCore.Qt.ArrowCursor)
            self.__resizing = False
            self.__resizeCorner = -1

        else:
            super(KBackdrop, self).mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event):
        if self.__inspectorWidget is None:
            parentWidget = self.getGraph().getGraphViewWidget()
            self.__inspectorWidget = BackdropInspector(parent=parentWidget, nodeItem=self)
            result = self.__inspectorWidget.exec_()
        else:
            self.__inspectorWidget.setFocus()

        super(KBackdrop, self).mouseDoubleClickEvent(event)

    def hoverEnterEvent(self, event):
        self.__hoveredOver = True
        self.update()

    def hoverMoveEvent(self, event):

        resizeCorner = self.getCorner(event.pos())
        if resizeCorner == 0:
            self.__setCustomCursor = True
            self.setCursor(QtCore.Qt.SizeFDiagCursor)
        elif resizeCorner == 1:
            self.__setCustomCursor = True
            self.setCursor(QtCore.Qt.SizeBDiagCursor)
        elif resizeCorner == 2:
            self.__setCustomCursor = True
            self.setCursor(QtCore.Qt.SizeBDiagCursor)
        elif resizeCorner == 3:
            self.__setCustomCursor = True
            self.setCursor(QtCore.Qt.SizeFDiagCursor)
        elif self.__headerItem.contains(event.pos()) is True:
            self.__setCustomCursor = True
            self.setCursor(QtCore.Qt.OpenHandCursor)
        else:
            if self.__setCustomCursor is True:
                self.setCursor(QtCore.Qt.ArrowCursor)

    def hoverLeaveEvent(self, event):
        self.setCursor(QtCore.Qt.ArrowCursor)
        self.__hoveredOver = False
        self.update()

    # =============
    # Misc Methods
    # =============
    def getCorner(self, pos):
        topLeft = self.mapFromItem(self, self.boundingRect().topLeft())
        bottomRight = self.mapFromItem(self, self.boundingRect().bottomRight())
        rect = QtCore.QRectF(topLeft, bottomRight)

        if (rect.topLeft() - pos).manhattanLength() < self.__resizeDistance:
            return 0
        elif (rect.topRight() - pos).manhattanLength() < self.__resizeDistance:
            return 1
        elif (rect.bottomLeft() - pos).manhattanLength() < self.__resizeDistance:
            return 2
        elif (rect.bottomRight() - pos).manhattanLength() < self.__resizeDistance:
            return 3

        return -1

    def inspectorClosed(self):
        self.__inspectorWidget = None


    # ==========
    # Shut Down
    # ==========
    def disconnectAllPorts(self):
        pass
