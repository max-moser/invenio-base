# SPDX-FileCopyrightText: 2015-2018 CERN.
# SPDX-License-Identifier: MIT

"""Command Line Interface for Invenio."""

from .app import create_cli

cli = create_cli()

if __name__ == "__main__":  # pragma: no cover
    cli()
