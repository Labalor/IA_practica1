# HOMEWORK 1: DISPERSION ATMOSFERICA

# Necessary packages are imported
import numpy as np
import matplotlib.pyplot as plt
from functions import *
from atmospheric_parameters import *
from study import *


# Differential atmospheric refraction with respect to lambda of 450

def graphic1():
	'''   
    Study the value of difference of refractions relative to a given wavelength 

    Returns
    -------
    graphic
        Differential atmospheric refraction for a reference value of 0.45 microns 
    '''
	fig, ax = plt.subplots(1, figsize=(14,10))
	ax.grid(True)
	ax.plot(z, delta_ref_350, 'bo-', label=r'$\lambda = 350nm$')
	ax.plot(z, delta_ref_500, 'go-', label=r'$\lambda = 500nm$')
	ax.plot(z, delta_ref_920, 'ro-', label=r'$\lambda = 920nm$')

	ax.axes.xaxis.set_label_text("Zenith angle (degrees)", fontdict={"size":16})
	ax.axes.yaxis.set_label_text("Diferential refraction (arc seconds)", fontdict={"size":16})
	fig.suptitle("Differential atmospheric refraction for a reference value of $\lambda=0.45$ microns",fontsize = 20)
	ax.legend(loc=3, fontsize = 14)
# 	plt.savefig('figura1.png')
	plt.show()
	

def graphic2():
	'''   
    Study the value of difference of refractions relative to a given wavelength including seeing effect

    Returns
    -------
    graphic
        Differential atmospheric refraction including seeing effect
    '''
	fig, ax = plt.subplots(1, figsize=(14,10))
	ax.grid(True)
	ax.plot(z, delta_ref_350, 'bo', label=r'$\lambda = 350nm$')
	ax.plot(z, delta_ref_500, 'go', label=r'$\lambda = 500nm$')
	ax.plot(z, delta_ref_920, 'ro', label=r'$\lambda = 920nm$')
	for i in range(len(z)):
		ax.plot(z[i], delta_ref_350[i], 'bo', ms=seeing_350[i]*118)
		ax.plot(z[i], delta_ref_500[i], 'go', ms=seeing_500[i]*118)
		ax.plot(z[i], delta_ref_920[i], 'ro', ms=seeing_920[i]*118)

	ax.axes.xaxis.set_label_text("Zenith angle (degrees)", fontdict={"size":16})
	ax.axes.yaxis.set_label_text("Diferential refraction (arc seconds)", fontdict={"size":16})

	fig.suptitle("Differential atmospheric refraction for a reference value of $\lambda=0.45$ microns \n including seeing effect", fontsize = 20)
	ax.legend(loc=3, fontsize = 14)
# 	plt.savefig('figura2.png')
	plt.show()	
