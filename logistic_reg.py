import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import zero_one_loss
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier


def load_data():
    dataset = pd.read_csv("./data/diabetes.csv")
    print(dataset.head())

    rows, cols = dataset.shape
    print("number of samples: {}, number of features: {}".format(rows,cols))

    #MISSING VALUE
    zero_not_accepted = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin'] #should not be zero
    for column in zero_not_accepted:
        dataset[column] = dataset[column].replace(0, np.nan)
        mean = int(dataset[column].mean(skipna=True))
        dataset[column] = dataset[column].replace(np.nan, mean)
    
    # print(dataset['Insulin'])

    data = dataset.iloc[:,:8]
    print(data.head())
 
    label = dataset.iloc[:,8]
    print(label.head())

    x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.2, random_state=42)
    # print(x_train.shape)
    # print(x_test.shape)
    # print(y_train.shape)
    # print(y_test.shape)

    #NORMALIZE
    sc_x = StandardScaler()
    # sc_x.fit(x_train)  #calcute mean and standard deviation
    # x_train = sc_x.transform(x_train)
    x_train = sc_x.fit_transform(x_train)
    x_test = sc_x.transform(x_test)

    return x_train, x_test, y_train, y_test


def training():
    # clf = LogisticRegression()

    clf = SGDClassifier(loss="log")
    clf.fit(x_train, y_train)  #Do Training

    # print(clf.coef_)
    # print(clf.intercept_)
    # print(clf.n_iter_)

    return clf


def results():
    y_pred = clf.predict(x_test)
    # print(y_pred)
    # print(y_test)
    # acc = accuracy_score(y_test, y_pred)
    # print("accuracy: {:.2f}".format(acc*100))


    acc = clf.score(x_test, y_test)
    print("accuracy in score:", acc)

    loss = zero_one_loss(y_test, y_pred)
    print("loss: {:.2f}".format(loss*100))

    prob = clf.predict_proba(x_test)
    print(prob)

x_train, x_test, y_train, y_test = load_data()
clf = training()
results()