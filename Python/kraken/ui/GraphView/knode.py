
#
# Copyright 2010-2015
#


import json
from kraken.ui.Qt import QtWidgets, QtGui, QtCore

from pyflowgraph.node import Node
from pyflowgraph.port import PortCircle, BasePort, InputPort, OutputPort, PortLabel

from kraken.core.maths import Vec2

from kraken.ui.component_inspector import ComponentInspector


def getPortColor(dataType):

    if dataType.startswith('Xfo'):
        return QtGui.QColor(128, 170, 170, 255)
    elif dataType.startswith('Float'):
        return QtGui.QColor(32, 255, 32, 255)
    elif dataType.startswith('Integer'):
        return QtGui.QColor(0, 128, 0, 255)
    elif dataType.startswith('Boolean'):
        return QtGui.QColor(255, 102, 0, 255)
    else:
        return QtGui.QColor(50, 205, 254, 255)


class KNodePortLabel(PortLabel):

    def __init__(self, port, text, hOffset, color, highlightColor):
        super(KNodePortLabel, self).__init__(port, text, hOffset, color, highlightColor)


class KNodePortCircle(PortCircle):

    def __init__(self, port, graph, hOffset, color, connectionPointType):
        super(KNodePortCircle, self).__init__(port, graph, hOffset, color, connectionPointType)

        if self.getPort().getDataType().endswith('[]'):
            self.setDefaultPen(QtGui.QPen(QtGui.QColor(204, 0, 0), 1.5))
            self.setHoverPen(QtGui.QPen(QtGui.QColor(255, 155, 100), 2.0))


    def canConnectTo(self, otherPortCircle):

        # Check if you're trying to connect to a port on the same node.
        # TODO: Do propper cycle checking..
        otherPort = otherPortCircle.getPort()
        port = self.getPort()
        if otherPort.getNode() == port.getNode():
            return False

        if self.isInConnectionPoint():
            return self.getPort().getComponentInput().canConnectTo(otherPortCircle.getPort().getComponentOutput())
        else:
            return self.getPort().getComponentOutput().canConnectTo(otherPortCircle.getPort().getComponentInput())


class KNodeInputPort(InputPort):

    def __init__(self, parent, graph, componentInput):

        name = componentInput.getName()
        dataType = componentInput.getDataType()
        color = getPortColor(dataType)

        super(KNodeInputPort, self).__init__(parent, graph, name, color, dataType)

        self.componentInput = componentInput

    def setCircle(self):
        self.setInCircle(KNodePortCircle(self, self.getGraph(), -2, self.getColor(), 'In'))

    def setLabel(self):
        self.setLabelItem(PortLabel(self, self.getName(), -10, self._labelColor, self._labelHighlightColor))

    def getComponentInput(self):
        return self.componentInput


class KNodeOutputPort(OutputPort):

    def __init__(self, parent, graph, componentOutput):

        name = componentOutput.getName()
        dataType = componentOutput.getDataType()
        color = getPortColor(dataType)

        super(KNodeOutputPort, self).__init__(parent, graph, name, color, dataType)

        self.componentOutput = componentOutput

    def setCircle(self):
        self.setOutCircle(KNodePortCircle(self, self.getGraph(), 2, self.getColor(), 'Out'))

    def setLabel(self):
        self.setLabelItem(PortLabel(self, self.getName(), 10, self._labelColor, self._labelHighlightColor))

    def getComponentOutput(self):
        return self.componentOutput

class KNode(Node):

    def __init__(self, graph, component):
        super(KNode, self).__init__(graph, component.getDecoratedName())

        self.__component = component
        self.__inspectorWidget = None

        for i in range(self.__component.getNumInputs()):
            componentInput = component.getInputByIndex(i)
            self.addPort(KNodeInputPort(self, graph, componentInput))

        for i in range(self.__component.getNumOutputs()):
            componentOutput = component.getOutputByIndex(i)
            self.addPort(KNodeOutputPort(self, graph, componentOutput))

        self.setGraphPos( QtCore.QPointF( self.__component.getGraphPos().x, self.__component.getGraphPos().y ) )

        nodeColor = component.getComponentColor()
        self.setColor(QtGui.QColor(nodeColor[0], nodeColor[1], nodeColor[2], nodeColor[3]))
        self.setUnselectedColor(self.getColor().darker(125))
        self.setSelectedColor(self.getColor().lighter(175))


    def getName(self):
        return self.__component.getDecoratedName()

    def getComponent(self):
        return self.__component

    #########################
    ## Graph Pos

    def translate(self, x, y):
        super(KNode, self).translate(x, y)
        self.__component.setGraphPos( Vec2(self.scenePos().x(), self.scenePos().y()) )


    #########################
    ## Events

    def mouseDoubleClickEvent(self, event):
        if self.__inspectorWidget is None:
            parentWidget = self.getGraph().getGraphViewWidget()
            self.__inspectorWidget = ComponentInspector(component=self.__component, parent=parentWidget, nodeItem=self)
            self.__inspectorWidget.show()
        else:
            self.__inspectorWidget.setFocus()

        super(KNode, self).mouseDoubleClickEvent(event)


    def inspectorClosed(self):
        self.__inspectorWidget = None


