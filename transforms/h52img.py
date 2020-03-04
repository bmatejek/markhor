import os
import time



from PIL import Image



from markhor.utilities.dataIO import ReadH5File



def ConvertH52ImageStack(prefix):
    # start statistics
    start_time = time.time()

    # read in the raw image data uint8
    data = ReadH5File(prefix)

    zres, yres, xres = data.shape

    # create the directory if it does not already exist
    if not os.path.exists('images/{}'.format(prefix)):
        os.mkdir('images/{}'.format(prefix))

    for iz in range(zres):
        image = Image.fromarray(data[iz,:,:])

        filename = 'images/{}/{:06d}.png'.format(prefix, iz)

        image.save(filename, optimize=True)

    print ('Converted {} in {:0.2f} seconds.'.format(prefix, time.time() - start_time))
