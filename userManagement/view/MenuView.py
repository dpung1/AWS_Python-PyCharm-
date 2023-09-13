from userManagement.view.UserView import UserView
class MenuView:

    @staticmethod
    def index():
        print("[사용자 관리 프로그램]")
        print("1. 사용자 전체 조회")
        print("2. username으로 사용자 정보 검색")
        print("3. 사용자 등록")
        print("4. 사용자 수정")
        print("5. 사용자 삭제")
        print("q. 프로그램 종료")

        try:
            select = input("메뉴 선택 >>> ")

            if select == "q":
                return False
            elif select == "1":
                UserView.showAllUser()
            elif select == "2":
                UserView.showFindUser()
            elif select == "3":
                UserView.register()
            elif select == "4":
                UserView.updateUser()
            elif select == "5":
                UserView.deleteUser()
            else:
                print("선택하신 번호는 등록되지 않은 메뉴입니다.")

            print()
            return True

        except KeyboardInterrupt:
            return None
