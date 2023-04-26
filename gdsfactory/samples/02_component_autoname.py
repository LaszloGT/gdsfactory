"""When you create pcells you have to make sure they have unique names.

the cell decorator gives unique names to pcells that depend on their
parameters

"""

from __future__ import annotations

import gdsfactory as gf


def test_autoname() -> None:
    c1 = gf.pcells.straight(length=5)
    assert c1.name.split("_")[0] == "straight"
