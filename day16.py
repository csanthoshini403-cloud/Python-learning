import json
employee={"name":"Ganga","age":"24","positon":"web developer"}
file_path="output.json"
with open (file_path,"w") as file:
    json.dump(employee,file,indent=4)
print("Data written successfully!")    

import csv
employee=[["name","age"],
["sanu",23],
["ray",25],
["june",33]]
file_path="output.csv"
with open (file_path,"w") as file:
   write = csv.writer(file)
   for data in employee:
       write.writerow(data)
