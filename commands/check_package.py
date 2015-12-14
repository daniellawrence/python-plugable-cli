import sys
sys.path.append("..")
import clickcommander
spec_cli = clickcommander.ClickCommander("spec")


cmd_map = {
    'all': {'app_name': 'zsh'},
    'spec': {'app_name': 'zsh-common'},
}


@spec_cli.register("check-package", cmd_map)
def cli_app_version(app_name):
    return "app: {0}".format(app_name)
