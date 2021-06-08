import requests
import json
def fake_emp():
    final_result = []

    for i in range(100):
        i += 1
        response = requests.get('https://randomuser.me/api/')
        test = response.json()
        name = f"{test['results'][0]['name']['first']} {test['results'][0]['name']['last']}"
        gender = test['results'][0]['gender']
        email = test['results'][0]['email']
        phone = test['results'][0]['phone']
        photo = test['results'][0]['picture']['medium']
        result = {
                "Name" : name,
                "Gender" : gender,
                "Phone_number" : phone,
                "email" : email,
                "photos" : photo
        }

        final_result.append(result)
    final_result = json.dumps(final_result, indent=4)
    return final_result
writeFile =open('file_name.json', 'w')
writeFile.write(fake_emp())
writeFile.close()