
#
# Copyright 2010-2014 Fabric Technologies Inc. All rights reserved.
#

import os
import json

from kraken.ui.Qt import QtGui, QtWidgets, QtCore


class PreferenceEditor(QtWidgets.QDialog):
    """A widget providing the ability to nest """

    def __init__(self, parent=None):

        # constructors of base classes
        super(PreferenceEditor, self).__init__(parent)
        self.setObjectName('PreferenceEditor')

        self.setWindowTitle('Preference Editor')
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.resize(600, 300)

        self.prefValueWidgets = []

        self.createLayout()
        self.createConnections()

    def createLayout(self):

        # Parent Layout
        self._topLayout = QtWidgets.QVBoxLayout()
        self._topLayout.setContentsMargins(0, 0, 0, 0)
        self._topLayout.setSpacing(0)

        self._mainWidget = QtWidgets.QWidget()
        self._mainWidget.setObjectName('mainPrefWidget')

        # Main Layout
        self._mainLayout = QtWidgets.QVBoxLayout(self._mainWidget)
        self._mainLayout.setContentsMargins(0, 0, 0, 0)
        self._mainLayout.setSpacing(0)

        self._preferenceLayout = QtWidgets.QGridLayout()
        self._preferenceLayout.setContentsMargins(10, 10, 10, 10)
        self._preferenceLayout.setSpacing(3)
        self._preferenceLayout.setColumnMinimumWidth(0, 200)
        self._preferenceLayout.setColumnStretch(0, 1)
        self._preferenceLayout.setColumnStretch(1, 2)

        # Add widgets based on type here
        preferences = self.parentWidget().window().preferences.getPreferences()
        i = 0
        for k, v in preferences.iteritems():
            labelFrameWidget = QtWidgets.QFrame()
            labelFrameWidget.setObjectName('prefLabelWidgetFrame')
            labelFrameWidget.setFrameStyle(QtWidgets.QFrame.NoFrame | QtWidgets.QFrame.Plain)
            labelFrameWidget.setToolTip(v['description'])
            labelFrameLayout = QtWidgets.QHBoxLayout()

            prefLabel = QtWidgets.QLabel(v['nice_name'], self)
            prefLabel.setProperty('labelClass', 'preferenceLabel')
            prefLabel.setObjectName(k + "_label")
            prefLabel.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
            prefLabel.setMinimumWidth(200)

            labelFrameLayout.addWidget(prefLabel)
            labelFrameWidget.setLayout(labelFrameLayout)

            self._preferenceLayout.addWidget(labelFrameWidget, i, 0)

            if v['type'] == 'bool':
                valueFrameWidget = QtWidgets.QFrame()
                valueFrameWidget.setObjectName('prefValueWidgetFrame')
                valueFrameWidget.setFrameStyle(QtWidgets.QFrame.NoFrame | QtWidgets.QFrame.Plain)
                valueFrameLayout = QtWidgets.QHBoxLayout()

                valueWidget = QtWidgets.QCheckBox(self)
                valueWidget.setObjectName(k + "_valueWidget")
                valueWidget.setChecked(v['value'])

                valueFrameLayout.addWidget(valueWidget)
                valueFrameWidget.setLayout(valueFrameLayout)

            self._preferenceLayout.addWidget(valueFrameWidget, i, 1, 1, 1)
            self.prefValueWidgets.append(valueWidget)

            i += 1

        # OK and Cancel buttons
        buttonLayout = QtWidgets.QHBoxLayout()
        buttonLayout.setContentsMargins(10, 10, 10, 10)
        buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        buttonLayout.addWidget(buttons)

        # Menu Bar
        self.menu_bar = QtWidgets.QMenuBar()
        self.file_menu = self.menu_bar.addMenu('&File')
        self.importPrefAction = self.file_menu.addAction('&Import...')
        self.exportPrefAction = self.file_menu.addAction('&Export...')

        self._mainLayout.addWidget(self.menu_bar)
        self._mainLayout.addLayout(self._preferenceLayout)
        self._mainLayout.addStretch(1)
        self._mainLayout.addLayout(buttonLayout)

        self._topLayout.addWidget(self._mainWidget)
        self.setLayout(self._topLayout)

    def createConnections(self):
        self.importPrefAction.triggered.connect(self.importPrefs)
        self.exportPrefAction.triggered.connect(self.exportPrefs)


    def importPrefs(self):
        fileDialog = QtWidgets.QFileDialog(self)
        fileDialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, on=True)
        fileDialog.setWindowTitle('Import Preferences')
        fileDialog.setDirectory(os.path.expanduser('~'))
        fileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        fileDialog.setNameFilter('JSON files (*.json)')

        if fileDialog.exec_() == QtWidgets.QFileDialog.Accepted:
            filePath = fileDialog.selectedFiles()[0]

            with open(filePath, "r") as openPrefFile:
                loadedPrefs = json.load(openPrefFile)

                self.parentWidget().window().preferences.loadPreferences(loadedPrefs)
                self.updatePrefValues()

    def exportPrefs(self):

        fileDialog = QtWidgets.QFileDialog(self)
        fileDialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, on=True)
        fileDialog.setWindowTitle('Export Preferences')
        fileDialog.setDirectory(os.path.expanduser('~'))
        fileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        fileDialog.setNameFilter('JSON files (*.json)')
        fileDialog.setDefaultSuffix('json')

        if fileDialog.exec_() == QtWidgets.QFileDialog.Accepted:
            filePath = fileDialog.selectedFiles()[0]

            preferences = self.parentWidget().window().preferences.getPreferences()
            with open(filePath, "w+") as savePrefFile:
                json.dump(preferences, savePrefFile)


    def updatePrefValues(self):
        """Updates the preference widgets with the values from the preferences.

        This is used when loading preferences from a file so that the widgets in
        the UI match what was loaded.
        """

        preferences = self.parentWidget().window().preferences

        for widget in self.prefValueWidgets:
            prefName = widget.objectName().rsplit('_', 1)[0]
            pref = preferences.getPreference(prefName)
            if pref['type'] == 'bool':
                widget.setChecked(pref['value'])

    # =======
    # Events
    # =======
    def accept(self):

        preferences = self.parentWidget().window().preferences

        for widget in self.prefValueWidgets:
            if type(widget) == QtWidgets.QCheckBox:
                prefName = widget.objectName().rsplit('_', 1)[0]
                preferences.setPreference(prefName, widget.isChecked())

        super(PreferenceEditor, self).accept()

    def closeEvent(self, event):
        pass
