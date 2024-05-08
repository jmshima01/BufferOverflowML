from keras.utils import image_dataset_from_directory
from keras.models import Sequential
from keras.layers import Dense, Flatten,Conv2D,MaxPooling2D,BatchNormalization,Activation,Dropout,Softmax
from keras.optimizers import Adam
from keras.callbacks import LearningRateScheduler
from tensorflow import math as tfm
from matplotlib import pyplot as plt
img_height = 256
img_width = 256
batch_size = 8

if __name__ == "__main__":
    data = "images"
    train_ds = image_dataset_from_directory(data,validation_split=0.2,subset="training",seed=123,image_size=(img_height, img_width),batch_size=batch_size)
    validation_ds = image_dataset_from_directory(data,validation_split=0.2,subset="validation",seed=123,image_size=(img_height, img_width),batch_size=batch_size)
    
    # print(train_ds.class_names)
    
    
    CNN = Sequential()
    CNN.add(Conv2D(16, (3,3), padding='same', input_shape=(img_height,img_width,3)))
    CNN.add(BatchNormalization())
    CNN.add(Activation('relu'))
    CNN.add(MaxPooling2D((2,2)))
    CNN.add(Conv2D(32, (3,3), padding='same'))
    CNN.add(BatchNormalization())
    CNN.add(Activation('relu'))
    CNN.add(MaxPooling2D((2,2)))
    CNN.add(Conv2D(32, (3,3), padding='same'))
    CNN.add(BatchNormalization())
    CNN.add(Activation('relu'))
    CNN.add(MaxPooling2D((2,2)))
    CNN.add(Conv2D(64, (3,3), padding='same'))
    CNN.add(BatchNormalization())
    CNN.add(Activation('relu'))
    CNN.add(MaxPooling2D((2,2)))
    CNN.add(Conv2D(32, (3,3), padding='same'))
    CNN.add(BatchNormalization())
    CNN.add(Activation('relu'))
    CNN.add(MaxPooling2D((2,2)))
    CNN.add(Conv2D(32, (3,3), padding='same'))
    CNN.add(BatchNormalization())
    CNN.add(Activation('relu'))
    CNN.add(MaxPooling2D((2,2)))
    CNN.add(Flatten())
    CNN.add(Dense(64, activation='relu'))
    CNN.add(Dropout(0.5))
    CNN.add(Dense(len(train_ds.class_names), name="outputs"))
    CNN.add(Softmax())


    CNN.compile(loss="sparse_categorical_crossentropy", optimizer=Adam(learning_rate = 1e-3), metrics=['accuracy'])
    CNN.summary()    
    history = CNN.fit(train_ds, epochs=10, batch_size=batch_size, validation_data=validation_ds)
    
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']
    
    print()
    print(acc)
    print(loss)
    