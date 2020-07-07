import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
# %matplotlib inline

def mandelbrot(creal,cimag,maxiter):
    real = creal
    imag = cimag
    for n in range(maxiter):
        real2 = real*real
        imag2 = imag*imag
        if real2 + imag2 > 4.0:
            return n
        imag = 2* real*imag + cimag
        real = real2 - imag2 + creal
    return 0


def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))

    for i in range(width):
        for j in range(height):
            n3[i,j] = mandelbrot(r1[i],r2[j],maxiter)
    return (r1,r2,n3)


def mandelbrot_image(xmin, xmax, ymin, ymax, width=10, height=10, maxiter=256):
    dpi = 72
    img_width = dpi * width
    img_height = dpi * height
    x, y, z = mandelbrot_set(xmin, xmax, ymin, ymax, img_width, img_height, maxiter)
    print('returned')
    fig, ax = plt.subplots(figsize=(width, height), dpi=72)
    ticks = np.arange(0, img_width, 3 * dpi)
    x_ticks = xmin + (xmax - xmin) * ticks / img_width
    plt.xticks(ticks, x_ticks)
    y_ticks = ymin + (ymax - ymin) * ticks / img_width
    plt.yticks(ticks, y_ticks)
    ax.imshow(z.T, origin='lower')
    return()


# main program: sample run time code below
# takes four arguements with arguement 0 being the name of this module
# mandelbrot_set(-2.0, 0.5, -1.25, 1.25, 1000,1000,80)
# mandelbrot_image(-2.0,0.5,-1.25,1.25)
main():
    if len(sys.argv) > 4: 
        xmin, xmax, ymin, ymax = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
    else:
        xmin, xmax, ymin, ymax = -2.0, 0.5, -1.25, 1.25
        
    mandelbrot_image(xmin, xmax, ymin, ymax)
    
    
if _name_ = '_main_':
    main()
