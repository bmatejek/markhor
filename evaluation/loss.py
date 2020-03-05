import math



import numpy as np



from markhor.utilities.dataIO import ReadCompressedFiles, ReadH5File



def ErrorMetrics(prefix, scheme, configurations):
    # read in the original data for this prefix
    original_data = ReadH5File(prefix)
    assert (original_data.dtype == np.uint8)

    # go through all of the configurations and produce the relevant error stats
    for parameters in configurations:
        # turn decompressed files into int16 for possible overflow issues
        # operations with this dataset will promote others to int16
        decompressed_data = ReadCompressedFiles(prefix, scheme, parameters).astype(np.int16)

        # get the mean absolute error and the mean squared error
        mean_absolute_error = np.mean(abs(original_data - decompressed_data))
        root_mean_squared_error = math.sqrt(np.mean((original_data - decompressed_data) ** 2))

        # calculate the peak signal-to-noise ratio
        max_l = 255
        PSNR = 20 * math.log10(max_l / root_mean_squared_error)

        print ('  Parameters:')
        for (key, value) in parameters.items():
            print ('    {}: {}'.format(key, value))
        print ('    Mean Absolute Error: {:0.2f}'.format(mean_absolute_error))
        print ('    Root Mean Squared Error: {:0.2f}'.format(root_mean_squared_error))
        print ('    Peak Signal-to-Noise Ratio: {:0.2f}'.format(PSNR))

        parameter_string = ''
        for (key, value) in parameters.items():
            parameter_string += '{}-{}'.format(key, value)

        output_filename = 'results/{}-{}-{}.txt'.format(prefix, scheme, parameter_string).lower()

        with open(output_filename, 'w') as fd:
            fd.write('Mean Absolute Error: {:0.6f}\n'.format(mean_absolute_error))
            fd.write('Root Mean Squared Error: {:0.6f}\n'.format(root_mean_squared_error))
            fd.write('Peak Signal-to-Noise Ratio: {:0.6f}\n'.format(PSNR))
