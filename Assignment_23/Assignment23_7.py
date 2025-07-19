import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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


    plt.figure(figsize=(8, 5))
    
    sns.barplot(x = 'Name', y = 'Total', data=df, palette='viridis')
    plt.title("Student name and Marks")
    plt.xlabel("Name of Student")
    plt.ylabel("Total Marks")

    plt.show()
    

if __name__ == "__main__":
    main()