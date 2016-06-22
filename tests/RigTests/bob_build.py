from kraken import plugins
from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy

from kraken_examples.bob_rig import BobRig


Profiler.getInstance().push("bob_build")

bobRig = BobRig("char_bob")

builder = plugins.getBuilder()
builder.build(bobRig)

Profiler.getInstance().pop()


if __name__ == "__main__":
    print Profiler.getInstance().generateReport()
else:
    logHierarchy(bobRig)
