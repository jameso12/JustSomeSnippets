import json

org = list('la tierra')
org.append(None)
js = json.dumps(org)
org = json.loads(js)
print("json:")
print(js)
print('python:')
print(org)