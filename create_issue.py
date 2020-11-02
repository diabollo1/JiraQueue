# https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/
# http://docs.python-requests.org
import requests
import json

from conf import jira_conf

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
    jira_conf.url,
    data=payload,
    headers=jira_conf.headers,
    auth=jira_conf.auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
