import os
import sys
import json

from kraken.ui.Qt import QtWidgets

import types

import maya
from maya import cmds
import maya.OpenMaya as OpenMaya
import maya.OpenMayaUI as OpenMayaUI
import maya.OpenMayaMPx as OpenMayaMPx

import pymel.core as pm

try:
    from shiboken import wrapInstance
except:
    from shiboken2 import wrapInstance

import kraken
from kraken import plugins
from kraken.core.objects.rig import Rig
from kraken.ui.kraken_window import KrakenWindow
from kraken.ui.kraken_splash import KrakenSplash

from kraken.helpers.utility_methods import prepareToSave, prepareToLoad

from kraken_examples.biped.biped_guide_rig import BipedGuideRig

os.environ['KRAKEN_DCC'] = 'Maya'


def getMayaWindow():
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(ptr), QtWidgets.QWidget)


# =========
# Commands
# =========
class OpenKrakenEditorCmd(OpenMayaMPx.MPxCommand):
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    # Invoked when the command is run.
    def doIt(self, args):

        isSetToCentimeters = True
        if pm.currentUnit( query=True, linear=True ) != 'cm':
            result = pm.confirmDialog(
                title='Confirm Change Units?',
                message='Kraken currently only supports scene units in centimeters.\nDo you want to switch to centimeters?',
                button=['Yes', 'No'],
                defaultButton='Yes',
                cancelButton='No',
                dismissString='No')

            if result == 'Yes':
                pm.currentUnit(linear='cm')
                OpenMaya.MGlobal.displayWarning('Kraken: Scene units changed to centimeters.')
            else:
                OpenMaya.MGlobal.displayWarning('Kraken: Open Cancelled.')
                isSetToCentimeters = False

        if isSetToCentimeters is True:
            app = QtWidgets.QApplication.instance()
            if not app:
                app = QtWidgets.QApplication([])

            for widget in app.topLevelWidgets():
                if widget.objectName() == 'KrakenMainWindow':
                    widget.showNormal()
                    widget.activateWindow() # bring to front

                    return

            splash = KrakenSplash(app)
            splash.show()

            window = KrakenWindow(parent=getMayaWindow())
            window.show()

            splash.finish(window)

    # Creator
    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(OpenKrakenEditorCmd())


class KrakenBipedBuildGuideCmd(OpenMayaMPx.MPxCommand):

    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    def isUndoable(self):
        return True

    def doIt(self, args):

        result = pm.promptDialog(title='Kraken: Build Biped',
                                 message='Rig Name',
                                 button=['OK', 'Cancel'],
                                 defaultButton='OK',
                                 cancelButton='Cancel',
                                 text='Biped')

        if result == 'OK':
            guideName = pm.promptDialog(query=True, text=True)
            guideName.replace(' ', '')
            guideName += '_guide'

            guideRig = BipedGuideRig(guideName)

            builder = plugins.getBuilder()

            OpenMaya.MGlobal.displayInfo('Kraken: Building Guide Rig: ' + guideName)

            try:
                main_window = pm.ui.Window(pm.MelGlobals.get('gMainWindow'))
                main_win_width = pm.window(main_window, query=True, width=True)

                buildMsgWin = pm.window("KrakenBuildBipedWin",
                                        title="Kraken: Build Biped",
                                        width=200,
                                        height=100,
                                        sizeable=False,
                                        titleBar=False,
                                        leftEdge=(main_win_width / 2) - 100)

                buildMsglayout = pm.verticalLayout(spacing=10)
                buildMsgText = pm.text('Kraken: Building Biped')
                buildMsglayout.redistribute()
                buildMsgWin.show()

                pm.refresh()

                builtRig = builder.build(guideRig)

                return builtRig

            finally:
                if pm.window("KrakenBuildBipedWin", exists=True) is True:
                    pm.deleteUI(buildMsgWin)

        else:
            OpenMaya.MGlobal.displayWarning('Kraken: Build Guide Rig Cancelled!')

    # Creator
    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(KrakenBipedBuildGuideCmd())


