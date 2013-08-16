#!/usr/bin/env python
import os, sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stalktest.settings")
    from django.core.management import execute_from_command_line
    import stalktest.startup as startup
    startup.run()
    execute_from_command_line(sys.argv)
