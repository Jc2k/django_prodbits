===============
django_prodbits
===============

Some reusable bits and pieces for making Django and virtualenvs nicer in production.

Django settings
===============

django_prodbits generates a ``bin/django`` in your virtualenv with a settings hook that looks for a ``settings.json`` or ``settings.py`` in the ``etc`` directory of the virtualenv.

This avoids having to source anything before running your code.

