#camille carter
#week 5



# Get the database instance
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.4a5dn1t.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

# pytech database
pytech = client.pytech

# students collection
students = pytech.students

# insert 3 students
records = [
    {
        "student_id": "1007",
        "first_name": "Thorin",
        "last_name": "Oakenshield II"
    },
    {
        "student_id": "1008",
        "first_name": "Bilbo",
        "last_name": "Baggins"
    },
    {
        "student_id": "1009",
        "first_name": "Frodo",
        "last_name": "Baggins"
    }
]

print("-- INSERT STATEMENTS --")
for record in records:
    new_student_Id = students.insert_one(record).inserted_id
    # print(record)
    print(f"Inserted student record {record['first_name']} {record['last_name']} into the students collection with document_id {new_student_Id}")
    print ()
    
   # print ("End of program, press any key to continue...")
    






















