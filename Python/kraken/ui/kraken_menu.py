import logging
import os
import sys
import webbrowser

from kraken.ui.Qt import QtGui, QtWidgets, QtCore
from kraken.ui.preference_editor import PreferenceEditor
from kraken.core import getVersion
from kraken.core.kraken_system import KrakenSystem
from kraken.core.configs.config import Config
from kraken.log import getLogger

logger = getLogger('kraken')


class KrakenMenu(QtWidgets.QWidget):
    """Kraken Menu Widget"""

    def __init__(self, parent=None):
        super(KrakenMenu, self).__init__(parent)
        self.setObjectName('menuWidget')
        self.recentFiles = []

        self.createLayout()
        self.createConnections()


    def createLayout(self):

        self.menuLayout = QtWidgets.QHBoxLayout()
        self.menuLayout.setContentsMargins(0, 0, 0, 0)
        self.menuLayout.setSpacing(0)

        # Menu
        self.menuBar = QtWidgets.QMenuBar()

        # File Menu
        self.fileMenu = self.menuBar.addMenu('&File')
        self.newAction = self.fileMenu.addAction('&New')
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.setObjectName("newAction")

        self.openAction = self.fileMenu.addAction('&Open...')
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.setObjectName("openAction")

        self.saveAction = self.fileMenu.addAction('&Save')
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.setObjectName("saveAction")

        self.saveAsAction = self.fileMenu.addAction('&Save As...')
        self.saveAsAction.setShortcut('Ctrl+Shift+S')
        self.saveAsAction.setObjectName("saveAsAction")

        self.fileMenu.addSeparator()
        self.recentFilesMenu = QtWidgets.QMenu(title='&Recent Files', parent=self.fileMenu)
        self.fileMenu.addMenu(self.recentFilesMenu)


        self.fileMenu.addSeparator()

        self.closeAction = self.fileMenu.addAction('&Close')
        self.closeAction.setShortcut('Ctrl+W')
        self.closeAction.setObjectName("closeAction")

        # Edit Menu
        self.editMenu = self.menuBar.addMenu('&Edit')
        self.copyAction = self.editMenu.addAction('&Copy')
        self.copyAction.setShortcut('Ctrl+C')
        self.pasteAction = self.editMenu.addAction('&Paste')
        self.pasteAction.setShortcut('Ctrl+V')
        self.pasteConnectedAction = self.editMenu.addAction('Paste Connected')
        self.pasteConnectedAction.setShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.SHIFT + QtCore.Qt.Key_V))
        self.editMenu.addSeparator()
        self.pasteMirroredAction = self.editMenu.addAction('Paste Mirrored')
        self.pasteMirroredConnectedAction = self.editMenu.addAction('Paste Mirrored Connected')
        self.editMenu.addSeparator()
        self.editAddBackdropAction = self.editMenu.addAction('Add &Backdrop')
        self.editMenu.addSeparator()
        self.editRigNameAction = self.editMenu.addAction('&Rig Name')
        self.editRigNameAction.setObjectName("editRigNameAction")
        self.editMenu.addSeparator()
        self.editPreferencesAction = self.editMenu.addAction('&Preferences...')
        self.editPreferencesAction.setObjectName("editPreferencesAction")

        # Build Menu
        self.buildMenu = self.menuBar.addMenu('&Build')
        self.buildGuideAction = self.buildMenu.addAction('Build &Guide')
        self.buildGuideAction.setShortcut('Ctrl+G')
        self.buildGuideAction.setObjectName("buildGuideAction")

        self.buildRigAction = self.buildMenu.addAction('Build &Rig')
        self.buildRigAction.setShortcut('Ctrl+B')
        self.buildRigAction.setObjectName("buildRigAction")

        # Tools Menu
        self.toolsMenu = self.menuBar.addMenu('&Tools')
        self.reloadComponentsAction = self.toolsMenu.addAction('Reload Component Modules')
        self.reloadComponentsAction.setShortcut('Ctrl+Shift+R')

        # View Menu
        self.viewMenu = self.menuBar.addMenu('&View')
        self.compLibAction = self.viewMenu.addAction('Component &Library')
        self.compLibAction.setShortcut('Ctrl+Tab')
        self.snapToGridAction = self.viewMenu.addAction('&Snap To Grid')
        self.snapToGridAction.setCheckable(True)

        # Help Menu
        self.helpMenu = self.menuBar.addMenu('&Help')
        self.krakenWebSiteAction = self.helpMenu.addAction('Kraken Web Site')
        self.krakenDocumentationAction = self.helpMenu.addAction('Kraken Documentation')
        self.fabricForumsAction = self.helpMenu.addAction('Fabric Forums')
        self.helpMenu.addSeparator()
        self.aboutKrakenAction = self.helpMenu.addAction('About Kraken')

        # Logo
        logoWidget = QtWidgets.QLabel()
        logoWidget.setObjectName('logoWidget')
        logoWidget.setMinimumHeight(20)
        logoWidget.setMinimumWidth(110)

        logoPixmap = QtGui.QPixmap(':/images/KrakenUI_Logo.png')
        logoWidget.setPixmap(logoPixmap)

        # Config Widget
        self.configsParent = QtWidgets.QFrame(self)
        self.configsParent.setObjectName('configParent')
        self.configsParent.setFrameStyle(QtWidgets.QFrame.NoFrame)
        self.configsParent.setMinimumWidth(160)

        self.configsLayout = QtWidgets.QVBoxLayout()
        self.configsLayout.setContentsMargins(0, 0, 0, 0)
        self.configsLayout.setSpacing(0)

        self.configsWidget = QtWidgets.QComboBox()
        self.configsWidget.setAutoFillBackground(True)
        self.configsWidget.setObjectName('configWidget')
        self.configsWidget.setMinimumWidth(160)
        self.configsWidget.addItem('Default Config', userData='Default Config')

        self.configsLayout.addWidget(self.configsWidget)
        self.configsParent.setLayout(self.configsLayout)

        configs = KrakenSystem.getInstance().getConfigClassNames()
        for config in configs:
            self.configsWidget.addItem(config.split('.')[-1], userData=config)

        self.rigNameLabel = RigNameLabel('Rig Name:')

        # Add Widgets
        self.menuLayout.addWidget(logoWidget, 0)
        self.menuLayout.addWidget(self.menuBar, 3)
        self.menuLayout.addWidget(self.configsParent, 0)
        self.menuLayout.addWidget(self.rigNameLabel, 0)

        self.setLayout(self.menuLayout)

    def createConnections(self):

        krakenUIWidget = self.parentWidget().getKrakenUI()
        graphViewWidget = krakenUIWidget.graphViewWidget

        # File Menu Connections
        self.newAction.triggered.connect(graphViewWidget.newRigPreset)
        self.newAction.triggered.connect(self.updateRigNameLabel)

        self.saveAction.triggered.connect(graphViewWidget.saveRigPreset)
        self.saveAsAction.triggered.connect(graphViewWidget.saveAsRigPreset)
        self.openAction.triggered.connect(graphViewWidget.openRigPreset)
        self.openAction.triggered.connect(self.updateRigNameLabel)
        self.closeAction.triggered.connect(self.window().close)

        # Edit Menu Connections
        self.copyAction.triggered.connect(graphViewWidget.copy)
        self.pasteAction.triggered.connect(graphViewWidget.pasteUnconnected)
        self.pasteConnectedAction.triggered.connect(graphViewWidget.paste)
        self.pasteMirroredAction.triggered.connect(graphViewWidget.pasteMirrored)
        self.pasteMirroredConnectedAction.triggered.connect(graphViewWidget.pasteMirroredConnected)
        self.editAddBackdropAction.triggered.connect(graphViewWidget.addBackdrop)
        self.editRigNameAction.triggered.connect(graphViewWidget.editRigName)
        self.editPreferencesAction.triggered.connect(self.editPreferences)

        # Build Menu Connections
        self.buildGuideAction.triggered.connect(graphViewWidget.buildGuideRig)
        self.buildRigAction.triggered.connect(graphViewWidget.buildRig)

        # Tools Menu Connections
        self.reloadComponentsAction.triggered.connect(self.reloadAllComponents)

        # View Menu Connections
        self.compLibAction.triggered.connect(krakenUIWidget.resizeSplitter)
        self.snapToGridAction.triggered[bool].connect(graphViewWidget.graphView.setSnapToGrid)

        # Help Menu Connections
        self.krakenWebSiteAction.triggered.connect(self.krakenWebSite)
        self.krakenDocumentationAction.triggered.connect(self.krakenDocumentation)
        self.fabricForumsAction.triggered.connect(self.fabricForums)
        self.aboutKrakenAction.triggered.connect(self.aboutKraken)

        # Config Widget
        self.configsWidget.currentIndexChanged.connect(self.setCurrentConfig)

        # Rig Name Label
        self.rigNameLabel.clicked.connect(graphViewWidget.editRigName)


    # ==========
    # Callbacks
    # ==========
    def krakenWebSite(self):
        webbrowser.open_new_tab('http://fabric-engine.github.io/Kraken')

    def krakenDocumentation(self):
        webbrowser.open_new_tab('http://kraken-rigging-framework.readthedocs.io')

    def fabricForums(self):
        webbrowser.open_new_tab('http://forums.fabricengine.com/categories/kraken')

    def aboutKraken(self):
        aboutMsgBox = QtWidgets.QMessageBox(self)
        aboutMsgBox.setWindowTitle('About Kraken')
        aboutMsgBox.setText("You are using Kraken v{}".format(getVersion()))
        aboutMsgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        aboutMsgBox.exec_()

    # ============
    # Preferences
    # ============
    def editPreferences(self):
        krakenUIWidget = self.window().getKrakenUI()
        graphViewWidget = krakenUIWidget.graphViewWidget

        preferenceEditor = PreferenceEditor(parent=graphViewWidget)
        preferenceEditor.exec_()

    # =======
    # Events
    # =======
    def updateRigNameLabel(self):
        krakenUIWidget = self.window().getKrakenUI()

        graphViewWidget = krakenUIWidget.graphViewWidget
        newRigName = graphViewWidget.guideRig.getName()

        self.rigNameLabel.setText('Rig Name: ' + newRigName)


    def setCurrentConfig(self, index=None):
        if index is None:
            index = self.configsWidget.currentIndex()
        else:
            self.configsWidget.setCurrentIndex(index)

        if index == 0:
            Config.makeCurrent()
        else:
            ks = KrakenSystem.getInstance()
            configs = ks.getConfigClassNames()
            configClass = ks.getConfigClass(configs[index-1])
            configClass.makeCurrent()

    def setCurrentConfigByName(self, configName):
        """Set the current config by the name of the config.

        If the config doesn't exist it won't change itself.

        Args:
            configName (str): Config name.

        Returns:
            Type: True if successful.

        """

        if configName == 'Default Config':
            self.setCurrentConfig(0)
        else:
            configs = KrakenSystem.getInstance().getConfigClassNames()
            if configName in configs:
                itemIndex = self.configsWidget.findData(configName, role=QtCore.Qt.UserRole)
                self.setCurrentConfig(itemIndex)
            else:
                logger.warn("Config from rig file could not be found: {}".format(configName))

        return True


    def reloadAllComponents(self):
        krakenUIWidget = self.window().krakenUI
        graphViewWidget = krakenUIWidget.graphViewWidget

        openedFile = graphViewWidget.openedFile
        # Sync and Store Graph Data
        graphViewWidget.synchGuideRig()
        rigData = graphViewWidget.guideRig.getData()

        # Create New Rig And Reload All Components.
        graphViewWidget.newRigPreset()
        if krakenUIWidget.nodeLibrary.componentTreeWidget.generateData():
            logger.info('Success Reloading Modules')
        else:
            logger.error('Error Reloading Modules')

        if openedFile:
            self.window().setWindowTitle('Kraken Editor - ' + openedFile + '[*]')
            graphViewWidget.openedFile = openedFile

        krakenUIWidget.nodeLibrary.componentTreeWidget.buildWidgets()

        # Load Saved Data And Update Widget
        graphViewWidget.guideRig.loadRigDefinition(rigData)
        graphViewWidget.graphView.displayGraph(graphViewWidget.guideRig)


    def writeSettings(self, settings):
        krakenUIWidget = self.window().krakenUI
        graphViewWidget = krakenUIWidget.graphViewWidget

        configIndex = self.configsWidget.currentIndex()
        configName = self.configsWidget.itemData(configIndex)

        settings.beginGroup("KrakenMenu")
        settings.setValue("currentConfigName", configName)
        settings.setValue("snapToGrid", graphViewWidget.graphView.getSnapToGrid())
        settings.setValue("recentFiles", ';'.join(self.recentFiles))

        settings.endGroup()

    def readSettings(self, settings):
        krakenUIWidget = self.window().krakenUI
        graphViewWidget = krakenUIWidget.graphViewWidget

        settings.beginGroup('KrakenMenu')

        if settings.contains('currentConfigName'):
            configName = str(settings.value('currentConfigName', 0))

            if configName != 'Default Config':

                configs = KrakenSystem.getInstance().getConfigClassNames()
                if configName in configs:
                    itemIndex = self.configsWidget.findData(configName, role=QtCore.Qt.UserRole)
                    self.setCurrentConfig(itemIndex)

        if settings.contains('snapToGrid'):
            if settings.value('snapToGrid') == 'true':
                snapToGrid = True
            else:
                snapToGrid = False

            self.snapToGridAction.setChecked(snapToGrid)
            graphViewWidget.graphView.setSnapToGrid(snapToGrid)

        if settings.contains('recentFiles'):
            recentFiles = settings.value('recentFiles', None)

            if recentFiles is not None:
                fileSplit = recentFiles.split(';')
                for eachFile in fileSplit[:4]:
                    if os.path.exists(eachFile):
                        self.recentFiles.append(eachFile)

        settings.endGroup()

        self.buildRecentFilesMenu()


    def buildRecentFilesMenu(self, newFilePath=None):

        self.recentFilesMenu.clear()

        self.recentFiles = self.recentFiles[:4]
        if newFilePath is not None:
            for i, eachFile in enumerate(list(self.recentFiles)):
                if eachFile == newFilePath:
                    self.recentFiles.pop(i)

            self.recentFiles = [newFilePath] + self.recentFiles

        for recentFile in self.recentFiles:

            action = self.recentFilesMenu.addAction(recentFile)
            action.triggered.connect(self.openRecentFile)

    def openRecentFile(self):
        krakenUIWidget = self.window().krakenUI
        graphViewWidget = krakenUIWidget.graphViewWidget
        graphViewWidget.loadRigPreset(self.sender().text())


class RigNameLabel(QtWidgets.QLabel):

    clicked = QtCore.Signal()

    def __init__(self, parent=None):
        super(RigNameLabel, self).__init__(parent)
        self.setObjectName('rigNameLabel')
        self.setToolTip('Double Click to Edit')

    def mouseDoubleClickEvent(self, event):
        self.clicked.emit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    KrakenMenu()

    sys.exit(app.exec_())