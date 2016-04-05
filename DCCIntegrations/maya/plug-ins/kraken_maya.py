import os
import sys
import json

from PySide import QtGui, QtCore

import types

import kraken
import kraken.ui.kraken_window
from kraken.ui.kraken_window import KrakenWindow
from kraken.ui.kraken_window import createSplash

import maya
from maya import cmds
import maya.OpenMaya as OpenMaya
import maya.OpenMayaUI as OpenMayaUI
import maya.OpenMayaMPx as OpenMayaMPx

import pymel.core as pm

try:
    # Maya 2013 with custom pyside build
    import PySide.shiboken as shiboken
except:
    # Maya 2014 and higher
    import shiboken

os.environ['KRAKEN_DCC'] = 'Maya'


def getMayaWindow():
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(ptr), QtGui.QWidget)


# Command
class OpenKrakenEditorCommand(OpenMayaMPx.MPxCommand):
    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

    # Invoked when the command is run.
    def doIt(self,argList):

        app = QtGui.QApplication.instance()
        if not app:
            app = QtGui.QApplication([])

        for widget in app.topLevelWidgets():
            if widget.objectName() == 'KrakenMainWindow':
                widget.showNormal()

                return

        splash = createSplash(app)

        window = KrakenWindow(parent=getMayaWindow())
        window.show()

        splash.finish(window)

    # Creator
    @staticmethod
    def creator():
        return OpenMayaMPx.asMPxPtr( OpenKrakenEditorCommand() )


class KrakenUndoableCmd(OpenMayaMPx.MPxCommand):

  def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

  def isUndoable(self):
        return True

  def doIt(self, argList):
        return 0

  def redoIt(self):
        print "TODO: provide undoable command here."
        return 0

  def undoIt(self):
        print "TODO: provide undoable command here."
        return 0

  @staticmethod
  def creator():
        return OpenMayaMPx.asMPxPtr( KrakenUndoableCmd() )


def setupKrakenMenu():
    mainWindow = maya.mel.eval('$tmpVar=$gMainWindow')

    menuName = 'Kraken'
    menus = pm.window(mainWindow, q=True, ma=True)
    if menuName in menus:
        return

    krakenMenu = pm.menu(menuName, parent=mainWindow, label=menuName, to=True)

    pm.menuItem(parent=krakenMenu, label="Open Kraken Editor", c="from maya import cmds; cmds.openKrakenEditor()")
    pm.menuItem(parent=krakenMenu, divider=True)
    pm.menuItem(parent=krakenMenu, label="Help", c="import webbrowser; webbrowser.open_new_tab('http://fabric-engine.github.io/Kraken')")


def removeKrakenMenu():

    mainWindow = maya.mel.eval('$tmpVar=$gMainWindow')
    menus = pm.window(mainWindow, q=True, ma=True)
    if 'Kraken' in menus:
        menuParent = pm.menu('Kraken', query=True, parent=True)
        pm.deleteUI('|'.join([menuParent, 'Kraken']))

# Initialize the script plug-in
def initializePlugin(mobject):

    pm.loadPlugin("FabricMaya", quiet=True)
    pm.pluginInfo('FabricMaya', edit=True, autoload=True)

    pm.loadPlugin("matrixNodes", quiet=True)
    pm.pluginInfo('matrixNodes', edit=True, autoload=True)

    mplugin = OpenMayaMPx.MFnPlugin(mobject)

    try:
        mplugin.registerCommand('openKrakenEditor', OpenKrakenEditorCommand.creator)
    except:
        sys.stderr.write('Failed to register commands: openKrakenEditor')
        raise

    try:
        mplugin.registerCommand('krakenUndoableCmd', KrakenUndoableCmd.creator)
    except:
        sys.stderr.write('Failed to register commands:krakenUndoableCmd')
        raise

    krakenLoadMenu = os.getenv('KRAKEN_LOAD_MENU', 'True')
    if krakenLoadMenu == 'True':
        setupKrakenMenu()

# Uninitialize the script plug-in
def uninitializePlugin(mobject):

    mplugin = OpenMayaMPx.MFnPlugin(mobject)

    removeKrakenMenu()

    try:
        mplugin.deregisterCommand('openKrakenEditor')
    except:
        sys.stderr.write('Failed to unregister command: openKrakenEditor')

    try:
        mplugin.deregisterCommand('krakenUndoableCmd')
    except:
        sys.stderr.write('Failed to unregister command: krakenUndoableCmd')
