from astropy.coordinates import SkyCoord
from astropy import units as u

# Virgo has R.A 12h27m = 12.45h = 12.45h * 15°/h = 186.75°
# Virgo has Dec 12° 43' = 12° + (43' * 1°/60' ) = 12.717°

# from what I read ICRS seems to correspond to equatorial coordinates
virgo_cluster_ICRS = SkyCoord('12h27m +12:43', unit=(u.hourangle, u.deg))
virgo_cluster_galactic = virgo_cluster_ICRS.transform_to("galactic")

print(virgo_cluster_ICRS)
print(virgo_cluster_galactic)

# Script output, coordinates of virgo cluster in different coordinates
# >>> <SkyCoord (ICRS): (ra, dec) in deg (186.75, 12.71666667)>
# >>> <SkyCoord (Galactic): (l, b) in deg (280.08096214, 74.49390662)>
