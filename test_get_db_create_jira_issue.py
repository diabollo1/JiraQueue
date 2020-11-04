from lib.DatabaseInput import DatabaseInput
from lib.JiraIssue import JiraIssue

db = DatabaseInput()
issues = db.get_issue_to_create_list()

print(issues)

if issues:

    data = {"id": "", "json": {"issueUpdates": []}}
    for issue in issues:
        data["id"] += str(issue[0])+","
        data["json"]["issueUpdates"].append(eval(issue[3]))

    data["id"] = data["id"].rstrip(',')

    print(data)

    i1 = JiraIssue()
    create_issue_output = i1.create_issue(data["json"])
    print(create_issue_output)

    print(db.set_data_issue(data["id"],create_issue_output))
else:
    print("nope!")
