import h5py
import numpy as np
from PIL import Image



def ConvertH52ImageStack(prefix):
    # read in the raw image data uint8
    with h5py.File('images/{}.h5'.format(prefix), 'r') as hf:
        data = np.array(hf[list(hf.keys())[0]]).astype(np.uint8)

    zres, yres, xres = data.shape

    for iz in range(zres):
        image = Image.fromarray(data[iz,:,:])

        filename = 'images/{}/{:06d}.png'.format(prefix, iz)

        image.save(filename)