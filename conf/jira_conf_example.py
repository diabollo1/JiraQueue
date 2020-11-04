from requests.auth import HTTPBasicAuth

url = "https://<site-url>.atlassian.net/rest/api/3/issue/bulk"

auth = HTTPBasicAuth("<user_mail>", "<user_rest_api_password>")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
