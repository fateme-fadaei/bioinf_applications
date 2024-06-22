import pandas as pd
# from sklearn.dataset import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import zero_one_loss 

def load_data():

    # iris = load_iris()
    # # print(iris)
    # # print(iris.data)
    # # print(iris.target) #label
    # # print(iris.target_name) 
    # features = iris.data
    # labels = iris.target

    dataset = pd.read_csv("./data/iris.data", header=None, 
                          names=["sepal length", "sepal width", "petal length", "petal width", "label"])
    print(dataset.head())

    rows, cols = dataset.shape
    print("number of samples: {}, number of features: {}".format(rows,cols))

    data = dataset.iloc[:,:4]
    print(data.head())

    label = dataset.iloc[:,4]
    print(label.head())

    x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.2, random_state=42)
    # print(x_train.shape)
    # print(x_test.shape)
    # print(y_train.shape)
    # print(y_test.shape)

    return x_train, x_test, y_train, y_test

def training():
    clf = KNeighborsClassifier(n_neighbors=5)
    clf.fit(x_train, y_train)  #Do Training -> save data
    return clf

def results():
    y_pred = clf.predict(x_test)
    # print(y_pred)
    # print(y_test)
    acc = accuracy_score(y_test, y_pred)
    print("accuracy: {:.2f}".format(acc*100))

    loss = zero_one_loss(y_test, y_pred)
    print("loss: {:.2f}".format(loss*100))

x_train, x_test, y_train, y_test = load_data()
clf = training()
results()

