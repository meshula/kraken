-- loads Python interpreter if it is not loaded already
python.Init()

curScriptPath = getSourceFileName()

-- grab current directory and format to krakenHook.py file
curPath = "C:\Users\Eric\Documents\dev\kraken\DCCIntegrations\max\scripts\krakenMenu.py"

-- Execute Python startup modules
python.ExecuteFile curPath