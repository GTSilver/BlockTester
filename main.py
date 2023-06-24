import json

str_json = """
{
"file_separator": "-"
}
"""

data = json.loads(str_json)

with open('config.json', 'w') as file:
    json.dump(data, file, indent = 4)
