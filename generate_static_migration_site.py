import json
import os
import shutil

MIGRATION_HTML_DOC = 'index.html'

def language_paths_for_exhibit(contentfulid):
    english_page = f'en-US/exhibits/{contentfulid}'
    german_page = f'de/exhibits/{contentfulid}'
    return [english_page, german_page]

def mirror_phaeno_exhibit_with_print(contentfulid):
    for path in language_paths_for_exhibit(contentfulid):
        mirror_web_directory(path)
        mirror_web_directory(path + '/print')

def mirror_phaeno_exhibit_with_print_and_details(contentfulid):
    mirror_phaeno_exhibit_with_print(contentfulid)
    for path in language_paths_for_exhibit(contentfulid):
        mirror_web_directory(path + '/print/details')

def mirror_web_directory(path):
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, path)
    print(path)
    os.makedirs(full_path, exist_ok=True)
    shutil.copyfile(MIGRATION_HTML_DOC, full_path + '/index.html')

with open('exhibits.json', 'r') as file:
    exhibits = json.load(file)

    for exhibit in exhibits:
        if 'vertiefung' in exhibit and exhibit['vertiefung'] is not None:
            mirror_phaeno_exhibit_with_print_and_details(exhibit['contentfulid'])
        else:
            mirror_phaeno_exhibit_with_print(exhibit['contentfulid'])
