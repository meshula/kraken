import re
from kraken.core.objects.components.base_example_component import BaseExampleComponent
from kraken.core.objects.component_group import ComponentGroup

from kraken.core.objects.attributes.attribute_group import AttributeGroup
from kraken.core.objects.attributes.scalar_attribute import ScalarAttribute
from kraken.core.objects.attributes.bool_attribute import BoolAttribute




class OSS_Component(BaseExampleComponent):
    """OSS Component object."""

    def __init__(self, name='', parent=None, data=None):

        super(OSS_Component, self).__init__(name, parent=parent, data=data)

        self._color = (155, 155, 200, 255)


        # Declare Inputs Xfos
        self.parentSpaceInputTgt = self.createInput('parentSpace', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.globalSRTInputTgt = self.createInput('globalSRT', dataType='Xfo', parent=self.inputHrcGrp).getTarget()
        self.rigScaleInputAttr = self.createInput('rigScale', dataType='Float', value=1.0, parent=self.cmpInputAttrGrp).getTarget()
        self.drawDebugInputAttr = self.createInput('drawDebug', dataType='Boolean', value=False, parent=self.cmpInputAttrGrp).getTarget()

        if self.getComponentType() == "Guide":
            self.guideSettingsAttrGrp = AttributeGroup("GuideSettings", parent=self)
            self.singleDeformerGroupAttr = BoolAttribute('SingleDeformerGroup', value=True, parent=self.guideSettingsAttrGrp)
            self.mocapAttr = BoolAttribute('mocap', value=False, parent=self.guideSettingsAttrGrp)
            self.globalComponentCtrlSizeInputAttr = ScalarAttribute('globalComponentCtrlSize', value=1.0, minValue=0.0,   maxValue=50.0, parent=self.guideSettingsAttrGrp)
        else: # Rig
            self.deformersLayer = self.getOrCreateLayer('deformers')
            self.deformersParent = self.deformersLayer


    def loadData(self, data):

        super(OSS_Component, self).loadData(data)


        if self.getComponentType() == "Guide":
            pass
        else: # Rig
            self.singleDeformerGroup = bool(data.get("SingleDeformerGroup", True))
            if not self.singleDeformerGroup:
                self.defCmpGrp = ComponentGroup(self.getName(), self, parent=self.deformersLayer)
                self.addItem("defCmpGrp", self.defCmpGrp)
                self.deformersParent = self.defCmpGrp


    def convertToStringList(self, inputString):
        """ tokenizes string argument, returns a list"""
        stringList = re.split(r'[ ,:;]+', inputString)

        # These checks should actually prevent the component_inspector from closing maybe?
        for name in stringList:
            if name and not re.match(r'^[\w_]+$', name):
                # Eventaully specific exception just for component class that display component name, etc.
                raise ValueError("inputString \""+name+"\" contains non-alphanumeric characters in component \""+self.getName()+"\"")

        stringList = [x for x in stringList if x != ""]

        if not stringList:
            return []

        if len(stringList) > len(set(stringList)):
            raise ValueError("Duplicate names in inputString in component \""+self.getName()+"\"")

        return stringList


    def convertToScalarList(self, inputString):
        """ tokenizes string argument, returns a list"""
        stringList = re.split(r'[ ,:;]+', inputString)
        scalarList = []
        # These checks should actually prevent the component_inspector from closing maybe?
        for name in stringList:
            if name:
                try:
                    scalarList.append(float(name))
                except ValueError:
                    raise ValueError("inputString \""+name+"\" cannot be converted to float: \""+self.getName()+"\"")


        # scalarList = [x for x in scalarList if x != ""]

        if not scalarList:
            return []

        if len(scalarList) > len(set(scalarList)):
            raise ValueError("Duplicate names in inputString in component \""+self.getName()+"\"")

        return scalarList
