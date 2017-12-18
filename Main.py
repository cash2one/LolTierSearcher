from LolApiGetter import LolApiGetter
from PopupMaker import PopupMaker
from MyThread import MyThread

from tkinter import *
from tkinter import messagebox

class MyApp:
    def __init__(self):
        ## 변수
        self.key = ""
        self.apiGetter = LolApiGetter()
        self.popupMaker = PopupMaker()
        self.nickname = ""

        ## 쓰레드
        self.t = MyThread()
        self.t.daemon = True # 부모 종료 시 같이 종료
        self.t.setApiGetter(self.apiGetter)
        self.t.setPopupMaker(self.popupMaker)

        ## UI
        self.root = Tk()
        self.main_frame = Frame(self.root)
        self.main_frame.pack()
        
        self.label = Label(self.main_frame, text="API KEY")
        self.label.pack()
        self.txt_key = Entry(self.main_frame)
        self.txt_key.pack()

        self.label2 = Label(self.main_frame, text="소환사 이름")
        self.label2.pack()
        self.txt = Entry(self.main_frame)
        self.txt.pack()

        self.btn_ok = Button(self.main_frame, text="OK", command=self.setNicknameByBtn)
        self.btn_ok.pack()

        self.txt.focus_force()
        self.root.mainloop()

    def setNicknameByBtn(self):
        self.nickname = self.txt.get()
        self.apiGetter.setApiKey(self.txt_key.get())

        if self.nickname == "":
            messagebox.showinfo("알림", "닉네임을 입력해주세요")
        else:
            messagebox.showinfo("이름", self.nickname)
            self.main_frame.destroy()
            self.main_frame = Frame(self.root)
            self.main_frame.pack()
            new_label = Label(self.main_frame, text="실행중")
            new_label.pack()

            self.t.setNickname(self.nickname)
            self.t.start()

    def tt(self):
        toplevel = Toplevel()


        frame = Frame(toplevel, background="white")
        frame.pack(side=LEFT)
        name_label = Label(frame, text="name", background="white")
        name_label.pack()
        tier_label = Label(frame, text="tier", background="white")
        tier_label.pack()

        toplevel.attributes('-topmost', 'true')
        toplevel.after(3000, lambda: toplevel.destroy())

if __name__ == "__main__":
    app = MyApp()




