import pandas as pd

def main():
    line = '-'*80
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'],
            'Math' : [85, 90, 78],
            'Science' : [92, 88, 80],
            'English' : [75, 85, 82]}
    
    df = pd.DataFrame(data)

    df['Gender'] = ['Male', 'Male', 'Female']
    print(line)
    print("Actual Dataframe :")
    print(df)
    print(line)

    print("After Grouping")
    df = df.groupby('Gender')[['Math', 'Science', 'English']].mean()
    print(df)
    print(line)


if __name__ == "__main__":
    main()