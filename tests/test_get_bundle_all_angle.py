from __future__ import annotations

from pytest_regressions.data_regression import DataRegressionFixture

import gdsfactory as gf

# from gdsfactory.difftest import difftest


def test_get_bundle_all_angle(
    data_regression: DataRegressionFixture, check: bool = True
) -> gf.Component:
    c = gf.Component()

    mmi = gf.pcells.mmi2x2(width_mmi=10, gap_mmi=3)
    mmi1 = c << mmi
    mmi2 = c << mmi

    mmi2.move((100, 10))
    mmi2.rotate(30)

    routes = gf.routing.get_bundle_all_angle(
        mmi1.get_ports_list(angle=0),
        [mmi2.ports["o2"], mmi2.ports["o1"]],
        connector=None,
    )
    lengths = {}
    for i, route in enumerate(routes):
        c.add(route.references)
        lengths[i] = route.length

    if check:
        data_regression.check(lengths)
        # difftest(c)

    return c


if __name__ == "__main__":
    c = test_get_bundle_all_angle(None, False)
    c.show(show_ports=True)
