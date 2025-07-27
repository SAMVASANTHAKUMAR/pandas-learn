import pandas as pd
# First DataFrame
employees_data = {
    "EmpID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "DeptID": [1, 2, 1, 3]
}
employees_df = pd.DataFrame(employees_data)
# Second DataFrame
departments_data = {
    "DeptID": [1, 2, 4],
    "DepartmentName": ["HR", "Tech", "Finance"]
}
departments_df = pd.DataFrame(departments_data)
#MERGING DFs - use pd.merge(df,df,on="Column on which merge should happen")
#SIMILAR TO SQL JOINS
#Note:Only common values will be merged - INNER JOIN -DEFAULT
dfmerge=pd.merge(employees_df,departments_df,on="DeptID")
print("Merged DF using dfmerge():\n",dfmerge)
#to merge all the values - use how="outer" - OUTER JOIN
dfmergeouter=pd.merge(employees_df,departments_df,on="DeptID",how="outer")
print("Merged DF using dfmerge(outer):\n",dfmergeouter)
#for left merge - use how="left" LEFT JOIN
dfmergeleft=pd.merge(employees_df,departments_df,on="DeptID",how="left")
print("Merged DF using dfmerge(left):\n",dfmergeleft)
#for right merge - use how="right" RIGHT JOIN
dfmergeright=pd.merge(employees_df,departments_df,on="DeptID",how="right")
print("Merged DF using dfmerge(right):\n",dfmergeright)
#To know from which df the value came - use indicator=True
dfmergeindi=pd.merge(employees_df,departments_df,on="DeptID",indicator=True)
print("Merged DF using dfmerge(indicator):\n",dfmergeindi)
#if same columns are repeated in both DF, it automatically adds suffixes
#for own suffixes - use suffixes={"",""}
#example
departments_data2= {
    "EmpID": [101, 102, 103, 104],
    "DeptID": [1, 2, 4,1],
    "DepartmentName": ["HR", "Tech", "Finance","Accounts"]
}
departments_dfwithempID = pd.DataFrame(departments_data2)
#now the above df contains EmpID which is also there in employees_df
#we add suffixes to indicate that EmpID from employee_Df adn EmpID from departments_dfwithempID
dfmergesuffixes=pd.merge(employees_df,departments_dfwithempID,on="DeptID",suffixes=(" EMP_DF"," DEP_DF"))
print("Merged DF using dfmerge(suffixes):\n",dfmergesuffixes)


