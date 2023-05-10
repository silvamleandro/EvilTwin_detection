# Imports
import os
import pandas as pd



# Functions
def txt_to_list(file_path):
    # Open the .txt file
    txt_file = open(file_path, "r")
    # Read the file
    data = txt_file.read()
    # Replace end split the text when newline ('\n') is seen
    data_into_list = data.split("\n")
    # Close the file
    txt_file.close()
    # Return file lines in list
    return data_into_list



def read_data(datasets_path, useful_features):
    frames = [] # DataFrames list

    for filename in sorted(os.listdir(datasets_path)):
        df = pd.read_csv(datasets_path + filename, usecols=useful_features) # Read .csv
        frames.append(df) # Add DataFrame to list

    # Return concatenated DataFrames
    return pd.concat(frames)



def split_X_y(df): 
    # DataFrame X (features)
    X = df.loc[:, df.columns != 'Label']
    y = df.loc[:, 'Label'] # y (labels)
    # DataFrame X and y
    return X, y
