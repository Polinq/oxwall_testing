import json
import pymysql

from models.news import News
from models.user import User


def _our_unknown_hash(password):
    return {
        "admin": "ae6179668fb6d3770ff2eba85f2c2fb8b06b3a174b79def62ee282fe0967fcbf",
        "test": "5f5da2ccbff4c3d0b998dd141ccc5cf39aa133d3031d66dc4628fc4438265962",
        "secret": "18256c1219e2ce08cab40242b1101e7aeb290e6beb0000af9422792f94d0191f"
    }[password]


class OxwallDB:
    def __init__(self, config):
        self.connection = pymysql.connect(
            **config,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def create_user(self, user):
        with self.connection.cursor() as cursor:
            sql = """INSERT INTO `ow_base_user` (`username`, `email`, `password`) 
            VALUES ("{}", "{}", "{}")""".format(user.username, user.email, _our_unknown_hash(user.password))
            cursor.execute(sql)
        self.connection.commit()

    def delete_user(self, user):
        with self.connection.cursor() as cursor:
            sql = """DELETE FROM `ow_base_user` 
            WHERE `ow_base_user`.`email` = %s"""
            cursor.execute(sql, (user.email,))
        self.connection.commit()

    def get_users(self):
        with self.connection.cursor() as cursor:
            sql = """SELECT `username`, `email`, `password` FROM `ow_base_user`"""
            cursor.execute(sql)
            result = [User(**user) for user in cursor]
        self.connection.commit()
        return result

    def get_last_news(self):
        """ Get newsfeed with maximum id that is last added """
        with self.connection.cursor() as cursor:
            sql = """SELECT * FROM `ow_newsfeed_action` 
                     WHERE `id`= (SELECT MAX(`id`) FROM `ow_newsfeed_action`)
                     AND `entityType`="user-status"
                     """
            cursor.execute(sql)
            line = cursor.fetchone()
            data = json.loads(line["data"])
        self.connection.commit()
        return News(text=data["status"])

    def count_news(self):
        with self.connection.cursor() as cursor:
            sql = """SELECT COUNT(*) FROM `ow_newsfeed_action` 
                     WHERE `entityType`="user-status"
                  """
            cursor.execute(sql)
        self.connection.commit()
        return cursor.fetchone()['COUNT(*)']


if __name__ == "__main__":
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "mysql",
        "db": "oxwa892"
    }
    user = User(username="test123", password="test", email="tester123@gmail.com")
    db = OxwallDB(db_config)
    print(db.get_users())
    db.create_user(user)
    print(db.get_users())
    db.delete_user(user)
    print(db.get_users())
