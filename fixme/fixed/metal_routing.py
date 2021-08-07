"""
Routing metal lines to pads

"""

import gdsfactory as gf

if __name__ == "__main__":
    c = gf.Component()
    ncols = 8
    nrows = 8
    pad_pitch = 150.0
    pad_width = 80
    nheaters = ncols * nrows
    heaters = c << gf.components.array(
        component=gf.components.straight_with_heater(
            port_orientation_input=180, port_orientation_output=0
        ),
        pitch=80,
        axis="y",
        n=nheaters,
    )
    pads = c << gf.components.pad_array_2d(
        ncols=ncols,
        nrows=nrows,
        pitchx=pad_pitch,
        pitchy=pad_pitch,
        port_list=("E",),
        pad_settings=dict(width=pad_width),
    )

    pads.y = 0
    heaters.y = 0
    pads.xmax = heaters.xmin - 1000
    metal_routes = gf.routing.get_bundle(
        heaters.get_ports_list(port_type="dc", orientation=180),
        pads.get_ports_list(),
        waveguide="metal_routing",
    )
    for metal_route in metal_routes:
        c.add(metal_route.references)

    c.show()
