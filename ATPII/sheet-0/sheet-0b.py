from astropy.coordinates import SkyCoord
from astropy import units as u

# Equinox is defined to be the origin in ICRS
equinox_ICRS = SkyCoord('00h00m +00:00:00', unit=(u.hourangle, u.deg))
equinox_galactic = equinox_ICRS.transform_to("galactic")
equinox_supergalactic = equinox_ICRS.transform_to("supergalactic")

print(equinox_galactic)
print(equinox_supergalactic)

# Script output, equinox position in different coordinate systems
# >>> <SkyCoord (Galactic): (l, b) in deg (96.33728337, -60.18855195)>
# >>> <SkyCoord (Supergalactic): (sgl, sgb) in deg (292.659, 13.231)>
