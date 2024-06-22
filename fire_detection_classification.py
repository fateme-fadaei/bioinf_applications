import cv2
import glob
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from joblib import dump
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

def load_data():
    data_list = []
    labels = []
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


        if i%100 == 0:
            print("[INFO]{}/{} proccessed".format(i, 1000))

    data_list = np.array(data_list)
    # print(data_list.shape)

    x_train, x_test, y_train, y_test = train_test_split(data_list, label, test_size=0.2)
    # print(x_train.shape)
    return x_train, x_test, y_train, y_test

x_train, x_test, y_train, y_test = load_data()

clf = KNeighborsClassifier()
clf.fit(x_train, y_train)
dump(clf, "fire_detection.z")   #save model

y_pred = clf.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label="fire")
recall = recall_score(y_test, y_pred, pos_label="fire")
f_score = f1_score(y_test, y_pred, pos_label="fire")

print("Accuracy: {:.2f} ".format(accuracy*100))
print("Precision: {:.2f} ".format(precision*100))
print("Recall: {:.2f} ".format(recall*100))
print("F1-Score: {:.2f} ".format(f_score*100))