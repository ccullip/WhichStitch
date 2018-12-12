import numpy as np
from keras.models import Sequential, load_model, model_from_json, save_model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.activations import softmax

# dimensions of the images.
img_width, img_height = 100, 100

# classes
classes = ['garter', 'stockinette', 'seed', 'slipstitchhoneycomb', 'star']

data_format = 'channels_first'

#RGB to gray
convert_gray = [0.2989, 0.587, 0.114]

def normalize(image):
    image = np.asarray(image, dtype='float32')
    image = image/255
    return image

def predict(model, img):
    print("predicting")
    model.predict(img)

def EntireModel(model_filename, img):
    # create model
    model = load_model(model_filename)

    # normalize image
    img = normalize(img)

    # get predictions
    preds = model.predict(img)

    # get top prediction
    index = np.argmax(preds)
    pred = classes[index]

    # get second prediction
    preds2 = np.delete(preds, index)
    classes2 = np.delete(classes, index)
    index2 = np.argmax(preds2)
    pred2 = classes2[index2]

    return pred, pred2



