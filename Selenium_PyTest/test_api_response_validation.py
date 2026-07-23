import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    print("API Response Validation")
    print("-----------------------")

    for user in users:
        print(user["name"])

    print("\nPASS - API Working Successfully")

else:

    print("FAIL")