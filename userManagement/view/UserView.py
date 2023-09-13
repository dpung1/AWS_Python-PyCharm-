from userManagement.entity.User import User
from userManagement.controller.UserController import UserController
import pandas as pd

class UserView:

    @staticmethod
    def register():
        print("[사용자 등록 화면]")
        username = input("사용자 이름 >>> ")
        password = input("비밀번호 >>> ")
        name = input("이름 >>> ")
        email = input("이메일 >>> ")
        response = UserController.registerUser(User(
            username=username,
            password=password,
            name=name,
            email=email
        ))

        if not response.__dict__.get("body"):
            print("데이터를 추가하는 중 오류가 발생하였습니다.")
            print("다시 시도해 주세요.")

    @staticmethod
    def showAllUser():
        response = UserController.getUsersAll()
        if bool(response.body):
            df = pd.DataFrame(response.body)
            print(df)
        else:
            print("조회 할 데이터가 없습니다.")

    @staticmethod
    def showFindUser():
        print("[ username으로 사용자 정보 검색]")
        username = input("검색하실 사용자 이름을 입력하세요. >>>")
        response = UserController.getUser(username)
        if bool(response.body):
            ps = pd.Series(response.body)
            print(ps)
        else:
            print("조회 할 데이터가 없습니다.")

    @staticmethod
    def updateUser():
        print("[ 사용자 정보 수정 ]")
        response = UserController.getUsersAll()
        if not bool(response.body):
            print("수정 할 사용자 정보가 없습니다.")
            return
        df = pd.DataFrame(response.body)
        print(df)
        userId = input("수정하실 userId를 입력하세요 >>>")
        index = df.index[df["userId"] == int(userId)].values[0]
        user = UserView.showUpdateMenu(response.body[index])
        if not bool(user):
            print("수정을 취소하였습니다.")
            return

        response = UserController.updateUser(user)
        if bool(response.body):
            print("========<< 수정 완료 >>========")


    @staticmethod
    def showUpdateMenu(oldUser):
        newUser = oldUser.copy()

        while True:
            print("-" * 50)
            df = pd.DataFrame([oldUser, newUser], index=["수정 전", "수정 후"])
            print(df)
            print("-" * 50)
            print("1. password")
            print("2. name")
            print("3. email")
            print("s. 저장")
            print("c. 취소")
            print("-" * 50)
            select = input("메뉴 선택 >>> ")

            if select == "c":
                return None
            elif select == "s":
                return newUser
            elif select == "1":
                password = input("비밀번호 입력 >>> ")

                if not UserView.isValid(oldUser.get("password"), password):
                    continue

                checkPassword = input("비밀번호 확인 입력 >>> ")

                if checkPassword != password:
                    print("비밀번호가 일치하지 않습니다.")
                    continue

                newUser["password"] = password

            elif select == "2":
                name = input("이름 입력 >>> ")

                if not UserView.isValid(oldUser.get("name"), name):
                    continue

                newUser["name"] = name

            elif select == "3":
                email = input("이메일 입력 >>> ")

                if not UserView.isValid(oldUser.get("email"), email):
                    continue

                newUser["email"] = email
            else:
                print("선택하신 번호는 등록되지 않은 메뉴입니다.")
            print()

        return newUser

    @staticmethod
    def isValid(oldValue, value):
        if not bool(value):
            print("공백일 수 없습니다.")
            return False
        elif oldValue == value:
            print("기존의 정보와 동일합니다.")
            return False

        return True

    @staticmethod
    def deleteUser():
        print("[ 사용자 정보 ]")
        response = UserController.getUsersAll()
        if not bool(response.body):
            print("삭제 할 사용자 정보가 없습니다.")
            return
        df = pd.DataFrame(response.body)
        print(df)
        userId = input("삭제 하실 아이디를 입력하세요. >>>")
        response = UserController.deleteUser(userId)
        if bool(response.body):
           print("========<< 삭제 완료 >>========")
        else:
            print("조회 할 데이터가 없습니다.")



