import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://incident-integration-test.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("incident.integration.test@gmail.com", "JpVFJgi5Gq3TumSE20AiE590")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

issueIdOrKey = "TEST1-5"

url += "/" + issueIdOrKey

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
