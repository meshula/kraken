from kraken.ui.Qt import QtWidgets, QtGui, QtCore

from ..fe import FE
from ..widget_factory import EditorFactory
from ..base_editor import BaseValueEditor


class ScalarEditor(BaseValueEditor):

    def __init__(self, valueController, parent=None):
        super(ScalarEditor, self).__init__(valueController, parent=parent)

        hbox = QtWidgets.QHBoxLayout()

        self._editor = QtWidgets.QLineEdit(self)
        validator = QtGui.QDoubleValidator(self)
        validator.setDecimals(3)
        self._editor.setValidator(validator)
        hbox.addWidget(self._editor, 1)

        hbox.addStretch(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(hbox)
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)

        self.updateEditorValue()
        self._editor.editingFinished.connect(self._setValueToController)
        self.setEditable( valueController.isEditable() )


    def setEditable(self, editable):
        self._editor.setReadOnly( not editable )


    def getEditorValue(self):
        return float(self._editor.text())


    def setEditorValue(self, value):
        self._editor.setText(str(round(value, 4)))


    @classmethod
    def canDisplay(cls, valueController):
        return(
                valueController.getDataType() == 'Scalar' or
                valueController.getDataType() == 'Float32' or
                valueController.getDataType() == 'Float64'
            )


EditorFactory.registerEditorClass(ScalarEditor)