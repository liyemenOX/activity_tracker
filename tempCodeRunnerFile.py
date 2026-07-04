import json
from datetime import datetime

with open ('db.json','r',encoding = 'utf-8')as file:
    db = json.load(file)

print("=================================================")
print("----------------ACTIVITY TRACKER-------------")
print("=================================================")

new_task = input("enter the task you have done today => ")
status = input("Enter the status: pending/completed/reschedule")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

load_db= {
"new_task": new_task,
"status": status,
"current_time": current_time
}

db.append(load_db)

with open ('db.json','w',encoding = 'utf-8')as file:
    json.dump(db,file,indent = 4)
    
print("Task saved successfully")