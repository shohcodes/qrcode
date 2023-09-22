import datetime
import json
import os

qrcode_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
users_json_path = os.path.join(qrcode_dir, 'bot', 'users.json')


class DB:
    def __init__(self):
        self.users = []
        try:
            with open(users_json_path, 'r') as data:
                self.users = json.load(data)
        except FileNotFoundError:
            with open(users_json_path, 'x') as data:
                json.dump(self.users, data)

    def commit(self):
        with open(users_json_path, 'w') as data:
            json.dump(self.users, data, indent=4)

    def select_user(self, user_id: str):
        for user in self.users:
            if user['user_id'] == user_id:
                return user

    def insert_into(self, user_id: str, username: str, full_name: str):
        quantity_of_users = len(self.users)
        self.users.append(
            {'id': quantity_of_users + 1, "user_id": user_id, "username": username, "full_name": full_name,
             "joined_at": str(datetime.datetime.now())})
        self.commit()
