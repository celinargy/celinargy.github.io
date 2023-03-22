import glob
import pandas as pd
import numpy as np

# r creates a raw path
# glob library to create list of paths for xls files
# CHANGE PATH HERE
path = (r"C:\Users\argyropoulos_c\Documents\GitHub\celinargy.github.io\notebooks\data")
file_list = glob.glob(path + "/*.xls")

# Create an empty list
excl_list = []
 
# iteratre through file_list to read xls and create DF 
for file in file_list:
    excl_list.append(pd.read_excel(file))

# merge DF using append but better using concat 
excl_merged = pd.DataFrame()

for excl_file in excl_list:
    excl_merged = excl_merged.append(
    excl_file, ignore_index=True)

#CHANGE NAME HERE
excl_merged.to_excel('total_recs.xlsx', index=False)