class KrakenBipedBuildRigCmd(OpenMayaMPx.MPxCommand):
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    def isUndoable(self):
        return True

    def doIt(self, argList):

        selObjects = self.parseArgs(argList)
        if selObjects.length() < 1:
            OpenMaya.MGlobal.displayWarning('Kraken: No objects selected, Build Rig cancelled.')
            return False

        firstObj = OpenMaya.MObject()
        selObjects.getDependNode(0, firstObj)

        firstObjDepNode = maya.OpenMaya.MFnDependencyNode(firstObj)
        if firstObjDepNode.hasAttribute('krakenRig') is False:
            OpenMaya.MGlobal.displayWarning('Kraken: Selected object is not the top node of a Kraken Rig!')
            return False

        guideName = firstObjDepNode.name()
        guideRig = BipedGuideRig(guideName)

        synchronizer = plugins.getSynchronizer()

        if guideRig.getName().endswith('_guide') is False:
            guideRig.setName(guideRig.getName() + '_guide')

        synchronizer.setTarget(guideRig)
        synchronizer.sync()

        rigBuildData = guideRig.getRigBuildData()
        rig = Rig()
        rig.loadRigDefinition(rigBuildData)
        rig.setName(rig.getName().replace('_guide', '_rig'))

        builder = plugins.getBuilder()
        builtRig = builder.build(rig)

        return builtRig

    def parseArgs(self, args):
        argData = OpenMaya.MArgDatabase(self.syntax(), args)

        selObjects = OpenMaya.MSelectionList()
        argData.getObjects(selObjects)

        return selObjects

    @staticmethod
    def syntaxCreator():
        syntax = OpenMaya.MSyntax()

        syntax.useSelectionAsDefault(True)
        syntax.setObjectType(syntax.kSelectionList, 0, 1)

        return syntax

    # Creator
    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(KrakenBipedBuildRigCmd())


class krakenBuildGuideFromRigCmd(OpenMayaMPx.MPxCommand):
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    def isUndoable(self):
        return True

    def doIt(self, argList):

        selObjects = self.parseArgs(argList)
        if selObjects.length() < 1:
            OpenMaya.MGlobal.displayWarning('Kraken: No objects selected, Build Guide From Rig cancelled.')
            return False

        firstObj = OpenMaya.MObject()
        selObjects.getDependNode(0, firstObj)

        firstObjDepNode = maya.OpenMaya.MFnDependencyNode(firstObj)
        if firstObjDepNode.hasAttribute('krakenRig') is False:
            OpenMaya.MGlobal.displayWarning('Kraken: Selected object is not the top node of a Kraken Rig!')
            return False

        guideData = firstObjDepNode.findPlug("krakenRigData").asString()

        rig = Rig()
        jsonData = json.loads(guideData)
        jsonData = prepareToLoad(jsonData)
        rig.loadRigDefinition(jsonData)
        rig.setName(rig.getName())

        builder = plugins.getBuilder()
        builtRig = builder.build(rig)

        # return builtRig
        return None

    def parseArgs(self, args):
        argData = OpenMaya.MArgDatabase(self.syntax(), args)

        selObjects = OpenMaya.MSelectionList()
        argData.getObjects(selObjects)

        return selObjects

    @staticmethod
    def syntaxCreator():
        syntax = OpenMaya.MSyntax()

        syntax.useSelectionAsDefault(True)
        syntax.setObjectType(syntax.kSelectionList, 0, 1)

        return syntax

    # Creator
    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr(krakenBuildGuideFromRigCmd())


