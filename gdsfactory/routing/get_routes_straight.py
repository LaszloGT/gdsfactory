from typing import Dict, List, Union

import gdsfactory as gf
from gdsfactory.components.straight import straight
from gdsfactory.difftest import difftest
from gdsfactory.port import Port
from gdsfactory.types import ComponentOrFactory, Routes


def get_routes_straight(
    ports: Union[List[Port], Dict[str, Port]],
    straight_factory: ComponentOrFactory = straight,
    waveguide: str = "strip",
    **kwargs,
) -> Routes:
    """Returns routes made by 180 degree straights.

    Args:
        ports: List or dict of ports
        straight_factory: function for straight
        **kwargs: straight settings
    """
    ports = list(ports.values()) if isinstance(ports, dict) else ports
    straight = straight_factory(waveguide=waveguide, **kwargs)
    references = [straight.ref() for port in ports]
    references = [ref.connect("W0", port) for port, ref in zip(ports, references)]
    ports = {f"{i}": ref.ports["E0"] for i, ref in enumerate(references)}
    lengths = [straight.length] * len(ports)
    return Routes(references=references, ports=ports, lengths=lengths)


def test_get_routes_straight(check: bool = True):
    c = gf.Component("get_routes_straight")
    pad_array = gf.components.pad_array(pitch=150, port_list=("S",))
    c1 = c << pad_array
    c2 = c << pad_array
    c2.ymax = -200

    routes = get_routes_straight(
        ports=c1.get_ports_list(), waveguide="metal_routing", length=200
    )
    c.add(routes.references)
    if check:
        difftest(c)
    return c


if __name__ == "__main__":
    c = test_get_routes_straight(False)
    c.show()
