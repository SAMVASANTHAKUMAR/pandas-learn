import pandas as pd
#read_csv() for reading csv files into code
df1=pd.read_csv(r"C:\Users\samva\OneDrive\Documents\GIT practice\pandasweatherdata.csv")
print("DF by read_csv():",df1)
print()
#read_excel() for reading excel files into code
df2=pd.read_excel("C:/Users/samva/OneDrive/Documents/GIT practice/pandasmarkdata.xlsx","Sheet1")
print("DF by read_excel():",df2)
print()
#using dictionary = pd.DataFrame()
data={"Date":["22/07/2025","23/07/2025","24/07/2025","25/07/2025","26/07/2025","27/07/2025","28/07/2025","29/07/2025","30/07/2025","31/07/2025",],
      "Temperature":[25,30,34,26,23,38,22,34,32,23],"Weather":["windy","sunny","hot_sunny","windy","windy","hot_sunny","windy","hot_sunny","hot_sunny","windy"],
      "Humidity":[4,7,8,4.5,3,9,2.5,8,7.5,3]}
df3=pd.DataFrame(data)
print("Created DF using DataFrame() = ",df3)
print()
#using list of tuples
datan=[("1/2/2025",35,60,"sunny"),
       ("2/2/2025",30,50,"sunny"),
       ("3/2/2025",25,40,"windy")]
df4=pd.DataFrame(datan,columns=["Date","temperature","humidity","weather"])
print("DF using list of tuples:",df4)
