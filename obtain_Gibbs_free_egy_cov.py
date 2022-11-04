#Eric A. Walker
#This script reads DFT calculation results and produces the Gibbs free energy covariance matrix.
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20})
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import extract_egy
from extract_egy import extract_egy
import extract_egy_ensemble
from extract_egy_ensemble import extract_egy_ensemble
import free_egy_correct
from free_egy_correct import free_egy_correct
import NIST_entropy_calc
from NIST_entropy_calc import NIST_entropy_calc
######################## Obtain free energies of DFT calculations:
T = 2243.15
dict_gas = {
'n_butane': ['./vasp0001.07'],
'butane_ts': ['./vasp0001.03'],
'iso_butane': ['./vasp0001.01']
}

n_butane_gas_energy = np.asarray(extract_egy(dict_gas['n_butane']))
n_butane_gas_free_energy_ensemble = np.asarray(extract_egy_ensemble(dict_gas['n_butane']))
n_butane_gas_ZPE = free_egy_correct(dict_gas['n_butane'], ads_or_gas = 'gas')
n_butane_gas_entropy = 0.0031243845*T*0.07205
n_butane_gas_free_energy = n_butane_gas_energy + n_butane_gas_ZPE - n_butane_gas_entropy
dict_gas['n_butane'].extend([n_butane_gas_free_energy, n_butane_gas_free_energy_ensemble])

iso_butane_gas_energy = np.asarray(extract_egy(dict_gas['iso_butane']))
iso_butane_gas_free_energy_ensemble = np.asarray(extract_egy_ensemble(dict_gas['iso_butane']))
iso_butane_gas_ZPE = free_egy_correct(dict_gas['iso_butane'], ads_or_gas = 'gas')
iso_butane_gas_entropy = 0.0031243845*T*0.0726 
iso_butane_gas_free_energy = iso_butane_gas_energy + iso_butane_gas_ZPE - iso_butane_gas_entropy
dict_gas['iso_butane'].extend([iso_butane_gas_free_energy, iso_butane_gas_free_energy_ensemble])

butane_ts_gas_energy = np.asarray(extract_egy(dict_gas['butane_ts']))
butane_ts_gas_free_energy_ensemble = np.asarray(extract_egy_ensemble(dict_gas['butane_ts']))
butane_ts_gas_ZPE = free_egy_correct(dict_gas['butane_ts'], ads_or_gas = 'gas')
butane_ts_gas_entropy = 0.0031243845*T*0.0726
butane_ts_gas_free_energy = butane_ts_gas_energy + butane_ts_gas_ZPE - butane_ts_gas_entropy
dict_gas['butane_ts'].extend([butane_ts_gas_free_energy, butane_ts_gas_free_energy_ensemble])

delta_G_1 = dict_gas['iso_butane'][1] - dict_gas['n_butane'][1]
delta_G_act_bar = dict_gas['butane_ts'][1] - dict_gas['n_butane'][1]

delta_G_1_ensemble = dict_gas['iso_butane'][2] - dict_gas['n_butane'][2] 
delta_G_act_bar_ensemble = dict_gas['butane_ts'][2] - dict_gas['n_butane'][2]

print('mu delta_G_1', delta_G_1, '\n')
print('mu delta_act_bar', delta_G_act_bar, '\n')

G_stacked = np.stack((delta_G_1_ensemble, delta_G_act_bar_ensemble), axis = 0)  
print('G_stacked: ', G_stacked)
G_cov = np.cov(G_stacked)

print('G_cov (eV) same order as mu',G_cov) 

