from keras import Sequential
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from keras.layers import Dense

df=pd.read_csv("aad.csv")

df.head()
df=df.replace({'yes':1,'no':0,'furnished':1,'semi-furnished':2,'unfurnished':3})
X=df.iloc[:,:11]
y=df.iloc[:,-1]
y.head()
me=Sequential()
X_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
me.add(Dense(16,input_dim=11,activation='relu'))
me.add(Dense(8,activation='relu'))
me.add(Dense(8,activation='relu'))
me.add(Dense(8,activation='relu'))

me.add(Dense(3,activation='softmax'))
me.compile(optimizer='adam',loss='mean_squared_error',metrics=['accuracy'])
me.fit(X_train,y_train,epochs=1000,batch_size=256)


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
rc=RandomForestClassifier()
rc.fit(X_train,y_train)
y_pred=rc.predict(x_test)
accuracy_score(y_test,y_pred)

from sklearn.svm import SVC

svm=SVC()
svm.fit(X_train,y_train)
svm.predict(x_test)
y_pred=svm.predict(x_test)
accuracy_score(y_test,y_pred)

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


digits = load_digits()
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target, test_size=0.2)
model.fit(X_train, y_train)
model.predict(digits.data[0:5])
model.score(X_test, y_test)


from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = ((y_pred - y_test) ** 2).mean()
print("Mean squared error:", mse)
