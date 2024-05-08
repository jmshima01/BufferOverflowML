import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import scipy.io
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical, plot_model, image_dataset_from_directory
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Dense, Flatten,Conv2D,MaxPooling2D,BatchNormalization,Activation,Dropout,InputLayer
from keras.optimizers import Adam
from keras.callbacks import LearningRateScheduler
from tensorflow import math as tfm
from scipy.io import savemat
from mat4py import loadmat

batch_size = 32
img_height = 256
img_width = 256


if __name__ == "__main__":
    data = ""
    train_ds = image_dataset_from_directory(data,validation_split=0.2,subset="training",seed=123,image_size=(img_height, img_width),batch_size=batch_size)
    
