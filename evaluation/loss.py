import numpy as np



from markhor.utilities.dataIO import ReadCompressedFiles, ReadH5File



def MeanAbsoluteError(prefix, scheme, configurations):
    # read in the original and decompressed data
    original_data = ReadH5File(prefix)

    for parameters in configurations:
        # turn decompressed files into int16 for possible overflow issues
        # operations with this dataset will promote others to int16
        decompressed_data = ReadCompressedFiles(prefix, scheme, parameters).astype(np.int16)

        mean_absolute_error = np.mean(abs(original_data - decompressed_data))

        print ('  Parameters:')
        for (key, value) in parameters.items():
            print ('    {}: {}'.format(key, value))
        print ('    Mean Absolute Error: {:0.2f}'.format(mean_absolute_error))
