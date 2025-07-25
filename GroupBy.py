import pandas as pd
#groupby() for split aplly combine process
employee_data = {
    "Employee": ["Arun", "Bharathi", "Chozhan", "Dally", "Elisa", "Fareena", "Goliath", "Honeyka"],
    "Department": ["HR", "Tech", "Tech", "HR", "Marketing", "Marketing", "Tech", "HR"],
    "Gender": ["M", "M", "M", "F", "F", "F", "M", "F"],
    "Salary": [40000, 55000, 60000, 42000, 48000, 50000, 62000, 41000]
}
df= pd.DataFrame(employee_data)
print(df)
#Splitting
dfg=df.groupby("Gender")
#usually grouped dfs are abstracted, for viewing them - use for loop
for x in dfg:
    print(x)
#get_group - for specific group displaying
dfgg=dfg.get_group("F")
print("DF of get_group(F):",dfgg)
print()
# Applying and Combining : get rows with max salary in each Gender group
dfga = df.loc[dfg["Salary"].idxmax()][["Employee", "Salary"]]
print(dfga)

