import cv2
import glob
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder 
from tensorflow.keras

def load_data():
    data_list = []
    labels = []

    le = LabelEncoder()
    for i, address in enumerate(glob.glob(".\data\\fire_dataset\\*\\*")):
        # print(address)
        img = cv2.imread(address)
        # print(img.shape)
        img = cv2.resize(img, (32, 32))
        # print(img.shape)
        img = img/255.0
        img = img.flatten()
        # print(img)
        # print(img.shape)
        data_list.append(img)

        # label = address.split("\\")[1]
        label = address.split("\\")[-1].split(".")[0]
        # print(label)
        labels.append(label)


        # if i % 100 == 0:
        #     print("[INFO]{}/{} proccessed".format(i, 1000))
        #     # print(f"[INFO] {i}/1000 processed")

        if i == 10:
            break 

    data_list = np.array(data_list)
    # print(data_list.shape)

    x_train, x_test, y_train, y_test = train_test_split(data_list, label, test_size=0.2)
    # print(x_train.shape)

    y_train = le.fit_transform(y_train)
    y_test = le.transform(y_test)  #go to integer space

    print(y_train[5])
    return x_train, x_test, y_train, y_test

x_train, x_test, y_train, y_test = load_data()