import pandas as pd
#DF 1
data={"Date":["22/07/2025","23/07/2025","24/07/2025","25/07/2025","26/07/2025","27/07/2025","28/07/2025","29/07/2025","30/07/2025","31/07/2025",],
      "Temperature":[25,30,34,26,23,38,22,34,32,23],"Weather":["windy","sunny","hot_sunny","windy","windy","hot_sunny","windy","hot_sunny","hot_sunny","windy"],
      "Humidity":[4,7,8,4.5,3,9,2.5,8,7.5,3.5]}
df1=pd.DataFrame(data)
#DF 2
data2={"name":["varun","vishnu","roy","ram"],
       "English":[90,85,75,65],
       "Tamil":[65,75,85,95],
       "Maths":[78,87,67,87],
       "Physics":[46,56,77,66],
       "Chemistry":[66,77,88,99],
       "CS":[97,96,95,94]}
df2=pd.DataFrame(data2)
#CONCATENATING DF using pd.concat() - index will be same for dfs as before
# Note: df1 and df2 have different shapes and column names.
# So vertical concat will result in NaNs where data doesn't exist.
# And horizontal concat (axis=1) will align rows by index — NaNs may appear if lengths differ.

condf=pd.concat([df1,df2])
print("Concatenated DF using concat([df1,df2]) = ",condf)
#To change index into continuous index - use ignore_index=True
condfigin=pd.concat([df1,df2],ignore_index=True)
print("Concatenated DF using concat([df1,df2],ignore_index) = ",condfigin)
#for naming each DF after conctenating - use keys=['','']
condfkeys=pd.concat([df1,df2],keys=["weather_DF","Score_DF"])
print("Concatenated DF using concat([df1,df2],keys=[]) = ",condfkeys)
#concatenating sidewise - use axis=1
condfside=pd.concat([df1,df2],axis=1)
print("Concatenated DF using concat([df1,df2],axis=1) = ",condfside)




