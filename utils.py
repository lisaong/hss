import pandas as pd

def read_kinoeva(input_file):
    """
    Arguments:
    input_file - path to the text file
    
    Returns:
    A pandas dataframe containing the data
    """
    # df will have local scope
    df = pd.read_csv(input_file, delim_whitespace=True, index_col=0)
    
    # drop last column
    df.drop(columns=['export'], inplace=True)
    
    # replace column names
    df.columns = ['X', 'Y']

    # remove first row
    df.drop(['#T'], inplace=True)

    # convert data to numeric
    df = df.apply(pd.to_numeric, errors='coerce', axis=1)

    # rename index
    df.index.name = 'T'

    # save the original timestamp as another column
    df['Original_timestamp'] = df.index

    # time units are in h:mm:ss:hundredth
    df.index = pd.to_timedelta(df.index.str.replace(r'(0:.*):(\d+)', r'0\1.\2'), errors='coerce')

    return df