from jinja2 import Template
from json import loads, dumps

data = loads(open("data.json", "r").read())
digest = {}

for store in data.keys():
    for day in data[store].keys():
        if day not in digest:
            digest[day] = {
                store: data[store][day]
            }
        else:
            digest[day][store] = data[store][day]

template = Template(open("template/index.html", "r", encoding="utf-8").read())
output = template.render(data=digest)

open("dist/index.html", "wb").write(output.encode("utf-8"))