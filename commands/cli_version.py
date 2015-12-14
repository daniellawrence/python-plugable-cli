import sys
sys.path.append("..")
import clickcommander
spec_cli = clickcommander.ClickCommander("spec")


cmd_map = {
    'all': {'version': 'all__'},
    'spec': {'version': 'spec__'},
}


@spec_cli.register("version", cmd_map)
def cli_version(version):
    return "version: {0}".format(version)
