from userManagement.config.DataBaseConfig import DataBaseConfig, pymysql

class UserRepository:

    @staticmethod
    def saveUser(user = None):
        connection = DataBaseConfig.getConnection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = f"""
insert into user_tb
values(0, %s, %s, %s, %s)
"""
        insertConut = cursor.execute(sql, (user.username, user.password, user.name, user.email))
        connection.commit()
        return insertConut