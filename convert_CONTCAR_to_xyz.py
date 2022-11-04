import ase
from ase.io import read, write

struct = read('CONTCAR')
write('initial0001.xyz', struct)
