import pandas as pd
def main():
    data = {'City' : ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
    
    df = pd.DataFrame(data)

    # df['City'] = df['City'].map({'Pune' : 0, 'Mumbai' : 1, 'Delhi' : 2})        #  encoding using map
    df['City'] = df['City'].astype('category').cat.codes        # using inbuilt function of pandas

    print(df) 

if __name__ == "__main__":
    main()