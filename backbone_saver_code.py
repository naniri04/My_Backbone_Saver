from win10toast import ToastNotifier


title_list = {"당신의 척추가 고통스러워합니다!"
              , "마지막으로 스트레칭한지 1시간 반이 지났습니다!"
              , "허리 스트레칭을 할 때입니다!"
              , "자리에서 잠시 일어날 때 입니다!"}

def notify():
    toaster = ToastNotifier()
    title = title_list.pop()
    message = "잠시 시간을 내어 허리를 쭉 펴세요"

    toaster.show_toast(title, message, duration=1)
    title_list.add(title)
        
if __name__ == "__main__":
    notify()
