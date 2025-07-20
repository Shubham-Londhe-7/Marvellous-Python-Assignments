import pandas as pd
def main():
    data = {'Name' : ['A', 'B', 'C'],
            'Age' : [21.0, 22.0, 23.0]}
    
    df = pd.DataFrame(data)

    print("Dataype of 'Age' Column is :")
    print(df['Age'].dtype)

    df['Age'] = df['Age'].astype(int)
    print("Dataype of 'Age' Column after changing is :")
    print(df['Age'].dtype)

if __name__ == "__main__":
    main()