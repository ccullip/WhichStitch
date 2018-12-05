from model.keras_model import KerasModel
from PIL import Image
import numpy as np


def get_model_api():
    """Returns lambda function for api"""
    # 1. initialize model and reload weights
    model = KerasModel("model/params.txt")
    model.load_weights("model/weights.h5")

    def model_api(input_img):
        # 2. process input by resizing to 100 x 100 pixels
        width = 100
        height = 100
        #input_img = input_img.resize((width, height), Image.ANTIALIAS)
        # 3. call model predict function
        img = np.array(input_img)
        preds = model.predict(img)
        # 4. process the output
        # 5. return the output for the api
        return preds

    return model_api