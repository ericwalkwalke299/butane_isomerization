def extract_egy_ensemble(path):
    with open(path[0]+'/OUTCAR') as f:
        content = f.readlines()
    output = False
    count=0
    energies = []
    for line in content:
        line = line.strip()
        if output == True and count <2000:
            energies.append(float(line))
            count +=1
        if 'ensemble' in line:
            output = True
            count = 0
            energies = []
    return energies

