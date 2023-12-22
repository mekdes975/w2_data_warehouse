
import pandas as pd
class get_data:
    '''
    this class divide the whole csv data into two and extract them.
    '''
    # Define the path to your CSV file
    csv_path = '/home/hp/Downloads/20181024_d1_0830_0900(2).csv'
    def __init__(self) -> None:
        pass

    def get_data1(**kwargs):
        
        # Read the CSV file into a pandas DataFrame
        df= pd.read_csv('/home/hp/Downloads/20181024_d1_0830_0900(2).csv',index_col=False,delimiter = '; ')
        df1 = df.iloc[:, :4]
        
       
        return df1
    def get_data1(**kwargs):
        
        # Read the CSV file into a pandas DataFrame
        df= pd.read_csv('/home/hp/Downloads/20181024_d1_0830_0900(2).csv',index_col=False,delimiter = '; ')
        df2 = df.iloc[:, 5:]
        return df2
            
            
       