"""Kraken Main Window and Launcher."""

import argparse
import logging
import os
import sys
import json

from kraken.log import getLogger
from kraken.ui.Qt import QtGui, QtWidgets, QtCore
from kraken.ui import images_rc
from kraken.ui.kraken_menu import KrakenMenu
from kraken.ui.kraken_ui import KrakenUI
from kraken.ui.preferences import Preferences
from kraken.ui.kraken_output_log import OutputLogDialog
from kraken.ui.kraken_statusbar import KrakenStatusBar
from kraken.ui.kraken_splash import KrakenSplash

logger = getLogger('kraken')


class KrakenWindow(QtWidgets.QMainWindow):
    """Main Kraken Window that loads the UI."""

    def __init__(self, parent=None):
        super(KrakenWindow, self).__init__(parent)
        self.setObjectName('KrakenMainWindow')
        self.setWindowTitle('Kraken Editor')
        self.setWindowIcon(QtGui.QIcon(':/images/Kraken_Icon.png'))
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.installEventFilter(self)
        # self.setFocusPolicy(QtCore.Qt.StrongFocus)
        # self.setFocus()

        QtCore.QCoreApplication.setOrganizationName("Kraken")
        QtCore.QCoreApplication.setApplicationName("Kraken Editor")
        self.settings = QtCore.QSettings("Kraken", "Kraken Editor")
        self.preferences = Preferences()

        self._focusInCallbacks = []
        self._focusOutCallbacks = []

        fontPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               'Fonts')

        fontPathList = [
            'Roboto' + os.path.sep + 'Roboto-Bold.ttf',
            'Roboto' + os.path.sep + 'Roboto-BoldItalic.ttf',
            'Roboto' + os.path.sep + 'Roboto-Italic.ttf',
            'Roboto' + os.path.sep + 'Roboto-Regular.ttf',
            'Roboto' + os.path.sep + 'RobotoCondensed-Bold.ttf',
            'Roboto' + os.path.sep + 'RobotoCondensed-BoldItalic.ttf',
            'Roboto' + os.path.sep + 'RobotoCondensed-Italic.ttf',
            'Roboto' + os.path.sep + 'RobotoCondensed-Regular.ttf',
            'Roboto' + os.path.sep + 'RobotoMono-Bold.ttf',
            'Roboto' + os.path.sep + 'RobotoMono-BoldItalic.ttf',
            'Roboto' + os.path.sep + 'RobotoMono-Italic.ttf',
            'Roboto' + os.path.sep + 'RobotoMono-Regular.ttf',
        ]

        for fontFilePath in fontPathList:
            QtGui.QFontDatabase.addApplicationFont(os.path.join(fontPath, fontFilePath))

        cssPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               'kraken_ui.css')

        styleData = ''
        with open(cssPath) as cssFile:
            styleData = cssFile.read()

        self.setStyleSheet(styleData)

        self.createLayout()
        self.createConnections()


    def createLayout(self):

        self.outputDialog = OutputLogDialog(self)

        # Setup Status Bar
        self.statusBar = KrakenStatusBar(self)

        mainWidget = QtWidgets.QWidget()

        # Main Layout
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.krakenUI = KrakenUI(self)
        self.krakenMenu = KrakenMenu(self)
        self.krakenUI.graphViewWidget.setGuideRigName('MyRig')
        self.krakenMenu.updateRigNameLabel()

        self.mainLayout.addWidget(self.krakenMenu)
        self.mainLayout.addWidget(self.krakenUI, 1)
        self.mainLayout.addWidget(self.statusBar)

        mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(mainWidget)

        self.statusBar.showMessage('Ready', 2000)

        self.setGeometry(250, 150, 800, 475)
        self.center()

        self.readSettings()

    def createConnections(self):
        self.statusBar.outputLogButton.clicked.connect(self.showOutputDialog)
        self.krakenUI.graphViewWidget.rigLoaded.connect(self.krakenMenu.buildRecentFilesMenu)
        self.krakenUI.graphViewWidget.rigLoadedConfig.connect(self.krakenMenu.setCurrentConfigByName)
        self.krakenUI.graphViewWidget.rigNameChanged.connect(self.krakenMenu.updateRigNameLabel)

    def eventFilter(self, source, event):
        if event.type()== QtCore.QEvent.WindowActivate:
            for focusInCb in self._focusInCallbacks:
                focusInCb()

            return True

        if event.type()== QtCore.QEvent.WindowDeactivate:
            for focusOutCb in self._focusOutCallbacks:
                focusOutCb()

            return True

        return QtWidgets.QMainWindow.eventFilter(self, source, event)

    def getKrakenUI(self):
        return self.krakenUI

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    # =========
    # Settings
    # =========
    def getSettings(self):
        return self.settings

    def writeSettings(self):
        self.settings.beginGroup('MainWindow')
        self.settings.setValue('size', self.size())
        self.settings.setValue('pos', self.pos())
        self.settings.setValue('preferences', json.dumps(self.preferences.getPreferences()))
        self.settings.endGroup()
        self.krakenMenu.writeSettings(self.settings)
        self.krakenUI.writeSettings(self.settings)

    def readSettings(self):
        self.settings.beginGroup('MainWindow')
        self.resize(self.settings.value('size', self.size()))
        self.move(self.settings.value('pos', self.pos()))
        self.preferences.loadPreferences(json.loads(self.settings.value('preferences', '{}')))
        self.settings.endGroup()

        self.krakenMenu.readSettings(self.settings)
        self.krakenUI.readSettings(self.settings)

    # =======
    # Events
    # =======
    def addFocusInCallback(self, method):
        """Adds a callback to the focus in event."""

        self._focusInCallbacks.append(method)

    def addFocusOutCallback(self, method):
        """Adds a callbak to the focus out event."""

        self._focusOutCallbacks.append(method)

    def closeEvent(self, event):

        msgBox = QtWidgets.QMessageBox(self)
        msgBox.setObjectName('SaveMessageBox')
        msgBox.setWindowTitle("Kraken Editor")
        msgBox.setText("You are closing Kraken.")
        msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Save)

        ret = msgBox.exec_()

        if ret == QtWidgets.QMessageBox.Cancel:
            event.ignore()
            return

        elif ret == QtWidgets.QMessageBox.Save:
            self.kraken_ui.graphViewWidget.saveRigPreset()

            self.statusBar.showMessage('Closing')

        self.writeSettings()

        # Clear widget handler of any widgets otherwise references to deleted
        # widgets remain.
        for handler in logger.handlers:
            if type(handler).__name__ == 'WidgetHandler':
                handler.clearWidgets()

    def showOutputDialog(self):

        self.outputDialog.show()
        self.outputDialog.textWidget.moveCursor(QtGui.QTextCursor.End)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    splash = KrakenSplash(app)
    splash.show()

    window = KrakenWindow()
    window.show()

    splash.finish(window)

    sys.exit(app.exec_())
