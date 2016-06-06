
from kraken import plugins
from kraken.core.maths import *
from kraken_components.biped.head_component import HeadComponentGuide, HeadComponentRig

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy


Profiler.getInstance().push("head_build")

headGuide = HeadComponentGuide("head")

headGuide.loadData({
    "headXfo": Xfo(Vec3(0.0, 17.5, -0.5)),
    "eyeLeftXfo": Xfo(tr=Vec3(0.375, 18.5, 0.5), ori=Quat(Vec3(-0.0, -0.707106769085, -0.0), 0.707106769085)),
    "eyeRightXfo": Xfo(tr=Vec3(-0.375, 18.5, 0.5), ori=Quat(Vec3(-0.0, -0.707106769085, -0.0), 0.707106769085)),
    "jawXfo": Xfo(Vec3(0.0, 17.875, -0.275))
})

# Save the hand guide data for persistence.
saveData = headGuide.saveData()

headGuideData = headGuide.getRigBuildData()

head = HeadComponentRig()
head.loadData(headGuideData)

builder = plugins.getBuilder()
builder.build(head)

Profiler.getInstance().pop()

if __name__ == "__main__":
    print Profiler.getInstance().generateReport()
else:
    for each in head.getItems().values():
        # Only log hierarchy for Layer objects as Layers in this test are added to
        # the component since there is no rig object.
        if each.isTypeOf('Layer'):
            logHierarchy(each)
