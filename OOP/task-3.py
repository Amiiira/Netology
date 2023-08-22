# Задание 1 : Кто самый умный супергерой?

import requests
from pprint import pprint

response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
data = response.json()


our_heroes = {
    'Hulk' : 0,
    'Captain America' : 0,
    'Thanos' : 0
}

for hero in data:
    name = hero["name"]
    power = hero["powerstats"]
    intelligence = power["intelligence"]
    if name in our_heroes:
        our_heroes[name] = intelligence

smartest_one = max(our_heroes, key=our_heroes.get)
print(f"Самый умный герой - это {smartest_one}")


# Задание 2: Яндекс.Диск

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            "path": file_path
        }
        headers = {
            "Authorization": token
        }
        response = requests.get(url, headers=headers, params=params)
        if 200 <= response.status_code < 300:
            print(response.status_code)
            pprint(response.json())
        url_for_upload = response.json().get('href', '')
        with open(file_path, 'rb') as file:
            response2 = requests.put(url_for_upload, files={"file": file})


if __name__ == '__main__':
    path_to_file = 'Morocco.jpg'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

# Задание 3: 

url = 'https://api.stackexchange.com/2.3/questions?fromdate=1692489600&order=desc&sort=activity&tagged=Python&site=stackoverflow'
response = requests.get(url)

data_info = response.json().get('items', {})

questions = []
for data in data_info:
    question = data.get('title', "")
    questions.append(question)

pprint(questions)