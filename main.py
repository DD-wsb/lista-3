import requests

BASE_URL = "https://swapi.dev/api/"
people_list = [1, 2, 3]


def run_requests():
    data = []
    for i in people_list:
        data.append(requests.get(f'{BASE_URL}/people/{i}'))
    return data


def check_data(data):
    for i in data:
        json = i.json()
        print(json)
        if isinstance(json, dict) and "name" in json and i.status_code == 200:
            print("TEST PASSED")
        else:
            print("TEST FAILED")


if __name__ == '__main__':
    check_data(run_requests())
