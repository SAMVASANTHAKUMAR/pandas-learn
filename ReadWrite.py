import pandas as pd
#READING CSV
#read_csv() for reading csv files 
#parameters: skiprows/header-for skipping rows,nrows=row specification,na_values=replacing null values
df1=pd.read_csv(r"C:\Users\samva\OneDrive\Documents\GIT practice\pandasweatherdata.csv")
print("DF by read_csv():",df1)
print()
#skiprows
df2=pd.read_csv(r"C:\Users\samva\OneDrive\Documents\GIT practice\pandasweatherdata.csv",skiprows=3)
print("DF by read_csv(skiprows):",df2)
print()
#nrows
df3=pd.read_csv(r"C:\Users\samva\OneDrive\Documents\GIT practice\pandasweatherdata.csv",nrows=5)
print("DF by read_csv(n_rows):",df3)
print()
#na_values
df4=pd.read_csv(r"C:\Users\samva\OneDrive\Documents\GIT practice\pandasweatherdata.csv",na_values=["NaN",0])
print("DF by read_csv(na_values without column specification):",df4)
print()
#na_rows with column specification
df5=pd.read_csv(r"C:\Users\samva\OneDrive\Documents\GIT practice\pandasweatherdata.csv",na_values={
    "Temperature":["NaN","0"],"Weather":["NaN","NO Event"]})
print("DF by read_csv(na_values with column specification):",df5)
print()