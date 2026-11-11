#!/usr/bin/env python3


import sys

from scripts import *
from scripts.molecules import *

sim = ReadLammpsData(sys.argv[1])


name = "out"
output = Writer(sim, name)
output.write_xyz(name + ".xyz")
output.write_lammps(name + ".data")
