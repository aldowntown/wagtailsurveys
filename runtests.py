#!/usr/bin/env python

import sys
import os
import shutil
import warnings

from django.core.management import execute_from_command_line


os.environ['DJANGO_SETTINGS_MODULE'] = 'wagtailsurveys.tests.settings'


def runtests():
    # Don't ignore DeprecationWarnings
    only_wagtailsurveys = r'^wagtailsurveys(\.|$)'
    warnings.filterwarnings('default', category=DeprecationWarning, module=only_wagtailsurveys)
    warnings.filterwarnings('default', category=PendingDeprecationWarning, module=only_wagtailsurveys)

    args = sys.argv[1:]
    argv = sys.argv[:1] + ['test'] + args
    try:
        execute_from_command_line(argv)
    finally:
        from wagtailsurveys.tests.settings import STATIC_ROOT, MEDIA_ROOT
        shutil.rmtree(STATIC_ROOT, ignore_errors=True)
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)


if __name__ == '__main__':
    runtests()
