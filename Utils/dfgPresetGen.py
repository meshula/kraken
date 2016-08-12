import fnmatch
import os
import shutil
import subprocess

import FabricEngine.Core as fabric


fabricPath = os.environ.get("FABRIC_DIR")
kl2dfgPath = os.path.join(fabricPath, 'bin', 'kl2dfg.exe')
krakenPath = os.environ.get('KRAKEN_PATH')
krakenExtsPath = os.path.join(krakenPath, 'Exts')
krakenDFGPath = os.path.join(krakenPath, 'Presets', 'DFG', 'Kraken', 'Exts')
krakenDFGSolverPath = os.path.join(krakenPath, 'Presets', 'DFG', 'Kraken', 'Exts', 'Solvers')

# Clear the Existing Presets
if os.path.exists(krakenDFGPath):
    shutil.rmtree(krakenDFGPath)

os.mkdir(krakenDFGPath)

# ========================
# Generate KL Ext Presets
# ========================
for root, dirs, files in os.walk(krakenExtsPath):
    if root.endswith(('KrakenAnimation', 'KrakenForCanvas')):
        continue

    getExts = lambda x: [f for f in x if f.endswith(".fpm.json")]

    exts = getExts(files)
    if len(exts) < 1:
        continue

    for ext in exts:
        extPath = os.path.join(root, ext)

        subprocess.call("{} {} {}".format(kl2dfgPath, extPath, krakenDFGPath), shell=True)

# ===========================
# Create User Facing Presets
# ===========================
options = {
    'guarded': True
}

client = fabric.createClient(options)
dfgHost = client.getDFGHost()

for root, dirs, files in os.walk(krakenDFGSolverPath):
    constructorPresets = fnmatch.filter(files, '*Solver_Constructor.canvas')
    solvePresets = fnmatch.filter(files, '*Solver_Solve.canvas')

    if len(constructorPresets) < 1 or len(solvePresets) < 1:
        continue

    for solver in constructorPresets:
        solvePresetName = solver.replace('_Constructor', '_Solve')
        if solvePresetName not in solvePresets:
            print "Can't find matching solve preset: " + solvePresetName
            continue

        solverName = solver.replace('_Constructor', '').replace('.canvas', '')
        solverOutputPath = os.path.join(root, solverName + '.canvas')
        if os.path.exists(solverOutputPath) is True:
            os.remove(solverOutputPath)

        print "{} {}".format("Creating Preset:",  solverName)
        print "  Solver Path: " + root
        print ""

        # Create preset
        dfgBinding = dfgHost.createBindingToNewGraph()
        dfgExec = dfgBinding.getExec()
        dfgExec.setTitle(solverName)
        dfgExec.addExtDep('Kraken')

        # Generate the Kraken relative preset path
        folders = []
        path = root
        while True:
            path, folder = os.path.split(path)

            if folder == "Solvers":
                break
            elif folder != "":
                folders.append(folder)
            else:
                if path != "":
                    folders.append(path)

                break

        folders.reverse()

        krakenPresetPath = ['Kraken', 'Exts', 'Solvers']
        solverPresetPath = '.'.join(krakenPresetPath + folders)
        constructorPresetPath = "{}.{}".format(solverPresetPath, solverName + "_Constructor")
        solvePresetPath = "{}.{}".format(solverPresetPath, solverName + "_Solve")

        var = dfgExec.addVar('solver', solverName, 'Kraken')

        solverConstructor = dfgExec.addInstFromPreset(constructorPresetPath)
        dfgExec.connectTo(solverConstructor + '.result', var + '.value')
        dfgExec.setNodeMetadata(solverConstructor, "uiGraphPos", "{\"x\":-300.0,\"y\":0.0}", False)

        solverSolve = dfgExec.addInstFromPreset(solvePresetPath)
        dfgExec.connectTo(var + '.value', solverSolve + '.this')
        dfgExec.setNodeMetadata(solverSolve, "uiGraphPos", "{\"x\":200.0,\"y\":0.0}", False)

        dfgExec.connectTo(solverSolve + '.this', 'exec')

        # Get all input ports for the constructor node and expose them
        portTypeMap = {
            0: 'In',
            1: 'IO',
            2: 'Out'
        }

        solverSolveBinding = dfgHost.createBindingToPreset(solvePresetPath)
        solverSolveTempNode = solverSolveBinding.getExec()
        for i in xrange(solverSolveTempNode.getExecPortCount()):
            portName = solverSolveTempNode.getExecPortName(i)
            portConnectionType = portTypeMap[solverSolveTempNode.getExecPortType(i)]
            rtVal = solverSolveBinding.getArgValue(portName)
            portDataType = rtVal.getTypeName().getSimpleType()

            if portConnectionType == 'In' and portName not in ('exec', 'this'):
                solverParamInPort = dfgExec.addExecPort(portName, client.DFG.PortTypes.In, portDataType)
                dfgExec.connectTo(solverParamInPort, solverSolve + '.' + portName)

            if portConnectionType == 'IO' and portName not in ('exec', 'this'):
                solverParamOutPort = dfgExec.addExecPort(portName, client.DFG.PortTypes.Out, portDataType)
                # dfgExec.connectTo(solverParamOutPort, solverSolve + '.' + portName)
                dfgExec.connectTo(solverSolve + '.' + portName, solverParamOutPort)

        content = dfgBinding.exportJSON()
        with open(solverOutputPath, "w") as solverPresetFile:
            solverPresetFile.write(content)

