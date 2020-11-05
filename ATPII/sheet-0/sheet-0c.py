from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
from astropy import units as u
from varname import nameof
import numpy as np

def draw_object(object,frame,label):
    if frame=="icrs":
        phi, theta = -object.ra.wrap_at(180*u.degree), -object.dec
    elif frame=="galactic":
        phi, theta = -object.galactic.l.wrap_at(180*u.degree), object.galactic.b
    elif frame=="supergalactic":
        phi, theta = object.supergalactic.sgl.wrap_at(180*u.degree), object.supergalactic.sgb

    if len(phi.flatten())==1:
        plt.scatter(phi.radian,theta.radian,label=label,s=60)
    else:
        plt.scatter(phi.radian,theta.radian,label=label,s=10)

# individual points
spring_equinox = SkyCoord('00h00m +00:00:00', unit=(u.hourangle, u.deg))
virgo_cluster = SkyCoord('12h27m +12:43', unit=(u.hourangle, u.deg))
sagittarius_A = SkyCoord('00h00m +00:00:00', unit=(u.hourangle, u.deg),frame="galactic").icrs
galactic_plane_l, galactic_plane_b = np.linspace(-np.pi,np.pi,100), np.zeros(100)
galactic_plane = SkyCoord(galactic_plane_l, galactic_plane_b, unit=(u.radian, u.radian),frame="galactic").icrs

objects = [spring_equinox, sagittarius_A, virgo_cluster, galactic_plane]
labels = ["Spring Equinox", "Sagittarius A*","Virgo Cluster","Galactic Plane"]


# icrs frame
plt.subplot(111, projection="aitoff")
plt.title("ICRS coordinate frame")
for i in range(4):
    draw_object(objects[i],"icrs",labels[i])

plt.grid()
plt.legend()


# galactic frame
plt.figure()
plt.subplot(111, projection="aitoff")
plt.title("galactic coordinate frame")
for i in range(4):
    draw_object(objects[i],"galactic",labels[i])

plt.grid()
plt.legend()


# galactic frame
plt.figure()
plt.subplot(111, projection="aitoff")
plt.title("supergalactic coordinate frame")
for i in range(4):
    draw_object(objects[i],"supergalactic",labels[i])

plt.grid()
plt.legend()

plt.show()
