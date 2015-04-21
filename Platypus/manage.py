#!/usr/bin/env python

"""@package manage
Manage.py allows the team to run the application on a local server. 

"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Platypus.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
