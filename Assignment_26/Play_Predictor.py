import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


def PlayPredictorLogistic(Datapath):
    line = '-'*80
    df = pd.read_csv(Datapath)
    print(line)
    print("First few data :")
    print(line)
    print(df.head())

    print(line)
    print("Description of dataset :")
    print(line)
    print(df.describe ())

    # Dropping unnecessary columns (data cleaning)
    df.drop(columns=['Unnamed: 0'], inplace=True)

    le = LabelEncoder()
    for i in df.columns:
        df[i] = le.fit_transform(df[i])

    print(line)
    print("Dataset after Encoding")
    print(line)
    print(df.head())
    
    # visualisation
    plt.figure(figsize=(10,5))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Play Predictor')
    plt.show()

    # independent variable
    x = df.drop(columns=['Play'], axis=1)

    # dependent variable
    y = df['Play']

    print(line)
    print("Dimensions of Dependent Variable :")
    print(x.shape)
    print("Dimensions of Independent Variable :")
    print(y.shape)
    print(line)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Bulding model
    model = LogisticRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print("Model Build Successful")
    print(line)

    # Calculating Accuracy
    accuracy = accuracy_score(y_pred, y_test)
    ConfM = confusion_matrix(y_pred, y_test)

    print("Accuracy Of Model : ",accuracy*100)
    print(line)

    print("Confusion Matrix : ")
    print(ConfM)
    print(line)

    

def main():
    PlayPredictorLogistic('PlayPredictor.csv')

if __name__ == '__main__':
    main()