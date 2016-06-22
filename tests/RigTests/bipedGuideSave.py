import json
import os
import tempfile

from kraken.core.maths import *

from kraken.helpers.utility_methods import prepareToSave, prepareToLoad

from kraken_examples.biped.biped_guide_rig import BipedGuideRig


bipedGuide = BipedGuideRig('Biped_Guide')
guideData = bipedGuide.getData()
pureJSON = prepareToSave(guideData)

tmpFilePath = os.path.join(os.getcwd(), 'bipedGuideSaveTest.krg')
try:
    with open(tmpFilePath, 'w+b') as tempFile:
        tempFile.write(json.dumps(pureJSON, indent=2))

    with open(tmpFilePath, 'r') as tempFile:
        jsonData = json.load(tempFile)
        jsonData = prepareToLoad(jsonData)

        for k, v in jsonData.iteritems():
            print k

            if k == 'components':
                for i in xrange(len(v)):
                    print '\t' + v[i]['name']

finally:
    os.remove(tmpFilePath)
