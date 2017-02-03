from kraken.ui.Qt import QtWidgets, QtGui, QtCore

from ..fe import FE
from ..widget_factory import EditorFactory
from ..base_editor import BaseValueEditor

from ..core.undo_redo_manager import UndoRedoManager

class ColorEditor(BaseValueEditor):

    def __init__(self, valueController, parent=None):
        super(ColorEditor, self).__init__(valueController, parent=parent)

        hbox = QtWidgets.QHBoxLayout()
        self._editors = []

        self._qgraphcsScene = QtWidgets.QGraphicsScene(self)
        self._qgraphcsView = QtWidgets.QGraphicsView(self)
        self._qgraphcsView.setScene(self._qgraphcsScene)
        self._qgraphcsView.setFixedSize(100, 20)
        self._qgraphcsView.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        hbox.addWidget(self._qgraphcsView, 1)

        hbox.addStretch(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(hbox)
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.updateEditorValue()
        self.setEditable( valueController.isEditable() )


    def setEditable(self, editable):
        self.setEnabled(editable)


    def getEditorValue(self):
        scalarKLType = FE.getInstance().types().Scalar
        colorKLType = FE.getInstance().types().Color
        return colorKLType(
            scalarKLType(self.__color.redF()),
            scalarKLType(self.__color.greenF()),
            scalarKLType(self.__color.blueF())
            )


    def setEditorValue(self, value):
        self.__color = QtGui.QColor(value.r*255, value.g*255, value.b*255)
        self._qgraphcsView.setBackgroundBrush(self.__color)
        self._qgraphcsView.update()


    def mousePressEvent(self, event):
        if self._valueController.isEditable():
            self.__backupColor = self.__color
            self.beginInteraction()
            dialog = QtWidgets.QColorDialog(self.__color, self)
            dialog.currentColorChanged.connect(self.__onColorChanged)
            dialog.accepted.connect(self.__onAccepted)
            dialog.rejected.connect(self.__onCanceled)
            dialog.setModal(True)
            dialog.show()


    def __onColorChanged(self, qcolor):
        self.__color = QtGui.QColor(qcolor.redF()*255, qcolor.greenF()*255, qcolor.blueF()*255)
        self._qgraphcsView.setBackgroundBrush(self.__color)
        self._setValueToController()


    def __onAccepted(self):
        self.endInteraction()


    def __onCanceled(self):
        self.endInteraction()

        undoManager = UndoRedoManager.getInstance()
        if undoManager and undoManager.canUndo():
            undoManager.undo()
        else:
            self.__onColorChanged(self.__backupColor)


    @classmethod
    def canDisplay(cls, valueController):
        if valueController.getDataType() == 'Color':
            return True
        return False

EditorFactory.registerEditorClass(ColorEditor)
