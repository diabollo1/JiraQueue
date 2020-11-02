from datetime import datetime
from lib.jira.Issue import Issue

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

i1 = Issue()
print(i1.create_issue(data))
