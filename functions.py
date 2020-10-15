# HOMEWORK 1: DISPERSION ATMOSFERICA

# Necessary packages are imported
import numpy as np

def index(lamb, T, P, f):
	'''   
    Study the value of refractive index for a certain temperature, pressure, wavelength and water vapor pressure

	Since observatories are usually located at high altitudes, the index of refraction must be corrected for the
	lower ambient temperature and pressure

    
    Parameters
    ----------
    lambda : float
        The wavelength of light in vacuo [microns]

    T : float
        The air temperature (celsius degrees)

    P : float
        The pressure [mm Hg]

    f : float
        The water vapor pressure [mm Hg]

    Returns
    -------
    float
        Refractive index 
    '''

	lamb2 = 1 / lamb ** 2
	adj_included = (64.328 + 29498.1 / (146 - lamb2) + 255.4 / (41 - lamb2)) * P * (1 + (1.049 - 0.0157 * T) * 10 ** (-6) * P) / (720.883 * (1 + 0.003661 * T)) - f * (0.0624 - 0.000680 * lamb2) / (1 + 0.003661 * T)

	return adj_included * 10 ** (-6) + 1

def delta_ref(lamb, lamb_ref, T, P, f, z):
	'''   
    Study the value of difference of refractions relative to a given wavelength 

	In order to obtain the refractive index, and atmospheric differential refraction relative to a given wavelength
	is then calculated for and object at zenith angle z

    Parameters
    ----------
    lambda : float
        The wavelength of light in vacuo [microns]

    lamba_ref : float
        The air temperature (celsius degrees)

    T : float
        The air temperature (celsius degrees)

    P : float
        The pressure [mm Hg]

    f : float
        The water vapor pressure [mm Hg]

    z : array
        The zenith angle [degrees]

    Returns
    -------
    float
        Refractive index 
    '''

	return 206265 * (index(lamb, T, P, f) - index(lamb_ref, T, P, f)) * np.tan(z * np.pi / 180)

def seeing(lamb,z):
    return 1.2 * 206265 * 0.55 ** 1.2 / (15 * 10 ** 4 * lamb ** 0.2 * (np.cos(z * np.pi / 180)) ** 0.6)