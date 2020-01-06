import numpy as np
from PIL import Image,  ImageDraw

#mandelbrot set is defined by a set of complex number C for which the
#sequence F(Z) remains bounded by a value (say 4) after a maximum set of iterations.
#where F(Z)= Z^2 + C
#
def mandelbrot(creal, cimaginary, maxiterations):
    real = creal
    imag = cimaginary
    for n in range(maxiterations):
        real2 = real*real
        imag2 = imag*imag
        if real2 + imag2 > 4.0:
           return n
        imag = 2 * real * imag + cimaginary
        real = real2 - imag2 + creal
    return 0



def mandelbrot_set(xmin, xmax, ymin, ymax, image_width, image_height, maxiter):
    #create spaced values from x and y min and max values using the height and width specified for the image
    rx = np.linspace(xmin, xmax, image_width)
    ry = np.linspace(ymin, ymax, image_height)
    rgb = np.empty((image_width, image_height))

    #iterate through each pixel of the image and set the RGB value
    for i in range(image_width):
        for j in range(image_height):
            rgb[i, j] = mandelbrot(rx[i], ry[j], maxiter)
    return (rx, ry, rgb)


def mandelbrot_image(xmin, xmax, ymin, ymax, width=10, height=10, maxiter=256):
    dpi = 72
    img_width = dpi * width
    img_height = dpi * height
    x, y, z = mandelbrot_set(xmin, xmax, ymin, ymax, img_width, img_height, maxiter)

    #setup image
    im= Image.new('RGB', (img_width, img_height), (0,0,0))
    draw = ImageDraw.Draw(im)

    for i in range(0, img_width):
        for j in range(0, img_height):
            color = int(z[i,j])
            # BW version
            #draw.point([i,j], (color, color, color))
            #color version
            hue = int(255 * color / maxiter)
            saturation = 255
            value = 255 if color < maxiter else 0
            draw.point([i,j], (hue, saturation, value))

    im.convert('RGB').save('output.png', 'PNG')
    return()

# main program
#mandelbrot_set(-2.0, 0.5, -1.25, 1.25, 1000,1000,80)
mandelbrot_image(-2.0,0.5,-1.25,1.25)