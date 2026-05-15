import pandas as pd
# creating data frame from dictinary 

students = {"name": ["jack", "james", "ethan"],
            "age": [15, 17, 16],
            "year": [10, 12, 11]}

students_df = pd.DataFrame(students, index = ["s1","s2","s3"])
print(students_df)
#creating data frame from list
students_list = [["Jack", 15, 10],["James", 17, 12],["Ethan", 16, 11]]
students_df2 = pd.DataFrame(students_list, columns=["name","age","year"])
print(students_df2)

#complete info 
students_df.info()

#describe 
print(students_df.describe())

#reading csv file
titanic_df = pd.read_csv("/Users/clarence/Desktop/data science/titanic.csv")
titanic_df.info()
print(titanic_df)

#fetch records from start
print(titanic_df.head()) #by defalt it gives 5 records, specify if want different amount

#fetch records from bottem
print(titanic_df.tail())

#shape of the data frame
print(titanic_df.shape)

#retrieve values for a single column
print(titanic_df["Name"])

#to find the age of the oldest passenger
print(titanic_df["Age"].max())
print(titanic_df["Fare"].sum())

#fetch multiple columns
print(titanic_df[["Name","Age"]])

#conditional filtering
print(titanic_df[titanic_df["Age"]<18])
print(titanic_df[(titanic_df["Pclass"]==1)&(titanic_df["Age"]<18)]) # or = |
#sliceing with index
print(titanic_df.iloc[400:410:2,2:5])
print(titanic_df.iloc[[5,30,25,50],[1,3,4]])

#conditional slicing
print(titanic_df.loc[titanic_df["Age"]<18,["Name","Pclass"]])
highest = titanic_df["Age"].max()
print(highest, "agqwidquwidhaishdoahsdoiawjodae")
print(titanic_df.loc[titanic_df["Age"]==highest,["Name","Survived"]])
print(titanic_df.loc[titanic_df["Survived"]==1,["Name","Pclass"]])

#change values
titanic_df.loc[0:2,"Name"] = ["adww", "dqwd", "qwdqw"]
print(titanic_df.loc[0:2,"Name"])

#
titanic_df["discounted fare"] = titanic_df["Fare"]/2
print(titanic_df["discounted fare"].head(10))
#rename collumns
titanic_df.rename(columns={"Fare":"Ticket Price", "discounted fare": "50ff"},inplace=True)
print(titanic_df)
#create csv
titanic_df.to_csv("newtitanic.csv")
#sort data frame
titanic_df = titanic_df.sort_values(by="Name")
print(titanic_df)
#replace values
titanic_df["Sex"] = titanic_df["Sex"].replace({"male":"M","female":"F"})
print(titanic_df)
#agrigation function
print(titanic_df.agg({"Age":["min","max"],"Ticket Price":["sum","mean"]}))
#grouping
pclassgroup = titanic_df.groupby(by="Pclass")
print(pclassgroup.max())
print(titanic_df.groupby(by=["Pclass","Sex"]).max())
print(titanic_df.groupby(by=["Pclass","Sex"])[["Age","Ticket Price"]].mean())
#operations on text data

print(titanic_df["Name"].str.lower())
titanic_df["last name"] = titanic_df["Name"].str.split().str.get(-1)
print(titanic_df)
