-- loads Python interpreter if it is not loaded already
python.Init()

dotNet.loadAssembly "System"
env = dotNetClass "system.Environment"
krakenPath = env.GetEnvironmentVariable "KRAKEN_PATH"

if krakenPath != undefined do
(
    krakeEnvScriptPath = krakenPath + "\DCCIntegrations\max\scripts\krakenEnv.py"
    krakeMenuScriptPath = krakenPath + "\DCCIntegrations\max\scripts\krakenMenu.py"
    
    -- Execute Python startup modules
    python.ExecuteFile krakeEnvScriptPath
    python.ExecuteFile krakeMenuScriptPath
)