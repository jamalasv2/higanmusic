import os
from typing import List

import yaml

languages = {}
languages_present = {}


def get_string(lang: str):
    return languages[lang]


for filename in os.listdir(r"./strings/langs/"):
    if "in" not in languages:
        languages["in"] = yaml.safe_load(
            open(r"./strings/langs/in.yml", encoding="utf8")
        )
        languages_present["in"] = languages["in"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "in":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["in"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["in"][item]
    try:
        languages_present[language_name] = languages[language_name]["name"]
    except:
        print("There is some issue with the language file inside bot.")
        exit()
