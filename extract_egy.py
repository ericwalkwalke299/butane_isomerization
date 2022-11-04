def extract_egy(path):
    with open(path[0]+'/OUTCAR') as f:
        content = f.readlines()
    for line in content:
        if 'energy' in line and 'without' in line and 'entropy' in line and 'sigma' in line:
            energy_zero = float(line.split()[-1])
    return energy_zero

