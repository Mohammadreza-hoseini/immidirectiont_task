from bs4 import BeautifulSoup
import json
import requests

url = "https://www.immigration.govt.nz/new-zealand-visas/preparing-a-visa-application/working-in-nz/qualifications-for-work/green-list-occupations"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
find_all_script = soup.find_all("script")
get_script = find_all_script[2].text

index_of_get_script = get_script.index("var green_list_roles_data")
result = get_script[index_of_get_script:]

start_json = result.index("[")
end_of_json = result.rindex("]")

json_result = result[start_json: end_of_json + 1]

new_json_result = '{"json":' + json_result + "}"

final_json = json.loads(new_json_result)
f = open('jobs_name.txt', 'w+', encoding='utf-8')
for i in range(len(final_json['json'])):
    try:
        f.write(final_json['json'][i]['title'] + '\n')
    except:
        f.write(final_json['json'][i]['rich_title'] + '\n')
f.close()
