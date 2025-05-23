import json

# data={
#     "Name":"Lolly",
#     "Height": 1.9
# }
#
# with open("data.json","w") as f:
#     json.dump(data,f,indent=4)
#

with open("data.json","r") as f:
    oldData= json.load(f)

newList=[]
newList.append(oldData)

newData={
    "Name":"Harry",
    "Height":1.6
}

newList.append(newData)

with open("data.json","w") as f:
    json.dump(newList,f, indent=4)