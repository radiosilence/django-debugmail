django-debugmail
================

Send e-mails to ADMINS instead of their recipients.

Quickstart
----------

::

    pip install django-debugmail

Add this to your development configuration:

::

    EMAIL_BACKEND = 'debugmail.backends.DebugEmailBackend'

