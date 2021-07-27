import json
with open('json/credentials.json') as credentials_j:
    credentials = json.load(credentials_j)
with open('json/settings.json') as settings_j:
    sj = json.load(settings_j)

print(sj)