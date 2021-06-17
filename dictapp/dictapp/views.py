import json
import requests
from decouple import config
from django.shortcuts import render
from django.http import JsonResponse

app_id = config('APP_ID') ## assign your own ID
app_key = config('APP_KEY') ## assign your own KEY
language = config('LANGUAGE') ## assign language

def index(request):
    return render(request, "index.html")

def dict_view(request, *args, **kwargs):
    if request.method == "POST":
        data = request.POST.copy()
        word_id = data.get("word")
        if word_id:
            url = (
                "https://od-api.oxforddictionaries.com:443/api/v2/entries/"
                + language
                + "/"
                + word_id.lower()
            )

            r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
            if "error" in r.json():
                return JsonResponse({"error": r.json()["error"]})
            
            results = r.json()["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]
            results_alt = r.json()

            definitions = ""
            definitions_sub = ""
            examples = ""
            examples_sub = ""
            shortdef = ""
            shortdef_sub = ""
            synonyms = []

            if ("definitions" in results.keys()):
                definitions = results["definitions"][0]
            if ("examples" in results.keys()):
                examples = results["examples"][0]["text"]
            if ("shortDefinitions" in results.keys()):
                shortdef = results["shortDefinitions"][0]
            if ("subsenses" in results.keys()):
                if ("definitions" in results["subsenses"][0].keys()):
                    definitions_sub = results["subsenses"][0]["definitions"][0]
                if ("examples" in results["subsenses"][0].keys()):
                    examples_sub = results["subsenses"][0]["examples"][0]["text"]
                if ("shortDefinitions" in results["subsenses"][0].keys()):
                    shortdef_sub = results["subsenses"][0]["shortDefinitions"][0]
            if ("synonyms" in results.keys()):
                synonyms_list = results["synonyms"]
                for item in synonyms_list:
                    synonyms.append(item["text"])
            elif ("synonyms" not in results.keys()):
                synonyms = ["-"]

            return JsonResponse({
                "definitions":definitions,
                "definitions_sub":definitions_sub,
                "examples":examples,
                "examples_sub":examples_sub,
                "shortdef":shortdef,
                "shortdef_sub":shortdef_sub,
                "synonyms_list":synonyms,
                "word":word_id,
            })
            
        return JsonResponse({"error":"word is required"})