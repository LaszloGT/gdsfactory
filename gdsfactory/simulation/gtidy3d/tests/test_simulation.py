from __future__ import annotations

import pathlib

from jsondiff import diff
from omegaconf import OmegaConf

import gdsfactory as gf
import gdsfactory.simulation.gtidy3d as gt

# from gdsfactory.simulation.gtidy3d.get_results import get_sim_hash
# def test_simulation_hash() -> None:
#     component = gf.pcells.straight(length=3)
#     sim = gt.get_simulation(component=component)
#     sim_hash = get_sim_hash(sim)
#     sim_hash_reference = "4b0cd0b69d0e1c32a1bf30e1f1ea5b27"
#     assert sim_hash == sim_hash_reference, f"sim_hash_reference = {sim_hash!r}"


def test_simulation(overwrite: bool = False) -> None:
    """export sim in JSON, and then load it again."""
    component = gf.pcells.straight(length=3)
    sim = gt.get_simulation(component=component)

    if overwrite:
        sim.to_file("sim_ref.yaml")  # uncomment to overwrite material

    sim.to_file("sim_run.yaml")

    dirpath = pathlib.Path(__file__).parent
    dref = OmegaConf.load(dirpath / "sim_ref.yaml")
    drun = OmegaConf.load(dirpath / "sim_run.yaml")

    d = diff(dref, drun)
    assert len(d) == 0, d


if __name__ == "__main__":
    # test_simulation_hash()
    test_simulation(overwrite=True)

    # test_simulation()
    # component = gf.pcells.straight(length=3)
    # sim = gt.get_simulation(component=component)
    # sim.to_file("sim_ref.yaml")
    # sim.to_file("sim_run.yaml")

    # dref = OmegaConf.load("sim_ref.yaml")
    # drun = OmegaConf.load("sim_run.yaml")

    # d = diff(dref, drun)
