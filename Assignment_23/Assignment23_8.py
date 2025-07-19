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

    amit_row = df[df['Name'] == 'Amit']

    # Convert to long format: Subjects + Marks
    amit_melt = amit_row.melt(id_vars=['Name'],
                              value_vars=['Math', 'Science', 'English'],
                              var_name='Subject',
                              value_name='Marks')

    print(amit_melt)



    sns.set(style='whitegrid')
    plt.figure(figsize=(6, 4))

    sns.lineplot(x='Subject', y='Marks', data=amit_melt, marker='o', color='blue')

    plt.title("Amit's Marks Across Subjects")
    plt.xlabel('Subject')
    plt.ylabel('Marks')

    plt.show()
    

if __name__ == "__main__":
    main()