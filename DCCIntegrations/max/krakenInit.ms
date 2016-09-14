-- loads Python interpreter if it is not loaded already
python.Init()

-- grab current directory and format to krakenHook.py file
krakeEnvScriptPath = "C:\Users\Eric\Documents\dev\kraken\DCCIntegrations\max\scripts\krakenEnv.py"
krakeMenuScriptPath = "C:\Users\Eric\Documents\dev\kraken\DCCIntegrations\max\scripts\krakenMenu.py"

-- Execute Python startup modules
python.ExecuteFile krakeEnvScriptPath
python.ExecuteFile krakeMenuScriptPath