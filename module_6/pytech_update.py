#camille carter 
# week 6


print(record)

 

result = collection.update_one(

 

{"student_id":1007},

 

{

 

"$set":{

 

"last_name":"Smith"

 

}

 

}

 

)

 

cursor = collection.find()

 

for record in cursor:

 

print(record)