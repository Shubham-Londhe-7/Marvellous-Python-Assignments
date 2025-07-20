import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    data = {'Age' : [25, 30, 45, 35, 22],
            'Salary' : [50000, 60000, 80000, 65000, 45000],
            'Purchased' : [1, 0, 1, 0, 1]}
    
    df = pd.DataFrame(data)
    print(df) 

    x = df[['Age','Salary']]
    y = df['Purchased']

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.2, random_state=42)

    print("Dimensions of Training dataset : ",x_train.shape)
    print("Dimensions of Testing dataset : ",x_test.shape)


if __name__ == "__main__":
    main()