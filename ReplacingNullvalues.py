import pandas as pd
import numpy as np
data = {
    "PatientID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", None, "David", "Eva"],
    "Temperature": ["98.6F", "37C", None, "36.5C", "99F"],
    "HeartRate": ["72bpm", None, "80bpm", "76", "75bpm"],
    "Diagnosis": ["Flu", "Covid", None, "Malaria", "Dengue"],
    "OxygenLevel": [None, "95%", "92%", None, "98%"]
}

df = pd.DataFrame(data)
print(df)
print()
dfrep=df.replace({None:np.nan})
print("DF after Replace(): ",dfrep)
#column specific replacement
dfrepcol=df.replace({"Name":{None:np.nan},
                     "Temperature":{None:0},
                     "HeartRate":{None:"Normal"},
                     "Diagnosis":{None:"Recovered"},
                     "OxygenLevel":{None:"80%"}})
print("DF after replace(column_specified) : ",dfrepcol)
print()
#similar to the above, we ca make value specific replacements

#REGEX - REGULAR EXPRESSION
#regex=True can be given and replaced with only numeric values instead of alphanumerics
dfrepregex=df.replace("[A-Z,a-z,%,]","",regex=True)
print("DF after REGEX removal: ",dfrepregex)
print()
#For column specific REGEX replacements use a dictionary 
#replace({"column1":regex_value,"column2":"regex_value"...},"",regex=True)
#apply the above for column specified regex removal