import numpy as np
def free_egy_correct(path, ads_or_gas = 'ads', T = 673.15):
    kB = 8.617e-5
    with open(path[0]+'/freq/freq.dat') as f:
        content = f.readlines()
    output = False
    count=0
    freqs = []
    for line in content:
        line = line.strip()
        if int(line[-1]) == 1:
            freqs.append(100.0)
        elif int(line[-1]) == 0:
            line = line.split()
            if float(line[0]) < 100.0:
                freqs.append(100.0)
            elif float(line[0]) > 100.0:
                freqs.append(float(line[0]))
            else:
                print('error reading frequencies')
        else:
            print('error reading frequencies')
    freqs = np.asarray(freqs)
    if ads_or_gas == 'ads':
        freqs = 0.5*4.13566e-15*3.00e10*freqs + kB*T*np.log(1-np.exp(-(4.13566e-15*3.00e10*freqs)/(kB*T)))
#        print('entropy_ads',np.sum(kB*T*np.log(1-np.exp(-(4.13566e-15*3.00e10*freqs)/(kB*T)))))
#        print('ZPE_ads',0.5*4.13566e-15*3.00e10*freqs)
    elif ads_or_gas == 'gas':
        freqs = 0.5*4.13566e-15*3.00e10*freqs
    else:
        print('ads_or_gas must be ads or gas')
    correction = np.sum(freqs)
    return correction

