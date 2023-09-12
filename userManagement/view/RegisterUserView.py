class RegisterUserView:

    @staticmethod
    def register():
        from userManagement.entity.User import User
        from userManagement.controller.UserController import UserController
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

        print(response.__dict__)
