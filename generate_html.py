import json
from os import listdir
from os.path import isfile, join
import random

f = open("messages.json", "r")
messages = json.load(f)["messages"]
f.close()

images_path = "images"
images = [
    f
    for f in listdir(images_path)
    if isfile(join(images_path, f)) and f.endswith(".png")
]
random.shuffle(images)

for i, msg in enumerate(messages):
    name, message = msg["name"], msg["message"]
    img_path = join(images_path , images[i])

    f = open(name + ".html", "w")

    contents = f"""<!DOCTYPE html>
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
                {name}
            </span>
            </h1>
            <div class="textBody">
                {message}
            </div>
            <div class="back">
                <a class="backA" href="./index.html">Back</a>
            </div>
            <div style="padding-top: 30px;">
            <img src="{img_path}" width="100%">
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    </body>
</html>"""

    f.write(contents)
    f.close()
    print("done writing {}.html".format(name))
