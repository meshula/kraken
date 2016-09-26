import webbrowser

import pymxs
import MaxPlus

from PySide import QtGui

import kraken
from kraken import plugins
from kraken.core.objects.rig import Rig
from kraken.ui.kraken_window import KrakenWindow
from kraken.ui.kraken_splash import KrakenSplash


class _GCProtector(object):
    widgets = []

app = QtGui.QApplication.instance()
if not app:
    app = QtGui.QApplication([])

# ================
# Focus Callbacks
# ================
def maxFocusInCallback():
    MaxPlus.CUI.DisableAccelerators()

def maxFocusOutCallback():
    MaxPlus.CUI.EnableAccelerators()

# ===============
# Menu Callbacks
# ===============
def openKrakenEditor():
    print 'Releasing the Kraken!'

    splash = KrakenSplash(app)
    splash.show()

    try:
        MaxPlus.CUI.DisableAccelerators()
        window = KrakenWindow(parent=MaxPlus.GetQMaxWindow())
        window.addFocusInCallback(maxFocusInCallback)
        window.addFocusOutCallback(maxFocusOutCallback)

        _GCProtector.widgets.append(window)
        window.show()

    except Exception, e:
        print e

    splash.finish(window)


def openKrakenSite():
    webbrowser.open_new_tab('http://fabric-engine.github.io/Kraken')


def openKrakenDocs():
    webbrowser.open_new_tab('http://kraken-rigging-framework.readthedocs.io')


def openFabricForums():
    webbrowser.open_new_tab('http://forums.fabricengine.com/categories/kraken')


# ==============
# Menu Creation
# ==============
def setupMenu():
    menu = None

    openKrakenEditorAction = MaxPlus.ActionFactory.Create('KrakenTools', 'Open Kraken Editor', openKrakenEditor)
    openKrakenWebSiteAction = MaxPlus.ActionFactory.Create('KrakenTools', 'Kraken Web Site', openKrakenSite)
    openKrakenDocsAction = MaxPlus.ActionFactory.Create('KrakenTools', 'Kraken Documentation', openKrakenDocs)
    openFabricForumsAction = MaxPlus.ActionFactory.Create('KrakenTools', 'Fabric Forums', openFabricForums)

    if MaxPlus.MenuManager.MenuExists('Kraken') is True:
        MaxPlus.MenuManager.UnregisterMenu('Kraken')

    krakenMenuBuilder = MaxPlus.MenuBuilder('Kraken')
    if openKrakenEditorAction._IsValidWrapper() is False:
        print "Failed to create Kraken Menu"

    krakenMenuBuilder.AddItem(openKrakenEditorAction)
    krakenMenuBuilder.AddSeparator()
    krakenMenuBuilder.AddItem(openKrakenWebSiteAction)
    krakenMenuBuilder.AddItem(openKrakenDocsAction)
    krakenMenuBuilder.AddItem(openFabricForumsAction)
    menu = krakenMenuBuilder.Create(MaxPlus.MenuManager.GetMainMenu())

    return menu


setupMenu()