def setupKrakenMenu():
    mainWindow = maya.mel.eval('$tmpVar=$gMainWindow')

    menuName = 'Kraken'
    menus = pm.window(mainWindow, q=True, ma=True)
    if menuName in menus:
        return

    krakenMenu = pm.menu(menuName, parent=mainWindow, label=menuName, to=True)

    pm.menuItem(parent=krakenMenu, label="Open Kraken Editor", c="from maya import cmds; cmds.openKrakenEditor()")
    pm.menuItem(parent=krakenMenu, divider=True, dividerLabel='Biped')
    pm.menuItem(parent=krakenMenu, label="Build Biped Guide", c="from maya import cmds; cmds.krakenBipedBuildGuide()")
    pm.menuItem(parent=krakenMenu, label="Build Biped Rig", c="from maya import cmds; cmds.krakenBipedBuildRig()")
    pm.menuItem(parent=krakenMenu, divider=True, dividerLabel='Utils')
    pm.menuItem(parent=krakenMenu, label="Build Guide From Rig", c="from maya import cmds; cmds.krakenBuildGuideFromRig()")
    pm.menuItem(parent=krakenMenu, divider=True, dividerLabel='Resources')
    pm.menuItem(parent=krakenMenu, label="Kraken Web Site", c="import webbrowser; webbrowser.open_new_tab('http://fabric-engine.github.io/Kraken')")
    pm.menuItem(parent=krakenMenu, label="Kraken Documentation", c="import webbrowser; webbrowser.open_new_tab('http://kraken-rigging-framework.readthedocs.io')")
    pm.menuItem(parent=krakenMenu, label="Fabric Forums", c="import webbrowser; webbrowser.open_new_tab('http://forums.fabricengine.com/categories/kraken')")


def removeKrakenMenu():

    mainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
    menus = pm.window(mainWindow, q=True, ma=True)
    if 'Kraken' in menus:
        menuParent = pm.menu('Kraken', query=True, parent=True)
        pm.deleteUI('|'.join([menuParent, 'Kraken']))


def initializePlugin(mobject):

    pm.loadPlugin("FabricMaya", quiet=True)
    pm.pluginInfo('FabricMaya', edit=True, autoload=True)

    pm.loadPlugin("matrixNodes", quiet=True)
    pm.pluginInfo('matrixNodes', edit=True, autoload=True)

    mplugin = OpenMayaMPx.MFnPlugin(mobject)

    try:
        mplugin.registerCommand('openKrakenEditor', OpenKrakenEditorCmd.creator)
    except:
        sys.stderr.write('Failed to register commands: openKrakenEditor')
        raise

    try:
        mplugin.registerCommand('krakenBipedBuildGuide', KrakenBipedBuildGuideCmd.creator)
    except:
        sys.stderr.write('Failed to register commands: krakenBipedBuildGuide')
        raise

    try:
        mplugin.registerCommand('krakenBipedBuildRig', KrakenBipedBuildRigCmd.creator, KrakenBipedBuildRigCmd.syntaxCreator)
    except:
        sys.stderr.write('Failed to register commands: krakenBipedBuildRig')
        raise
    try:
        mplugin.registerCommand('krakenBuildGuideFromRig', krakenBuildGuideFromRigCmd.creator, krakenBuildGuideFromRigCmd.syntaxCreator)
    except:
        sys.stderr.write('Failed to register commands: krakenBuildGuideFromRig')
        raise

    krakenLoadMenu = os.getenv('KRAKEN_LOAD_MENU', 'True')
    if krakenLoadMenu == 'True':
        setupKrakenMenu()


def uninitializePlugin(mobject):

    mplugin = OpenMayaMPx.MFnPlugin(mobject)

    removeKrakenMenu()

    try:
        mplugin.deregisterCommand('openKrakenEditor')
    except:
        sys.stderr.write('Failed to unregister command: openKrakenEditor')

    try:
        mplugin.deregisterCommand('krakenBipedBuildGuide')
    except:
        sys.stderr.write('Failed to unregister command: krakenBipedBuildGuide')

    try:
        mplugin.deregisterCommand('krakenBipedBuildRig')
    except:
        sys.stderr.write('Failed to unregister command: krakenBipedBuildRig')
    try:
        mplugin.deregisterCommand('krakenBuildGuideFromRig')
    except:
        sys.stderr.write('Failed to unregister command: krakenBuildGuideFromRig')
