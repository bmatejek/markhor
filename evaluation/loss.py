import numpy as np



from markhor.utilities.dataIO import ReadCompressedFiles, ReadH5File



def MeanAbsoluteError(prefix, scheme):
    # read in the original and decompressed data
    original_data = ReadH5File(prefix)
    decompressed_data = ReadCompressedFiles(prefix, scheme)

    mean_absolute_error = np.mean(abs(original_data - decompressed_data))

    print ('  Mean Absolute Error: {:0.2f}'.format(prefix, mean_absolute_error))
