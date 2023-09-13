from userManagement.config.DataBaseConfig import DataBaseConfig, pymysql
import pandas as pd

class UserRepository:

    @staticmethod
    def saveUser(user = None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            insert into user_tb
            values(0, %s, %s, %s, %s)
            """
            insertConut = cursor.execute(sql,
                                         (user.username,
                                          user.password,
                                          user.name,
                                          user.email))
            connection.commit()
            return insertConut

        except Exception as e:
            print(e)
            return 0

    @staticmethod
    def getUsersAll():
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            select 
                user_id as userId,
                username,
                password,
                name,
                email
            from
                user_tb
            """
            cursor.execute(sql)
            rs = cursor.fetchall()
            return rs

        except Exception as e:
            print(e)
            return None

    @staticmethod
    def findUserByUsername(username = None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            select
                user_id as userId,
                username,
                password,
                name,
                email
            from
                user_tb
            where
                username = %s
            """
            cursor.execute(sql, (username))
            rs = cursor.fetchone()
            return rs

        except Exception as e:
            print(e)
            return None

    @staticmethod
    def updateUser(user = None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            update user_tb
            set
                password = %s,
                name = %s,
                email = %s
            where
                user_id = %s
            """
            updateConut = cursor.execute(sql,
                                         (user.get("password"),
                                          user.get("name"),
                                          user.get("email"),
                                          user.get("userId")))
            connection.commit()
            return updateConut

        except Exception as e:
            print(e)
            return 0

    @staticmethod
    def deleteUser(userId = None):
        print(userId)
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            delete
            from user_tb
            where user_id = %s
            """
            cursor.execute(sql, (userId))
            rs = cursor.fetchone()
            return rs

        except Exception as e:
            print(e)
            return None


# if __name__ == '__main__':
#     userList = UserRepository.getUsersAll()
#     print(userList)
#
#  # pandas example
#     data = {
#         "userId": [1, 2, 3, 4, 5],
#         "username": ["aaa", "bbb", "ccc", "ddd", "eee"],
#         "password": ["1234", "1234", "1234", "1234", "1234"],
#         "name": ["aaa", "bbb", "ccc", "ddd", "eee"],
#         "email": ["aaa@gmail.com", "bbb@naver.com", "ccc@gmail.com", "ddd@nate.com", "eee@naver.com"]
#     }
#
#     # print(pd.Series(userList))
#     # df = pd.DataFrame(data, index=data["userId"])
#     # print(df.get("username"))
