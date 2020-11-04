from lib.DatabaseInput import DatabaseInput
from lib.JiraIssue import JiraIssue

db = DatabaseInput()
issues = db.get_issue_to_create_list()

data = {"issueUpdates": []}
for issue in issues:
    data["issueUpdates"].append(eval(issue[3]))

print(data)

i1 = JiraIssue()
print(i1.create_issue(data))
