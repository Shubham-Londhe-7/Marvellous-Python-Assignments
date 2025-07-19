import pandas as pd

def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'],
            'Math' : [85, 90, 78],
            'Science' : [92, 88, 80],
            'English' : [75, 85, 82]}
    
    df = pd.DataFrame(data)

    Total = {'Total': [0] * len(data['Name'])}      

    for i in range(len(df['Name'])):             
        Total['Total'][i] = int(df['Math'][i]) + int(df['Science'][i]) + int(df['English'][i]) 

    df['Total'] = Total['Total'] 
    print("Original Dataframe :")
    print(df)                   

    df = df.sort_values(by='Total' , ascending=False)
    print("Sorted Dataframe by Total in Decending order :")
    print(df)
    

if __name__ == "__main__":
    main()