### This is meant for analysis of the Badminton Data
# import packages
import pandas as pd



# import data
bad_dir = r"C:\Users\liudv\Projects\BadmintonStats\Badminton_data.xlsx"
badminton_data = pd.read_excel(bad_dir)

# basic structure
badminton_data.head()          # first 5 rows
badminton_data.tail()          # last 5 rows
badminton_data.info()          # data types, null counts
badminton_data.describe()      # numeric summary stats
#badminton_data.describe(include='object') 

