-- loads Python interpreter if it is not loaded already
python.Init()

-- grab current directory and format to krakenHook.py file
currFilePath = getFilenamePath ( getThisScriptFilename() )
krakeEnvScriptPath = currFilePath + "scripts\krakenEnv.py"
krakeMenuScriptPath = currFilePath + "scripts\krakenMenu.py"

-- Execute Python startup modules
python.ExecuteFile krakeEnvScriptPath
python.ExecuteFile krakeMenuScriptPath