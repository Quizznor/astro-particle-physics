import matplotlib.pyplot as plt
import numpy as np
import h5py

with h5py.File("events.h5", "r") as hdf5_file:
    print(hdf5_file.keys())
    energies_from_hdf5 = np.array([entry[2] for entry in hdf5_file["array"]])

E = np.linspace(17,19,21)
hist, bins, patches = plt.hist(energies_from_hdf5,bins=20,log=True)
coeffs = np.polyfit(E,bins,1)

print(coeffs)

plt.show()
