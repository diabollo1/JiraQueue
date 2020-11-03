from datetime import datetime
from lib.JiraIssue import JiraIssue

data = {
    "issueUpdates": [
        {
            "update": {},
            "fields": {
                "summary": "1Main order flow broken " + str(datetime.now()),
                "project": {
                    "key": "TEST1"
                },
                "issuetype": {
                    "name": "Zadanie"
                },
            }
        }, {
            "update": {},
            "fields": {
                "summary": "2Main order flow broken " + str(datetime.now()),
                "project": {
                    "key": "TEST1"
                },
                "issuetype": {
                    "name": "Zadanie"
                },
            }
        }
    ]
}

i1 = JiraIssue()
print(i1.create_issue(data))
