from userManagement.view.ClearView import clear

def main():
    from userManagement.view.MenuView import MenuView
    while MenuView.index():
        pass
        # clear()

if __name__ == "__main__":
    main()
    print("프로그램이 종료되었습니다.")

