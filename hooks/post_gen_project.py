#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os

# Generate new SECRET_KEY
with open('./.env', 'a') as f:
    import random
    import string
    try:
        letters = string.ascii_letters
    except AttributeError:
        letters = string.letters
    allowed_chars = string.digits + letters + string.punctuation
    secret_key = ''.join([random.SystemRandom().choice(allowed_chars) for i in range(50)])
    print('SECRET_KEY=' + secret_key, file=f)

# We need .env in cookiecutter's git, but not in project's
with open('./.gitignore', 'a') as f:
    print('.env', file=f)

# We want cookiecutter to create media and static but not
# including the .gitignore in the project or else we'll get
# modified status from git when/if these are cleaned.
os.remove('./public/media/.gitignore')
os.remove('./public/static/.gitignore')
