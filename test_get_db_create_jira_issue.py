import sys

from lib.DatabaseInput import DatabaseInput
from lib.JiraIssue import JiraIssue

try:
    db = DatabaseInput()
    issues = db.get_issue_to_create_list()

    print(issues)

    data = {"id": "", "json": {"issueUpdates": []}}
    for issue in issues:
        data["id"] += str(issue[0]) + ","
        data["json"]["issueUpdates"].append(eval(issue[3]))

    data["id"] = data["id"].rstrip(',')

    print(data)

    i1 = JiraIssue()
    create_issue_output = i1.create_issue(data["json"])
    print(create_issue_output)

    print(db.set_data_issue(data["id"],create_issue_output))

except ResourceWarning as e:
    print("It looks ok but: " + str(e))
except Exception as e:
    print("The error occurred: " + __name__ + ":" + str(sys.exc_info()[2].tb_lineno) + "|" + str(e))
