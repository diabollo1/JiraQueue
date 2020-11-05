import json
import sys
from aifc import Error

import requests

from conf import jira_conf, log_conf


class JiraIssue:
    def __init__(self):
        self.url = jira_conf.url
        self.auth = jira_conf.auth
        self.headers = jira_conf.headers

        self.logger = log_conf.get_logger(__class__.__name__ + ".log")

    def create_issue(self, data):
        try:
            payload = json.dumps(data)
            self.logger.debug("Tries to send to Jira json: " + payload)

            response = requests.request(
                "POST",
                self.url,
                data=payload,
                headers=self.headers,
                auth=self.auth
            )

            if not response.ok:
                raise Error("Error response code: " + str(response))

            if json.loads(response.text)["errors"]:
                raise Error("Error creating issue" + json.dumps(json.loads(response.text)["errors"]))

            return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

        except requests.exceptions.RequestException as e:
            self.logger.error("The error occurred: " + str(e))
            raise Error(__name__ + ":" + str(sys.exc_info()[2].tb_lineno) + "|" + str(e))

        except Error as e:
            self.logger.error("The error occurred: " + str(e))
            raise Error(__name__ + ":" + str(sys.exc_info()[2].tb_lineno) + "|" + str(e))
