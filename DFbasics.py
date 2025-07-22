import pandas as pd
#creating dataframe using python dictionary and pandas DataFrame()
data={"Date":["22/07/2025","23/07/2025","24/07/2025","25/07/2025","26/07/2025","27/07/2025","28/07/2025","29/07/2025","30/07/2025","31/07/2025",],
      "Temperature":[25,30,34,26,23,38,22,34,32,23],"Weather":["windy","sunny","hot_sunny","windy","windy","hot_sunny","windy","hot_sunny","hot_sunny","windy"],
      "Humidity":[4,7,8,4.5,3,9,2.5,8,7.5,3]}
df=pd.DataFrame(data)
print("Created DF using DataFrame() = ",df)
print()
#DEALING ROWS AND COLUMNS
#df.shape
print("Shape of the created DF using df.shape = ",df.shape)
print()
#storing shape in variables
row,col=df.shape
print("Stored df.shape as row = ",row)
print("Stored df.shape as col = ",col)
print()
#head() for first few rows fetching default=5
print("head() method result = ",df.head())
print()
#head() for first few rows fetching specified rows
print("head() method with row specification result = ",df.head(3))
print()
#tail() for last few rows fetching default=5
print("tail() method result = ",df.tail())
print()
#tail() for last few rows fetching specified rows
print("tail() method with row specification result = ",df.tail(3))
print()
#slicing DF
print("Sliced Df = ",df[2:4])
print()
#df.columns for fetching column names
print("column names of df using df.columns = ",df.columns)
print()
#for fetching values of specified columns
print("Values of Temperature column = ",df.Temperature)
#or
print("values of Temperature column using [] operator = ",df["Temperature"])
print()
#type() for fetching data type
print("Data Type of Weather column = ",type(df["Weather"]))
print()
#OPERATIONS ON DF
#max(),min(),mean()
print("Max value of temperature using max() = ",df["Temperature"].max())
print("Min value of temperature using min() = ",df["Temperature"].min())
print("Mean value of temperature using mean() = ",df["Temperature"].mean())
print()
#describe() privides statistical summary of specified DF
print("Result of describe(): ",df.describe())
print()
#CONDITIONAL SELECTION
#Examples:
print("Temp values greater than 20 =",df[df["Temperature"]>20])
print("Dates where temp values are maximum = ",df[df["Temperature"]==df["Temperature"].max()]["Date"])
print()
#SETTING INDICES
#df.index() prints start and stop indices of DF
print("Start and Stop Indices of Df are = ",df.index)
print()
#to set a column as index valus = df.set_index(<column_name>) doesnot modifies original Df
df.set_index("Temperature")
print("DF with Temperature values as indices : ",df)
print()
#to modify original DF indices
df.set_index("Temperature",inplace=True)
#to reset index = df.reset_index(inplace=True)->hence modifies original DF also
df.reset_index(inplace=True)
print("Df with Reset index using reset_index = ",df)
print()
#for index based location use loc[<index value>]
print("Found value using loc[] = ",df.loc[2])





