import matplotlib.pyplot as plt
import numpy as np

def deg_to_rad(degree):
    return 2*degree*np.pi/360

# loading data
data = np.loadtxt("auger_public_2019_11_03.txt", usecols=(2,3,4))

# throwing out events with E < 4 EeV
theta = [data[i][0] for i in range(len(data)) if data[i][2] > 4]
phi = [data[i][1] for i in range(len(data)) if data[i][2] > 4]
E = [data[i][2] for i in range(len(data)) if data[i][2] > 4]

# plotting everything
plt.figure()
plt.subplot(111, projection="aitoff")
plt.title("Distribution of Auger events")
plt.scatter(deg_to_rad(np.array(phi)),deg_to_rad(np.array(theta)), c=np.log(E), cmap="Blues")
plt.colorbar(label="log(E)")
plt.ylabel(r"$\Theta$ / b")
plt.xlabel(r"$\Phi$ / l")
plt.grid(True)
plt.savefig("auger-plot.png", dpi=400)
plt.show()
