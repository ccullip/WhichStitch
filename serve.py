from model.keras_model import EntireModel
from PIL import Image
import numpy as np
from io import BytesIO
import base64


def get_model_api():
    """Returns lambda function for api"""
    # 1. initialize model and reload weights
    #model = KerasModel("model/params.txt", "model/weights.h5")

    def model_api(input_string):
        # remove extraneous beginning padding
        comma = input_string.find(',')
        input_data = input_string[comma + 1:]

        # decode base64 data
        decoded_string = base64.b64decode(input_data)
        input_img = Image.open(BytesIO(decoded_string))

        # convert to greyscale
        greyscale = input_img.convert('L')

        # convert to numpy array
        img = np.array(greyscale)

        # crop image to 100 x 100 square
        img = img[0:100, 0:100]

        img = np.expand_dims(img, axis=0)
        img = np.expand_dims(img, axis=0)

        # call model predict function
        pred1, pred2 = EntireModel("model/12_11_2018-model.h5", img)

        # return the output for the api
        return pred1, pred2

    return model_api