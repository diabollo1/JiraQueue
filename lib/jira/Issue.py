import json
import requests

from conf import jira_conf


class Issue:
    def __init__(self):
        self.url = jira_conf.url
        self.auth = jira_conf.auth
        self.headers = jira_conf.headers

    def create_issue(self, data):
        # print("abc" + str(json))

        payload = json.dumps(data)

        response = requests.request(
            "POST",
            self.url,
            data=payload,
            headers=self.headers,
            auth=self.auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
