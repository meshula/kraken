import webbrowser

import MaxPlus


def openKrakenEditor():
    print 'Open Kraken Editor!'

def openKrakenSite():
    webbrowser.open_new_tab('http://fabric-engine.github.io/Kraken')

def openKrakenDocs():
    webbrowser.open_new_tab('http://kraken-rigging-framework.readthedocs.io')

def openFabricForums():
    webbrowser.open_new_tab('http://forums.fabricengine.com/categories/kraken')



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
