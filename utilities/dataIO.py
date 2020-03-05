import glob
import h5py



import numpy as np



from PIL import Image



def ReadH5File(prefix):
    # return the first h5 dataset from this file
    with h5py.File('images/{}.h5'.format(prefix), 'r') as hf:
        data = np.array(hf[list(hf.keys())[0]]).astype(np.uint8)

    return data



def ReadPNGFiles(prefix):
    compressed_files = sorted(glob.glob('images/{}/*.png'.format(prefix)))

    for iz, filename in enumerate(compressed_files):
        img = np.array(Image.open(filename)).astype(np.uint8)

        if not iz:
            zres = len(compressed_files)
            yres = img.shape[0]
            xres = img.shape[1]

            data = np.zeros((zres, yres, xres), dtype=np.uint8)

        data[iz,:,:] = img

    return data



def ReadJPEGFiles(prefix, parameters):
    # only one parameter corresponding to quality
    compressed_files = sorted(glob.glob('jpegs/{}/*-{}.jpg'.format(prefix, parameters['Quality'])))

    for iz, filename in enumerate(compressed_files):
        img = np.array(Image.open(filename)).astype(np.uint8)

        if not iz:
            zres = len(compressed_files)
            yres = img.shape[0]
            xres = img.shape[1]

            data = np.zeros((zres, yres, xres), dtype=np.uint8)

        data[iz,:,:] = img

    return data



def ReadCompressedFiles(prefix, scheme, parameters):
    if scheme == 'png': return ReadPNGFiles(prefix)
    elif scheme == 'jpeg': return ReadJPEGFiles(prefix, parameters)
    else: assert (False)
