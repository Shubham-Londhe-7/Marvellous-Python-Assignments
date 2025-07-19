import pandas as pd


def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'],
            'Math' : [85, 90, 78],
            'Science' : [92, 88, 80],
            'English' : [75, 85, 82]}
    
    df = pd.DataFrame(data)

    df = df.drop('English', axis=1)  # axis=1 means drop a column (axis=0 is for rows)

    print("DataFrame after dropping 'English' column:")
    print(df)
    

if __name__ == "__main__":
    main()