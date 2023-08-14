#!/usr/bin/python3
"""Define a child class MyInt."""


class MyInt(int):
    """Interchanges in toperators == and !="""

    def __eq__(self, other):
        """Change == to != behaviour."""
        return super().__ne__(other)

    def __ne__(self, other):
        """change != to == behaviour."""
        return super().__eq__(other)
