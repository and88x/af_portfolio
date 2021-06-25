import json
from projects.models import My_Portfolio

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
            image        = i["image"],
            second_img   = i["second_img"],
            link         = i["link"]
        )
        p[j].save()     
        j += 1 