#
# Kraken unit test environment and execution.
# Place this in the /unittest folder and 
# change path to Fabric directory.
#

unix_to_windows_path()
{
  echo "$@" | sed 's/^\/\(.\)\//\1:\\/' | sed 's/\//\\/g'
}

echo "Setting up Fabric Engine environment:"

FABRIC_DIR=/c/Users/USERNAME/Documents/fabric/FabricEngine-2.4.0-Windows-x86_64
export FABRIC_DIR
echo "  Set FABRIC_DIR=\"$FABRIC_DIR\""

PATH="$FABRIC_DIR/bin:$PATH"
export PATH
echo "  Set PATH=\"$PATH\""

KRAKEN_PATH=$( cd "$( dirname "${BASH_SOURCE[0]}" )/../" && pwd )
export KRAKEN_PATH

PYTHON_VERSION=$(python -c 'import sys; print "%u.%u" % sys.version_info[:2]')
FABRIC_PYPATH="$FABRIC_DIR/Python/$PYTHON_VERSION"
KRAKEN_PYPATH="$KRAKEN_PATH/Python"
FABRIC_OS=$(uname -s)
if [[ "$FABRIC_OS" == *W32* ]] || [[ "$FABRIC_OS" == *W64* ]]; then
  PYTHONPATH="$(unix_to_windows_path $FABRIC_PYPATH);$(unix_to_windows_path $KRAKEN_PYPATH);$PYTHONPATH"
else
  PYTHONPATH="$FABRIC_PYPATH:$KRAKEN_PYPATH:$PYTHONPATH"
fi
export PYTHONPATH
echo "  Set PYTHONPATH=\"$PYTHONPATH\""

FABRIC_EXTS_PATH="$FABRIC_DIR/Exts:$KRAKEN_PATH/Exts"

export FABRIC_EXTS_PATH
echo "  Set FABRIC_EXTS_PATH=\"$FABRIC_EXTS_PATH\""

FABRIC_DFG_PATH="$FABRIC_DIR/Presets/DFG:$KRAKEN_PATH/Presets/DFG"

export FABRIC_DFG_PATH
echo "  Set FABRIC_DFG_PATH=\"$FABRIC_DFG_PATH\""

python -m unittest discover

read -n1 -r -p "Press any key to continue..."

