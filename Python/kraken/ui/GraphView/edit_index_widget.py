
#
# Copyright 2010-2015
#


import json
from kraken.ui.Qt import QtWidgets, QtGui, QtCore


class IndexSpinBox(QtWidgets.QSpinBox):
    def __init__(self, parent):
        super(IndexSpinBox, self).__init__(parent)
        self.setObjectName('editIndexSpinBox')

    def focusOutEvent(self, event):
        self.parent().close()


class EditIndexWidget(QtWidgets.QWidget):

    def __init__(self, componentInput, pos, parent):
        super(EditIndexWidget, self).__init__(parent)
        self.setObjectName('editIndexWidget')

        self.componentInput = componentInput
        self.setWindowTitle( "Edit " + self.componentInput.getName() + " Index" )
        self.setWindowFlags( QtCore.Qt.Window )
        self.setFixedSize(150, 60)

        self.editLabel = QtWidgets.QLabel('Array Index')

        self.spinBoxWidget = IndexSpinBox(self)
        self.spinBoxWidget.setMinimum(0)
        self.spinBoxWidget.setValue(self.componentInput.getIndex())
        self.spinBoxWidget.valueChanged.connect(self.__setIndex)

        grid = QtWidgets.QVBoxLayout(self)
        grid.addWidget(self.editLabel, 0)
        grid.addWidget(self.spinBoxWidget, 0)

        self.move(pos)
        self.show()
        self.spinBoxWidget.setFocus()

    def __setIndex(self, index):
        self.componentInput.setIndex(index)


    def focusOutEvent(self, event):
        self.close()

