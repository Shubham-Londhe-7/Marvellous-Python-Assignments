import pandas as pd

def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'],
            'Math' : [85, 90, 78],
            'Science' : [92, 88, 80],
            'English' : [75, 85, 82]}

    df = pd.DataFrame(data  )

    print("Students who scored more than 85 in science :")
    for i in range(len(data['Name'])):
        if(data['Science'][i] > 85):
            print(data['Name'][i], " : ", data['Science'][i])

if __name__ == "__main__":
    main()