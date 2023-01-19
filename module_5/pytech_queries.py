 #camille carter
 #week 5 
 
 
# Get the database instance
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.4a5dn1t.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

pytech = client.pytech
students = pytech.students
# display all documents in the collection
docs = students.find()

print ("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print()
    
    
# display a single document by student_id

print ("--DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY--")

doc = students.find_one({"student_id": "1008"})

print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")
print ()

#print ("End of program, press any key to continue...")


