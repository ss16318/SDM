## DISPLAYS IMAGES

import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np

def display( im , Title ):

    im_array = sitk.GetArrayFromImage(im)                     #creates array of image
    
    plt.figure()                                              #creates figure for plot
    plt.imshow( (im_array)[int(im_array.shape[0]/2), :, :])   #takes halfway slice of transverse view
    plt.clim(-1600, 1600)                                     #sets extremes of color map
    cbar  = plt.colorbar()                                    #displays colorbar
    ax = plt.gca()                                            #gets plot axis
    ax.invert_yaxis()                                         #flips y-axis for intuitive view
    ax.set_ylabel("Pixels (0.5mm spacing)")                   #y axis label
    ax.set_xlabel("Pixels (0.5mm spacing)")                   #x axis label
    cbar.ax.set_ylabel("Intensity (HU)" , fontsize = 10)       #colorbar title
    plt.title(Title + " (Transverse view)")                   #adds title to plot                   
    
    #same setup for frontal view
    plt.figure()
    plt.imshow((im_array)[:, int(im_array.shape[1]/2) ,:])    
    plt.clim(-1600, 1600)
    cbar  = plt.colorbar() 
    ax = plt.gca()
    ax.invert_yaxis()
    ax.set_ylabel("Pixels (0.5mm spacing)")
    ax.set_xlabel("Pixels (0.5mm spacing)")
    cbar.ax.set_ylabel("Intensity (HU)" , fontsize = 10)
    plt.title(Title + " (Frontal view)")
    
    #same setup for saggital view
    plt.figure()
    plt.imshow((im_array)[:, :, int(im_array.shape[2]/2)])
    plt.clim(-1600, 1600)
    cbar  = plt.colorbar() 
    ax = plt.gca()
    ax.invert_yaxis()
    ax.set_ylabel("Pixels (0.5mm spacing)")
    ax.set_xlabel("Pixels (0.5mm spacing)")
    cbar.ax.set_ylabel("Intensity (HU)" , fontsize = 10)
    plt.title(Title + " (Saggital view)")
    
    return plt.show()                                        #displays figures                             

## DISPLAYS DEFORMATION FIELD MAPS
def display4D( im , Title ):

    im_array = sitk.GetArrayFromImage(im) 
    
    plt.figure()
    plt.imshow((im_array)[int(im_array.shape[0]/2), :, : , 0])    #note extra dimension being called
    cbar  = plt.colorbar() 
    plt.clim(-20, 25)
    ax = plt.gca()
    ax.invert_yaxis()
    ax.set_ylabel("Pixels (0.5mm spacing)")                   
    ax.set_xlabel("Pixels (0.5mm spacing)")                   
    cbar.ax.set_ylabel("Deformation vector length (Pixels)" , fontsize = 10)       
    plt.title(Title + " (Transverse view)")
    
    plt.figure()
    plt.imshow((im_array)[:, int(im_array.shape[0]/2) ,: , 1])
    cbar  = plt.colorbar() 
    plt.clim(-20, 25)
    ax = plt.gca()
    ax.invert_yaxis()
    ax.set_ylabel("Pixels (0.5mm spacing)")                   
    ax.set_xlabel("Pixels (0.5mm spacing)")                   
    cbar.ax.set_ylabel("Deformation vector length (Pixels)" , fontsize = 10)
    plt.title(Title + " (Frontal view)")
    
    plt.figure()
    plt.imshow((im_array)[:, :, int(im_array.shape[0]/2) , 2])
    cbar  = plt.colorbar() 
    plt.clim(-20, 25)
    ax = plt.gca()
    ax.invert_yaxis()
    ax.set_ylabel("Pixels (0.5mm spacing)")                   
    ax.set_xlabel("Pixels (0.5mm spacing)")                   
    cbar.ax.set_ylabel("Deformation vector length (Pixels)" , fontsize = 10)
    plt.title(Title + " (Saggital view)")
    
    return plt.show()

