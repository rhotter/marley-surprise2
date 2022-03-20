import json

f = open("messages.json","r")
messages = json.load(f)["messages"]
f.close()

for i in messages:
    name, message = i["name"],i["message"]
    f = open(name + ".html", "w")

    contents = """<DOCTYPE html>
<html>
<head>

</head>
<body>
    <h1>{nm}</h1>
    <p>{msg}</p>
</body>

</html>
    """.format(nm=name,msg=message)


    f.write(contents)
    f.close()
    print("done")


