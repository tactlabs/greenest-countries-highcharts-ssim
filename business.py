import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')
    # df.drop(["Austria","Netherlands","Spain"], axis=1, inplace = True)

    df.drop(df.index[(df["Country"] == "Austria"),],axis=0,inplace=True)
    df.drop(df.index[(df["Country"] == "Netherlands") ],axis=0,inplace=True)
    df.drop(df.index[(df["Country"] == "Spain") ],axis=0,inplace=True)



    #print(df['states'].tolist())

    country                 = df['Country'].tolist()
    score                   = df['Score'].tolist()
   

    list_of_tuples = [tuple(row) for row in df.values]
  
    print(list_of_tuples)

    result_dict = {
        'Country'           : country,
        'Score'             :  score,
        
       
        # 'data_list'         : list_of_tuples
    }

    # print(result_dict)

    return result_dict


# def add_row(Lake, Area):

#     df = pd.read_csv('data.csv') 

#     new_row = {
    
#         'Lake'       : Lake, 
#         'Area'        : Area
#     }

#     print(df)

#     df = df.append(new_row, ignore_index=True)

#     print(df)

#     df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()