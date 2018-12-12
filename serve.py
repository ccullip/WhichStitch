from model.keras_model import KerasModel, KerasModels, EntireModel
from PIL import Image
import numpy as np
from io import BytesIO
import base64


def get_model_api():
    """Returns lambda function for api"""
    # 1. initialize model and reload weights
    #model = KerasModel("model/params.txt", "model/weights.h5")

    def model_api(input_string):
        comma = input_string.find(',')
        input_data = input_string[comma + 1:]
        print(input_data)
        #new_string = ""
        #for i in range(len(input_data)):
        #    if input_data[i] == ' ':
        #        new_string += '+'
        #    else:
        #        new_string += input_data[i]
        #print(new_string)
        decoded_string = base64.b64decode(input_data)
        input_img = Image.open(BytesIO(decoded_string))
        print(input_img.size)

        greyscale = input_img.convert('L')
        greyscale.save("greyscale.jpg")
        print(greyscale.size)

        # create numpy array and convert to greyscale
        img = np.array(greyscale)
        print(img.shape)

        # crop image to 100 x 100 square
        img = img[0:100, 0:100]
        print(img.shape)
        print(img)

        img = np.expand_dims(img, axis=0)
        img = np.expand_dims(img, axis=0)
        print(img.shape)

        # 3. call model predict function
        pred1, pred2 = EntireModel("model/12_11_2018-model.h5", img)

        # 5. return the output for the api
        return pred1, pred2

    return model_api