import requests


class YoujileProject:
    def __init__(self, url, token):
        self.url = url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, name):
        project = {
            "title": name
        }
        resp = requests.post(f"{self.url}/api-v2/projects",
                             json=project, headers=self.headers)
        return resp

    def get_project_by_id(self, id):
        resp = requests.get(f"{self.url}/api-v2/projects/{id}",
                            headers=self.headers)
        return resp

    def edit_project(self, new_id, new_name):
        project = {
             "title": new_name
             }
        result = requests.put(f"{self.url}/api-v2/projects/{new_id}",
                              json=project, headers=self.headers)
        return result
