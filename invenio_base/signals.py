# SPDX-FileCopyrightText: 2017-2018 CERN.
# SPDX-License-Identifier: MIT

"""Signals for application creation."""

from blinker import Namespace

_signals = Namespace()

app_created = _signals.signal("app-created")
"""Signal sent when the base Flask application have been created.

Parameters:
- ``sender`` - the application factory function.
- ``app`` - the Flask application instance.

Example receiver:

.. code-block:: python

   def receiver(sender, app=None, **kwargs):
       # ...
"""

app_loaded = _signals.signal("app-loaded")
"""Signal sent when the Flask application have been fully loaded.

Parameters:
- ``sender`` - the application factory function.
- ``app`` - the Flask application instance.

Example receiver:

.. code-block:: python

   def receiver(sender, app=None, **kwargs):
       # ...
"""
