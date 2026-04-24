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
print(titanic_df[titanic_df["Age"]<18,["name","pclass"]])
highest = titanic_df["Age"].max
print(highest)
