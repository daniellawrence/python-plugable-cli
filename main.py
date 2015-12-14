#!/usr/bin/env python
import clickcommander


if __name__ == '__main__':        
    spec_cli = clickcommander.ClickCommander("spec")
    import commands
    
    print spec_cli.execute("version")
    print spec_cli.execute("check-package")
