import pandas as pd

def clean_currency(x):
    """ If the value is a string, then remove currency symbol and delimiters
    otherwise, the value is numeric and can be converted
    """
    if isinstance(x, str):
        return(x.replace('€', '').replace(',', ''))
    return(x)



def preprocess(data_path,clean_currency):
    """The function main at preprocesssing the data"""
    data= pd.read_csv (data_path, header= 1)
    data.drop_duplicates()
    data = data[data['Area'].str.contains('m²')]                                     # this check if the data contain "m2"
    data['Area'] = data['Area'].str.split('|', n=1, expand=False)                    # this split the data by "|" into list (0, 1)


    data['Area']=data.Area.apply(lambda x: x[0] if len(x) ==1 else x[1])            # This checked if the data len is 1, then X= x[0] else x[1]
    data['Area'] = data['Area'].str.extract(r'(\d+)') 

    data['Number_of_Rooms'] = data['Number_of_Rooms'].str.extract(r'(\d+)')         # using regrex (regular expressions)
    data['Garden surface'] = data['Garden surface'].str.extract(r'(\d+)')
    
    # cleaning currency
    data['Price'] = data['Price'].apply(clean_currency).astype('float')
    
    #converting categorical variable to dummy variable 
    data['Furnished_encoded'] =data['Furnished'].map({'No': 0, 'Yes': 1})         
    data['Swimming Pool_encoded'] =data['Swimming Pool'].map({'No': 0, 'Yes': 1})
    
    #drop some price and Number of room less than some range
    data.drop(data.index[data['Price'] < 40000.0], inplace=True)
    data.drop(data.index[data['Number_of_Rooms'] < "10"], inplace=True)
    
    #Delete column 
    data.drop(['Furnished', 'Swimming Pool'], axis=1, inplace=True)

    #Rename a column
    dict = {'Swimming Pool_encoded': 'Swimming Pool','Furnished_encoded': 'Furnished'}

    # call rename () method
    data.rename(columns=dict, inplace=True)  

    # removing extra column that is not needed for the model 

    data.drop(['Title', 'Location',"Status", "Kitchen type", "Furnished","Swimming Pool"], axis=1, inplace=True)

    data.to_csv("cleandata.csv")



data_path = r"Becode\Data\data2.csv"

preprocess(data_path,clean_currency)
