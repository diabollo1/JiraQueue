from datetime import datetime
from lib.JiraIssue import JiraIssue

data = {
    "update": {},
    "fields": {
        "summary": "Main order flow broken " + str(datetime.now()),
        "project": {
            "key": "TEST1"
        },
        "issuetype": {
            "name": "Zadanie"
        },
    }
}

i1 = JiraIssue()
print(i1.create_issue(data))
