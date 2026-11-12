#!/usr/bin/env python3


from makegraphitics.params import Parameterise
from makegraphitics.write_coords import Writer


class Reactor:
    """Base class that performs a reaction on sim object"""

    def react(self, sim):
        """Perform reaction on sim, return with changes"""
        raise NotImplementedError

    def output_snapshot(self, sim, format_="xyz", filename="out"):
        if format_ == "xyz":
            out = Writer(sim)
            out.write_xyz(filename=filename + ".xyz", option="a")
        elif format_ == "lammps":
            sim.generate_connections()
            Parameterise(sim)
            out = Writer(sim)
            out.write_lammps(filename=filename + ".data")
        else:
            raise NotImplementedError
