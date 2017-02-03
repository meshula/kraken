import os
import sys
import optparse

os.environ['KRAKEN_DCC'] = 'KL'

from kraken import plugins
from kraken.core.kraken_system import KrakenSystem
from kraken.core.objects.rig import Rig


def argOpts():

    prog = os.path.basename(__file__)
    usage = "usage: %prog krg_file output_directory [options]"
    parser = optparse.OptionParser(usage, version="%prog 1.0")

    parser.add_option("-c", "--config", dest="config",
                      help="Create the directory structure of a new asset locally.")

    parser.add_option("-p", "--profiling", dest="numframes", type="int",
                      help="Embeds profiling inside the generated rig for the provided number of frames")

    parser.add_option("-f", "--logfile", dest="logfile",
                      help="Stores the profiling results in a file instead of reporting them")

    parser.add_option("-C", "--constants", dest="constants", action="store_true",
                      help="Enables the use of constants for the array indices - thus easier to read code")

    parser.add_option("-n", "--extensionname", dest="extensionname",
                      help="Overrides the name of the extension. By default it is based on the name of the rig in the krg file.")

    description = optparse.OptionGroup(parser, "Description", "Generate a kl character from krg input")

    parser.add_option_group(description)


    options, args = parser.parse_args()

    options.name = None
    if len(args) != 2:
        print "\nPlease provide the rig file to convert and the target folder as command line arguments."
        exit(1)

    if options.config and not os.path.isfile(options.config):
        print "\nCannot read config file path [%s]" % options.config
        exit(1)

    return (options, args)


def main():

    options, args = argOpts()

    ks = KrakenSystem.getInstance()
    numConfigs = len(ks.registeredConfigs)

    if options.config:
        directory, file = os.path.split(options.config)
        filebase, ext = os.path.splitext(file)
        sys.path = [directory] + sys.path  # prepend
        exec("import " + filebase)

        if len(ks.registeredConfigs) > numConfigs:
            configName = next(reversed(ks.registeredConfigs))
            print ("Using config %s from %s" % (configName, options.config))
            ks.getConfigClass(configName).makeCurrent()

        else:
            print ("Failed to use config in %s" % options.config)
            exit()

    guideRig = Rig()
    guideRig.loadRigDefinitionFile(args[0])

    rig = Rig()
    rig.loadRigDefinition(guideRig.getRigBuildData())

    builder = plugins.getBuilder()
    builder.setOutputFolder(args[1])

    config = builder.getConfig()

    config.setMetaData('RigTitle', os.path.split(args[0])[1].partition('.')[0])
    if options.constants:
        config.setMetaData('UseRigConstants', True)
    if options.numframes:
        config.setMetaData('ProfilingFrames', options.numframes)
    if options.logfile:
        config.setMetaData('ProfilingLogFile', options.logfile)
    if options.extensionname:
        config.setMetaData('RigTitle', options.extensionname)

    builder.build(rig)

if __name__ == "__main__":
    main()
