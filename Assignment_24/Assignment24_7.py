import pandas as pd
import numpy as np

def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'],
            'Math' : [85, 90, 78],
            'Science' : [92, 88, 80],
            'English' : [75, 85, 82]}
    
    df = pd.DataFrame(data)

    Total = {'Total': [0] * len(df['Name'])}      # empty list of size as per student name

    for i in range(len(data['Name'])):              # dictionary travel with list as a value
        Total['Total'][i] = int(df['Math'][i]) + int(data['Science'][i]) + int(data['English'][i]) 

    df['Total'] = Total['Total']                    # adding Toatl column in original dataframe (data)

    print(df)

    Status = {'Status' : [0] * len(df['Name'])}

    for i in range(len(data['Name'])):
        if(df['Total'][i] >= 250):
            Status['Status'][i] = 'Pass'
        else:
            Status['Status'][i] = 'Fail'

    df['Status'] = Status['Status']
    print(df)

    df.to_csv('Student.csv')

if __name__ == "__main__":
    main()