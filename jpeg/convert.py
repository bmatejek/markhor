import os
import time



from PIL import Image



from markhor.utilities.dataIO import ReadH5File



def ConvertH5ToJPEG(prefix):
    # start statistics
    start_time = time.time()

    # read in the raw image data uint8
    data = ReadH5File(prefix)

    zres, yres, xres = data.shape

    # create the directory structure if it does not already exist
    if not os.path.exists('jpegs'): os.mkdir('jpegs')
    if not os.path.exists('jpegs/{}'.format(prefix)):
        os.mkdir('jpegs/{}'.format(prefix))

    # every five and include the worst quality
    qualities = [1] + [iv for iv in range(5, 100, 5)]

    # go through every slice and save for every quality
    for iz in range(zres):
        image = Image.fromarray(data[iz,:,:])
        for quality in qualities:
            filename = 'jpegs/{}/{:06d}-{:02d}.jpg'.format(prefix, iz, quality)

            image.save(filename, quality=quality)

    print ('Created JPEG images for {} in {:0.2f} seconds.'.format(prefix, time.time() - start_time))
