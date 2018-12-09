#Stock price prediction

import csv
import numpy 
from sklearn.svm import SVR
import matplotlib.pyplot as plt

date = []
price = []

def Predict(date,price,p):
    date = numpy.reshape(date,(len(date),1))
    svrL = SVR(kernel='linear',C=1e3)
    svrP = SVR(kernel='poly', C=1e3, degree=2)
    svrR = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svrL.fit(date, price)
    svrP.fit(date,price)
    svrR.fit(date, price)

    plt.scatter(date, price, color='blue', label='Data')
    plt.plot(date, svrR.predict(date), color='green', label='RBF model')
    plt.plot(date, svrL.predict(date), color='red', label='Linear model')
    plt.plot(date, svrP.predict(date), color='black', label='Polynomial model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('support vector regression')
    plt.legend()
    plt.show()

    return svrR.predict(p)[0],svrL.predict(p)[0],svrP.predict(p)[0]

def Getdata(file):
    with open(file,'r') as csvfile:
        readcsv = csv.reader(csvfile)
        next(readcsv)
        for row in readcsv:
            date.append(int(row[0].split('-')[0]))
            price.append(float(row[1]))

#Getdata(filename.csv)
#predictprice = predict(date,price,num)
#print(predictprice)



