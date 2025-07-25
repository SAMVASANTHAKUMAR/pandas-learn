import pandas as pd
df=pd.read_csv(r"C:\Users\samva\OneDrive\Documents\GIT practice\pandaspatientdatawithnull.txt")
print(df)
print()
#FILLING NULL VALUES 
#df.fillna(value) for filling all null values with desired value
dffill=df.fillna(0)
print("DF after fillna(0) : ",dffill)
print()
#fillna with column specific values
dffillcol=df.fillna({"Name":"not_available","Age":18,"BloodGroup":"O+","Diagnosis":"Flu"})
print("DF after fillna(column_specified) : ",dffillcol)
print()
#parameters of fillna: method="ffill"/"bfill",axis="columns"
#method="ffill" for forward filling
dffillforward=df.fillna(method="ffill")
print("DF after fillna(forward) : ",dffillforward)
print()
#fillna with no of null values allowed to be filled with that value
dffillforward=df.fillna(method="ffill",limit=1)
print("DF after fillna(forward with limit) : ",dffillforward)
print()
#method="bfill for backward filling"
dffillbackward=df.fillna(method="bfill")
print("DF after fillna(backward) : ",dffillbackward)
print()
#axis="columns" for horizontal filling
dffillhori=df.fillna(method="ffill",axis="columns")
print("DF after fillna(horizontally with columns) : ",dffillhori)
print()

#INTERPOLATION
#interpolate() for interpolated value filling at numerical column null values
dfip=df.interpolate()
print("DF with Interpolate() :",dfip)
print()

#DROPPING NULL VALUES
#df.dropna() for dropping null values containing rows
dfdrop=df.dropna()
print("DF after dropna(): ",dfdrop)
print()
#how=all -  to drop rows with full of null values
dfdrophow=df.dropna(how='all')
print("DF after dropna(how=all): ",dfdrophow)
print()
#dropna with thresh - for dropping rows without minimum number of valid values
dfdropthresh=df.dropna(thresh=5)
print("DF after dropna(thresh): ",dfdropthresh)