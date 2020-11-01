# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://incident-integration-test.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("incident.integration.test@gmail.com", "JpVFJgi5Gq3TumSE20AiE590")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps({
    "update": {},
    "fields": {
        "summary": "Main order flow broken",
        "project": {
            "key": "TEST1"
        },
        "issuetype": {
            "name": "Zadanie"
        },
    }
})

response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
