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