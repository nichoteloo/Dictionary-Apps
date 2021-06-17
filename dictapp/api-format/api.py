import json
import requests

app_id = "050970e7"
app_key = "863d4f01d8a7e5b8aa359bbe9c9436aa"
language = "en-gb"
word_id = "positive"

url = (
    "https://od-api.oxforddictionaries.com:443/api/v2/entries/"
    + language
    + "/"
    + word_id.lower()
)

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
results = r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]

# out_file = open("api-format-2.json", "w")
# json.dump(results,out_file,indent=2,sort_keys=True)
# out_file.close()

# import pdb; pdb.set_trace()

definition = results["definitions"][0]
definition_sub = results["subsenses"][0]["definitions"][0]
example = results["examples"][0]["text"]
example_sub = results["subsenses"][0]["examples"][0]["text"]
shortdef = results["shortDefinitions"][0]
shortdef_sub = results["subsenses"][0]["shortDefinitions"][0]
synonyms_list = results["synonyms"]

print(definition)
print(definition_sub)
print(example)
print(example_sub)
print(shortdef)
print(shortdef_sub)
print(synonyms_list)