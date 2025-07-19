import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    line = '-'*80
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'],
            'Math' : [85, 90, 78],
            'Science' : [92, 88, 80],
            'English' : [75, 85, 82]}
    
    df = pd.DataFrame(data)

    x = df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].iloc[0]

    plt.figure(figsize=(8, 6))
    plt.pie(x, labels=x.index)
    plt.title("Sagar's Marks")
    plt.show()

    

if __name__ == "__main__":
    main()