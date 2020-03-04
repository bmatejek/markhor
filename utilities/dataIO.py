import h5py



import numpy as np



def ReadH5File(prefix):
    # return the first h5 dataset from this file
    with h5py.File('images/{}.h5'.format(prefix), 'r') as hf:
        data = np.array(hf[list(hf.keys())[0]]).astype(np.uint8)

    return data
