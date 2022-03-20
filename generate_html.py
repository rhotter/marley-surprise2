import json

f = open("messages.json","r")
messages = json.load(f)["messages"]
f.close()

for i in messages:
    name, message = i["name"],i["message"]
    f = open(name + ".html", "w")


    contents = """<!DOCTYPE html>
<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <title>Definitely Curius.app</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="page.css">
    </head>
    <body>
        <div class="container-sm">
            
            <h1 class="name">
                <span class="highlight">
                {nm}
            </span>
            </h1>
            <div class="textBody">
                {msg}
            </div>
            <div class="back">
                <a class="backA" href="./index.html">Back</a>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    </body>
</html>
""".format(nm=name,msg=message)


    f.write(contents)
    f.close()
    print("done writing {}.html".format(name))


