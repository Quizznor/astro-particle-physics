from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
from astropy import units as u
import numpy as np

# individual points
spring_equinox_ICRS = SkyCoord('00h00m +00:00:00', unit=(u.hourangle, u.deg))
virgo_cluster_ICRS = SkyCoord('12h27m +12:43', unit=(u.hourangle, u.deg))
sagittarius_A_GAL = SkyCoord('00h00m +00:00:00', unit=(u.hourangle, u.deg),frame="galactic")

#the galactic plane
galactic_plane_ra, galactic_plane_dec = np.linspace(-np.pi,np.pi,100), np.zeros(100)
galactic_plane_GAL = SkyCoord(galactic_plane_ra, galactic_plane_dec, unit=(u.deg, u.deg),frame="galactic")

# galactic frame
spring_equinox_GAL = spring_equinox_ICRS.galactic
virgo_cluster_GAL = virgo_cluster_ICRS.galactic


plt.subplot(111, projection="aitoff")
plt.title("galactic coordinates")
plt.scatter(spring_equinox_GAL.l,spring_equinox_GAL.b,label="Spring Equinox")
plt.scatter(virgo_cluster_GAL.l,virgo_cluster_GAL.b,label="Virgo Cluster")
plt.scatter(sagittarius_A_GAL.l,sagittarius_A_GAL.b,label="Sagittarius A*")
plt.plot(galactic_plane_GAL.l,galactic_plane_GAL.b,label="Galactic plane")

plt.grid()
plt.legend()


# icrs frame
sagittarius_A_ICRS = sagittarius_A_GAL.icrs
galactic_plane_ICRS = galactic_plane_GAL.icrs

plt.figure()
plt.subplot(111, projection="aitoff")
plt.title("equatorial coordinates")
plt.scatter(spring_equinox_ICRS.ra,spring_equinox_ICRS.dec,label="Spring Equinox")
plt.scatter(virgo_cluster_ICRS.ra,virgo_cluster_ICRS.dec,label="Virgo Cluster")
plt.scatter(sagittarius_A_ICRS.ra,sagittarius_A_ICRS.dec,label="Sagittarius A*")
plt.plot(galactic_plane_ICRS.ra,galactic_plane_ICRS.dec,label="ICRSactic plane")

plt.grid()
plt.legend()

plt.show()

#print(spring_equinox_ICRS)
#print(galactic_plane_GAL)
