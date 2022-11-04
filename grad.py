#!/usr/bin/python

import sys
sys.path.append('/projects/academic/ericwalk/software/ase')

from ase import Atoms,Atom
from ase.visualize import view
from ase.calculators.emt import EMT
from ase.calculators.nwchem import NWChem
from ase.calculators.vasp import Vasp
from ase.constraints import FixAtoms
from ase.io import write
from ase.io import read
import sys
import os
import shutil
from ase.lattice.surface import fcc111,add_adsorbate,fcc100,fcc110,hcp0001,bcc111

nargs = len(sys.argv)
argv1 = sys.argv[1]
argv2 = sys.argv[2]

#print 'argv1: ',argv1
fname = 'scratch/structure'+argv1
folder = 'scratch/vasp'+argv1

#lattice and initial atom setup for unit cell
#slab = fcc111('Pt', size=(3,4,4), vacuum=10)
molecule =  Atoms('C4H10')
molecule.set_cell([[8.3155757467537992, 0.0000000000000000, 0.0000000000000000],
     [5.5437171645025325, 9.6019997917100568, 0.0000000000000000],
     [0.0000000000000000, 0.0000000000000000, 26.7896391656699997]])
#add_adsorbate(slab, molecule, 2.5, 'fcc')

#current position read in
moleculeatoms = read(fname, format='xyz')

#print 'atoms: ',slabatoms.get_positions()
molecule.set_positions(moleculeatoms.get_positions())

#set up Calculators
#mask = [atom.tag > 2 for atom in slab]
#slab.set_constraint(FixAtoms(mask=mask))
calc = Vasp(lwave=True,lcharg=False,lreal='Auto',kpts=[4,4,1],prec='acc',addgrid=True,icharg=2,ispin=1,encut=400,ediff=1e-3,nelm=100,algo='normal',ismear=0,sigma=0.05,istart=1,ibrion=-1,npar=8,xc='BEEF-vdW')
molecule.set_calculator(calc)

cwd = os.getcwd()
if not os.path.exists(folder):
    os.makedirs(folder)
os.chdir(folder)

energy = - molecule.get_potential_energy() 
grads = - molecule.get_forces()

#print grads
f = open('GRAD'+argv1, 'w')
f.write(str(energy))
f.write('\n')
f.write(str(grads))
f.write('\n')
f.close()

shutil.copy2('GRAD'+argv1, cwd+'/scratch')
os.chdir(cwd)
