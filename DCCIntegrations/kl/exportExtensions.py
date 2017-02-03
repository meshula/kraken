import os
import sys
import optparse

import FabricEngine.Core as FabricCore

def argOpts():

    prog = os.path.basename(__file__)
    usage = "usage: %prog extensionA extensionB output_file [options]"
    parser = optparse.OptionParser(usage, version="%prog 1.0")

    parser.add_option("-s", "--suffix", dest="suffix",
                      help="Suffix to use for the extensions.")

    description = optparse.OptionGroup(parser, "Description", "Exports one or more extensions into a json package.")

    parser.add_option_group(description)

    options, args = parser.parse_args()

    options.name = None
    if len(args) < 2:
        print "\nPlease provide the name of the extension(s) and the output file."
        exit(1)

    return (options, args)


def main():

    options, args = argOpts()
    suffix = ""

    client = FabricCore.createClient()
    if not hasattr(client, 'exportKLExtensions'):
        raise Exception('This build of Fabric does not have the exportKLExtensions feature enabled.')

    if not options.suffix:
        raise Exception('You need to specify the --suffix option.')
    suffix = options.suffix
    flags=client.RegisterKLExtension_Flag_AutoNamespace

    extensions = args[:-1]
    outputfile = args[-1]

    for ext in extensions:
        print 'Loading extension ' + str(ext)
        try:
            client.loadExtension(ext)
        except Exception as e:
            print "Caught exception: " + str(e)
            return

    json = None
    try:
        json = client.exportKLExtensions(
            extensions,
            suffix,
            flags=flags
            )
    except Exception as e:
        print "Caught exception: " + str(e)
        return     

    client = None

    open(outputfile, 'wb').write(json)
    print 'Created json package %s' % outputfile

if __name__ == "__main__":
    main()
