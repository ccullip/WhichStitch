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

def KerasModel(params, weights_filename):
    param_filename = params

    param_list = []
    with open(param_filename, 'r') as file:
        all_lines = file.readlines()
        for j in range(0, len(all_lines)):
            param_list.append(all_lines[j].rstrip('\n'))

    num_conv_filt1 = int(param_list[5])
    kernel_size1 = int(param_list[7])
    num_strides1 = int(param_list[9])
    activation = ""
    activation += str(param_list[11])
    num_conv_filt2 = int(param_list[13])
    kernel_size2 = int(param_list[15])
    num_strides2 = int(param_list[17])
    dense1 = int(param_list[19])
    dropout1 = float(param_list[21])
    dropout2 = float(param_list[23])

    model = Sequential()
    model.add(Conv2D(filters=num_conv_filt1, kernel_size=kernel_size1, strides=(num_strides1), data_format=data_format,
                     input_shape=(1, 100, 100)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), data_format=data_format))
    model.add(
        Conv2D(filters=num_conv_filt2, kernel_size=kernel_size2, strides=(num_strides2), data_format=data_format))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), data_format=data_format))
    model.add(Flatten())
    model.add(Dropout(dropout1))
    model.add(Dense(dense1))
    model.add(Activation('relu'))
    model.add(Dropout(dropout2))
    model.add(Dense(len(classes)))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    print("loaded weights")
    model.load_weights(weights_filename)
    model._make_predict_function()

    return model



def predict(model, img):
    print("predicting")
    model.predict(img)

def KerasModels(params, weights_filename, image):
    param_filename = params
    param_list = []
    with open(param_filename, 'r') as file:
        all_lines = file.readlines()
        for j in range(0, len(all_lines)):
            param_list.append(all_lines[j].rstrip('\n'))

    num_conv_filt1 = int(param_list[5])
    kernel_size1 = int(param_list[7])
    num_strides1 = int(param_list[9])
    activation = ""
    activation += str(param_list[11])
    num_conv_filt2 = int(param_list[13])
    kernel_size2 = int(param_list[15])
    num_strides2 = int(param_list[17])
    dense1 = int(param_list[19])
    dropout1 = float(param_list[21])
    dropout2 = float(param_list[23])

    model = Sequential()
    model.add(Conv2D(filters=num_conv_filt1, kernel_size=kernel_size1, strides=(num_strides1), data_format=data_format,
                     input_shape=(1, 100, 100)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), data_format=data_format))
    model.add(Conv2D(filters=num_conv_filt2, kernel_size=kernel_size2, strides=(num_strides2), data_format=data_format))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), data_format=data_format))
    model.add(Flatten())
    model.add(Dropout(dropout1))
    model.add(Dense(dense1))
    model.add(Activation('relu'))
    model.add(Dropout(dropout2))
    model.add(Dense(len(classes)))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    print("loading weights")
    model.load_weights(weights_filename)
    print("loaded weights")
    preds = model.predict(image)
    print(preds)
    return preds

def EntireModel(model_filename, img):
    print("creating model")
    model = load_model(model_filename)
    print("scaling img")
    img = normalize(img)
    print(img)
    print("predicting")
    preds = model.predict(img)
    index = np.argmax(preds)
    print(index)
    pred = classes[index]
    print(pred)
    return pred



