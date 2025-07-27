import pandas as pd
data={"date":["1/1/2025","2/1/2025","3/1/2025","1/1/2025","2/1/2025","3/1/2025","1/1/2025","2/1/2025","3/1/2025"],
      "city":["Chennai","Chennai","Chennai","Mumbai","Mumbai","Mumbai","Banglore","Banglore","Banglore"],
      "temp":[25,35,24,34,25,36,34,27,32],
      "humid":[40,50,40,50,40,50,50,41,49]}
df=pd.DataFrame(data)
print("Created Df :\n",df)
#PIVOTING DF using df.pivot()/pivot_table()
#Parameters: index="which column should be rows",column="which column should be columns"
dfpivot=df.pivot_table(index="date",columns="city")
print("Pivoted DF :\n",dfpivot)
#need only specific values - example temp - use values="temp"
dfpivottemp=df.pivot_table(index="date",columns="city",values="temp")
print("Pivoted DF with temp vlaues :\n",dfpivottemp)
#to fill null values, use fillvalue ="value"
dfpivottempwithfill=df.pivot_table(index="date",columns="city",values="temp",fill_value=0)
print("Pivoted DF with temp vlaues with fillvalue :\n",dfpivottempwithfill)

#APPLYING AGGREGATE FUNCTIONS IN PIVOT TABLE - sum(),mean(),count()
#pivot_table()
pivotcount=df.pivot_table(index="date",columns="city",values="temp",aggfunc="count",)
print("count of temp using pivot_table(aggfunc=count):\n",pivotcount)
print()
pivotmean=df.pivot_table(index="date",columns="city",values="temp",aggfunc="mean")
print("mean of temp using pivot_table(aggfunc=mean):\n",pivotmean)
#use margins=Ture for row wise and column wise sum
pivotcountmargin=df.pivot_table(index="date",columns="city",values="temp",aggfunc="count",margins=True)
print("Count of temp with margin using pivot_table(aggfunc=count):\n",pivotcountmargin)
print()
pivotmeanmargin=df.pivot_table(index="date",columns="city",values="temp",aggfunc="mean",margins=True)
print("mean of temp with margin using pivot_table(aggfunc=mean):\n",pivotmeanmargin)
print()
pivotmin=df.pivot_table(index="date",columns="city",values="temp",aggfunc="min",margins=True)
print("min of temp with margin using pivot_table(aggfunc=min):\n",pivotmin)
print()
pivotmax=df.pivot_table(index="date",columns="city",values="temp",aggfunc="max",margins=True)
print("max of temp with margin using pivot_table(aggfunc=max):\n",pivotmax)
print()
#for multiple aggfunc in single display , use -[]
pivotagg=df.pivot_table(index="date",columns="city",values="temp",aggfunc=["min","max","count","sum","mean"],margins=True)
print("Agg values of temp with margins using pivot_table(aggfunc=[]):\n",pivotagg)
print()