import pandas as pd

def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'],
            'Math' : [85, 90, 78],
            'Science' : [92, 88, 80],
            'English' : [75, 85, 82]}
    
    df = pd.DataFrame(data)

    df['Gender'] = ['Male', 'Male', 'Female']       # Adding gender column
    print(df)

    df['Gender'] = df['Gender'].map({'Male' : 1, 'Female' : 0})     # one hot encoding using map function

    print("DataFrame after encoding Gender column :")
    print(df)


if __name__ == "__main__":
    main()