import gdsfactory as gf

if __name__ == "__main__":
    """FIXME: this case needs to be implemented for get_bundle."""

    w = h = 10
    c = gf.Component()
    pad_south = gf.components.pad_array(
        port_list=["S"],
        pitch=15,
    )
    pl = c << pad_south
    pb = c << pad_south
    pl.rotate(90)
    pb.move((100, -100))

    pbports = pb.get_ports_list()
    ptports = pl.get_ports_list()

    routes = gf.routing.get_bundle(pbports, ptports)
    for route in routes:
        c.add(route.references)
    c.show()
