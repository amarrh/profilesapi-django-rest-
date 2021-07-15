import requests

def client():
    token_h = "Token 450972a219e5f3b17c920afb08694d2501d7bcc4"
    #data = {
    #        "username": "test", 
    #        "email": "mail@example.com",
    #        "password1": "testrest123",
    #        "password2": "testrest123"
    #        }

    #response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
    #                         data=data)

    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()