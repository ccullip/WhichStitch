from model.keras_model import KerasModel, KerasModels, EntireModel
from PIL import Image
import numpy as np
from io import BytesIO
import base64


def get_model_api():
    """Returns lambda function for api"""
    # 1. initialize model and reload weights
    model = KerasModel("model/params.txt", "model/weights.h5")

    def model_api(input_string):
        comma = input_string.find(',')
        input_data = input_string[comma + 1:]
        new_string = ""
        for i in range(len(input_data)):
            if input_data[i] == ' ':
                new_string += '+'
            else:
                new_string += input_data[i]
        #print(new_string)
        decoded_string = base64.b64decode(new_string)
        input_img = Image.open(BytesIO(decoded_string))
        img = np.array(input_img)
        convert_gray = [0.2989, 0.587, 0.114]
        img = np.dot(img[...,:3],convert_gray)
        print(img.shape)
        #img = np.swapaxes(img,0,2)
        #img = np.swapaxes(img,1,2)
        #img = img[0:3,:,:]
        img = np.expand_dims(img, axis=0)
        img = np.expand_dims(img, axis=0)
        print(img.shape)
        # 2. process input by resizing to 100 x 100 pixels
        #width = 100
        #height = 100
        #input_img = input_img.resize((width, height), Image.ANTIALIAS)
        # make image greyscale

        #print(img.shape)
        # 3. call model predict function
        print('predicting')
        preds = EntireModel("model/model.h5", img)
        preds = KerasModels("model/params.txt", "model/weights.h5", img)
        print(preds)
        # 4. process the output
        # 5. return the output for the api
        return preds

    return model_api