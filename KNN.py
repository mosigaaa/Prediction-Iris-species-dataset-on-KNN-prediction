import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

Iris = pd.read_csv("Iris.csv")

X = Iris.drop(columns=["Species","Id"])
y = Iris["Species"]

sns.pairplot(Iris, hue='Species')
plt.show()


SS = StandardScaler()
X= SS.fit_transform(X)

X_train , X_test, y_train , y_test = train_test_split(X,y,test_size=0.3,random_state=5)



def knn_func(X_trains,label_data,test_data,k):
    KNN = KNeighborsClassifier(n_neighbors=k)
    KNN.fit(X_trains,label_data)
    Predict_data = KNN.predict(test_data)

    return  Predict_data


normal_accuracy = []
k_value = range(1,24)
for k in k_value :
    y_predict = knn_func(X_train,y_train,X_test,k)
    accur = accuracy_score(y_test, y_predict)
    normal_accuracy.append(accur)
plt.plot(k_value,normal_accuracy,c="grey",marker=".",ms=7,mfc="black",mec="black")
plt.xlabel("K")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()


#Best K is 6
