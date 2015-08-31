from split_settings.tools import optional, include
import os

include(
    'settings/base.py',
    'settings/database.py',
    'settings/email.py',
    'settings/secret.py',
    optional('local_settings.py'),

    scope=globals()
)
