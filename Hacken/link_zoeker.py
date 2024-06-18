import requests

# TODO 1: vervang URL door te doorzoeken webpagina.
URL = "http://172.16.2.177:8000/" 
html_code = requests.get(URL).text

# Overloop iedere regel HTML-code apart.
for regel in html_code.split("\n"):
    # TODO 2: ALS regel een link bevat...

        if "href" in regel:
            print("##############")
            print(regel)
            print("##############")