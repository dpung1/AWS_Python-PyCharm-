class UserInfo:

    # cls변수(클래스변수 == static 변수)
    adminUser = {
        "username": "root",
        "password": "1q2w3e4r"
    }

    def __init__(self):
        self.adminUser = {
            "username": "user1",
            "password": "1234"
        }

    @classmethod
    def showAdminUSer(cls):
        print("[showAdminUSer]")
        print(cls.adminUser)

# 따로 cls 젤 위에 만들고 매개변수는 생성자로 만든다.
class User:

    def __intit__(self):
        self.username = None
        self.password = None
        self.name = None
        self.email = None

    @staticmethod
    def showUserClassInfo():
        print("그냥 실행할 수 있는 메소드")

if __name__ == "__main__":
    userInfo = UserInfo()
    print(userInfo.adminUser)
    print(UserInfo.adminUser)

    userInfo.showAdminUSer()
    UserInfo.showAdminUSer()

    User.showUserClassInfo()




























