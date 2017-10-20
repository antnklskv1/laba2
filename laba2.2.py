ivan = {
    "name" : "ivan",
    "age" : 34,
     "children":[{
         "name":"vasja",
         "age":25,
     },{
         "name":"petja",
         "age":25,
     }],
}

darja = {
    "name" : "darja",
    "age" : 41,
     "children":[{
         "name":"kirill",
         "age":21,
     },{
         "name":"pavel",
         "age":25,
     }],
}

emps = [ivan, darja]


emps = [ivan, darja]
for i in emps:
    for j in range(len(i["children"])):
        if i["children"][j]["age"] > 18:
            print(i["name"])
            break
