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

#WRITING CSV
#to_csv() for writing csv
#parameters: index,header
data={"Date":["22/07/2025","23/07/2025","24/07/2025","25/07/2025","26/07/2025","27/07/2025","28/07/2025","29/07/2025","30/07/2025","31/07/2025",],
      "Temperature":[25,30,34,26,23,38,22,34,32,23],"Weather":["windy","sunny","hot_sunny","windy","windy","hot_sunny","windy","hot_sunny","hot_sunny","windy"],
      "Humidity":[4,7,8,4.5,3,9,2.5,8,7.5,3.5]}
dfforwrite=pd.DataFrame(data)
print(dfforwrite)
dfforwrite.to_csv("WrittenCSVwithDF.csv")
print("Wrote CSV")
#index=False for not writting indices
dfforwrite.to_csv("WrittenCSVwithDF.csv",index=False)
print("Wrote CSV with index=False")
#header=False for skipping column names from writing
dfforwrite.to_csv("WrittenCSVwithDF.csv",header=False,index=False)
print("Wrote CSV with header=False")
#columns=["",""] for writing oly specific columns
dfforwrite.to_csv("WrittenCSVwithDF.csv",columns=["Temperature","Weather"],index=False)
print("Wrote CSV with columns=[]")

#---------------------------------------------------------------------------------------------------------

#READING EXCEL
#read_excel() for reading excel files
dfexcel=pd.read_excel("C:/Users/samva/OneDrive/Documents/GIT practice/pandasmarkdata.xlsx","Sheet1")
print("DF by read_excel():",dfexcel)
print()
#to fill null values in specific columns of excel file
def convert(cell):
    if cell == "null":
        return "the cell is null"
    return cell
dfexcelnull=pd.read_excel("C:/Users/samva/OneDrive/Documents/GIT practice/pandasmarkdata.xlsx","Sheet1",converters={
    "Temperature":convert})
print(dfexcelnull)

#WRITING EXCEL
#to_excel() for writing
data={"Date":["22/07/2025","23/07/2025","24/07/2025","25/07/2025","26/07/2025","27/07/2025","28/07/2025","29/07/2025","30/07/2025","31/07/2025",],
      "Temperature":[25,30,34,26,23,38,22,34,32,23],"Weather":["windy","sunny","hot_sunny","windy","windy","hot_sunny","windy","hot_sunny","hot_sunny","windy"],
      "Humidity":[4,7,8,4.5,3,9,2.5,8,7.5,3]}
dfforwriteexcel=pd.DataFrame(data)
dfforwriteexcel.to_excel("WrittenExcelwithDF.xlsx",sheet_name="FirstDF")

#WRITING TWO different DFs in SINGLE EXCEL file with TWO SHEET names
data2={"name":["varun","vishnu","roy","ram"],
       "English":[90,85,75,65],
       "Tamil":[65,75,85,95],
       "Maths":[78,87,67,87],
       "Physics":[46,56,77,66],
       "Chemistry":[66,77,88,99],
       "CS":[97,96,95,94]}
df2forwriteexcel=pd.DataFrame(data2)
with pd.ExcelWriter("ExcelwithTwoDFs.xlsx")as writer:
    df2forwriteexcel.to_excel(writer,sheet_name="MARKS_DF")
    dfforwriteexcel.to_excel(writer,sheet_name="WEATHER_DF")









