import matplotlib.pyplot as plt
import numpy as np
import timeit

start = timeit.default_timer()

def deg_to_rad(degree):
    return 2*degree*np.pi/360

# loading data
data = np.loadtxt("auger_public_2019_11_03.txt", usecols=(2,3,4,6,7))

# throwing out events with E < 4 EeV
theta = [data[i][0] for i in range(len(data)) if data[i][2] > 4]
phi = [data[i][1] for i in range(len(data)) if data[i][2] > 4]
E = [data[i][2] for i in range(len(data)) if data[i][2] > 4]
longitude = [data[i][3] for i in range(len(data)) if data[i][2] > 4]
latitude = [data[i][4] for i in range(len(data)) if data[i][2] > 4]

end = timeit.default_timer()

print("collected data in %.2f seconds"%(end-start))

# plotting everything
plt.subplot(111, projection="aitoff")
plt.title("galactic coordinates")
plt.scatter(deg_to_rad(-np.array(longitude)),deg_to_rad(np.array(latitude)), c=np.log(E), cmap="BuPu", label="CR sources")              
plt.ylabel(r"$\Theta$")
plt.xlabel(r"$\Phi$")
plt.grid(True)
plt.colorbar(orientation="horizontal",label="log(E)",aspect=90)
plt.legend()

plt.figure()
plt.subplot(111, projection="aitoff")
plt.title("angular coordinates")
plt.scatter(deg_to_rad(np.array(phi)),deg_to_rad(np.array(theta)), c=np.log(E), cmap="BuPu", label="CR sources")
plt.ylabel(r"b")
plt.xlabel(r"l")
plt.grid(True)
plt.colorbar(orientation="horizontal",label="log(E)",aspect=90)
plt.show()
#plt.savefig("auger-plot.png", dpi=400)
