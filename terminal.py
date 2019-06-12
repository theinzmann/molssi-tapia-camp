import numpy as np
import os
import sys

def read(mol_name):
    try:
        file_path = os.path.join('{}.xyz'.format(mol_name))
        data = np.genfromtxt(file_path, dtype='unicode', skip_header=2)
        return data
    except:
        print('File not found.\n')
        exit()

def stripValues(data):
    atom = data[:,0]
    coord = data[:,1:]
    return atom, coord.astype(np.float)

def calcDistances(data):
    n = len(data)
    distance = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            dist = (data[i,0]-data[j,0])**2 + (data[i,1]-data[j,1])**2 + (data[i,2]-data[j,2])**2
            distance[i,j] = np.sqrt(dist)

    return distance

def bondCheck(length, dist=1.5):
    if length > dist or length < 0:
        return False
    else:
        return True

def printResults(header, length):
    bond_def = input('What distance would you like to define the bond as?: ')
    bond_def = float(bond_def)  

    for i in range(len(header)):
        for j in range(len(header)):
            if i > j:
                if bondCheck(length[i,j], dist=bond_def):
                    print('{:>2s} to {:>2s}: {:.5f}'.format(header[i],header[j],length[i,j]))

def main():
    mol_name = input('What is the name of the molecule you would like to open?: ')
    data = read(mol_name)
    name, coord = stripValues(data)
    bond_length = calcDistances(coord)

    printResults(name, bond_length)


if __name__ == '__main__':
    main()