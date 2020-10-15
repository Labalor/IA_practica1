# HOMEWORK 1: DISPERSION ATMOSFERICA

# Necessary packages are imported
import numpy as np
from functions import *
from atmospheric_parameters import *
from tabulate import tabulate

'''
The values of difference of refractions relative to a given wavelength are calculated
Also zenith angles are calculated
'''

# Zenith angles from 0 to 60 degrees
z = np.linspace(0, 60, 6)

# Evaluation of the refractive index for each wavelength
delta_ref_350 = delta_ref(lambda1, lambda_ref, T, P, f, z)
delta_ref_500 = delta_ref(lambda2, lambda_ref, T, P, f, z)
delta_ref_920 = delta_ref(lambda3, lambda_ref, T, P, f, z)

# Evaluation of seeing value for each wavelength
seeing_350 = seeing(lambda1, z)
seeing_500 = seeing(lambda2, z)
seeing_920 = seeing(lambda3, z)

'''
Construction of tables of values
'''

# LAMBDA VALUES
lambda_values = [['lambda (microns)', 'value'], ['lambda 1', lambda1], ['lambda 2', lambda2], ['lambda 3', lambda3], ['lambda ref', lambda_ref]]

# ATMOSPHERIC PARAMETER VALUES
atmospheric_parameter_values = [['parameter (units)', 'value'], ['temperature (°C)', T], ['pressure (hPa)', P], ['water vapor pressure (hPa)', f]]

# ZENITH ANGLE VALUES
zenith_values = [['zenith angle (arc seconds)', 'value'], ['angle 1', z[0]], ['angle 2', z[1]], ['angle 3', z[2]], ['angle 4', z[3]], ['angle 5', z[4]], ['angle 6', z[5]]]

# ATMOSPHERIC DIFERENTIAL REFRACTION VALUES
delta_values = [['lambda (microns)', 'value', 'ATMOSPHERIC DIFERENTIAL REFRACTION VALUES (arc seconds)'], ['lambda 1', lambda1, delta_ref_350], ['lambda 2', lambda2, delta_ref_500], 
['lambda 3', lambda3, delta_ref_920]]

# SEEING DIAMETER VALUES
seeing_values = [['lambda (microns)', 'value', 'SEEING DIAMETER VALUES (arc seconds)'], ['lambda 1', lambda1, seeing_350], ['lambda 2', lambda2, seeing_500], 
['lambda 3', lambda3, seeing_920]]


def print_tables():
	'''   
    Tables of different values we have calculated

    Returns
    -------
    graphic
        Tables of different values calculated are displayed on screen
    '''
	# LAMBDA VALUES
	print('\n LAMBDA VALUES \n')
	print(tabulate(lambda_values, headers='firstrow', tablefmt='fancy_grid'))

	# ATMOSPHERIC PARAMETER VALUES
	print('\n ATMOSPHERIC PARAMETER VALUES \n')
	print(tabulate(atmospheric_parameter_values, headers='firstrow', tablefmt='fancy_grid'))

	# ZENITH ANGLE VALUES
	print('\n ZENITH ANGLE VALUES \n')
	print(tabulate(zenith_values, headers='firstrow', tablefmt='fancy_grid'))

	# ATMOSPHERIC DIFERENTIAL REFRACTION VALUES
	print('\n ATMOSPHERIC DIFERENTIAL REFRACTION VALUES \n     (for each value of zenith angle) \n')
	print(tabulate(delta_values, headers='firstrow', tablefmt='fancy_grid'))

	# SEEING DIAMETER VALUES
	print('\n     SEEING DIAMETER VALUES \n (for each value of zenith angle) \n')
	print(tabulate(seeing_values, headers='firstrow', tablefmt='fancy_grid'))

	print('\n')
