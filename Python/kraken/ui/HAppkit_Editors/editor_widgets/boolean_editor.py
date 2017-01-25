from kraken.ui.Qt import QtWidgets, QtGui, QtCore

from ..fe import FE
from ..widget_factory import EditorFactory
from ..base_editor import BaseValueEditor


class BooleanEditor(BaseValueEditor):

    def __init__(self, valueController, parent=None):
        super(BooleanEditor, self).__init__(valueController, parent=parent)

        hbox = QtWidgets.QHBoxLayout()

        self._editor = QtWidgets.QCheckBox(self)
        hbox.addWidget(self._editor, 1)

        hbox.addStretch(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(hbox)
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)

        self.updateEditorValue()

        def __stateChanged(value):
            self._setValueToController()
        self._editor.stateChanged.connect(__stateChanged)

        self.setEditable(self.isEditable())


    def setEditable(self, editable):
        self._editor.setEnabled(editable)


    def getEditorValue(self):
        return self._editor.checkState() == QtCore.Qt.Checked


    def setEditorValue(self, value):
        if value:
            self._editor.setCheckState(QtCore.Qt.Checked)
        else:
            self._editor.setCheckState(QtCore.Qt.Unchecked)


    @classmethod
    def canDisplay(cls, valueController):
        return valueController.getDataType() == 'Boolean'

EditorFactory.registerEditorClass(BooleanEditor)

