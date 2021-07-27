import json
from projects.models import My_Portfolio

# python manage.py flush
# python manage.py shell
# import projects.load_data

GITHUB_URL = "https://raw.githubusercontent.com/and88x/af_portfolio/50c7f7fecc3c60d5f70247f5f5dbe88238c65f49/projects/static/"
# Opening JSON file
with open('./projects/static/data.json') as json_file:
    data = json.load(json_file)

    p = [None] * len(data['project'])
    j = 0

    for i in data['project']:    
        p[j] = My_Portfolio(
            title        = i["title"],
            sdescription = i["sdescription"],
            ldescription = i["ldescription"],
            technology   = i["technology"],
            image        = GITHUB_URL+i["image"],
            second_img   = GITHUB_URL+i["second_img"],
            link         = i["link"]
        )
        p[j].save()     
        j += 1 