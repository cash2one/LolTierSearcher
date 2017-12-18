from tkinter import *
import PIL.Image
import PIL.ImageTk

class PopupMaker:
    def __init__(self):
        self.imageCache = []

    def showTierInfo(self, tierInfo, timelimit):
        print(tierInfo)
        headColor = "#59D9A4"
        bgColor= "#39414e"
        frameWidth = 200
        labelWidth = int(frameWidth / 10)
        toplevel = Toplevel(background="black")
        for t in tierInfo:
            name = t["name"]
            tier = t["tier"]
            rank = t["rank"]

            frame = Frame(toplevel, background="black")
            frame.pack(side=LEFT)

            name_label = Label(frame, width=labelWidth, text=name, background=headColor)
            name_label.config(justify=CENTER, fg=bgColor, font=("calibri", 15))
            name_label.pack()

            tier_label = Label(frame, width=labelWidth, text=tier + " " + rank, background=bgColor)
            tier_label.config(justify=CENTER, fg="white", font=("calibri", 15))
            tier_label.pack()


            tier_img_url = "images/tier/"+tier.lower()+"_"+rank+".png"
            tier_img = PIL.Image.open(tier_img_url)
            photo = PIL.ImageTk.PhotoImage(tier_img)
            self.imageCache.append(photo)
            tier_img_label = Label(frame, image=photo, background="black")
            tier_img_label.pack()
        ws = toplevel.winfo_screenwidth()
        hs = toplevel.winfo_screenheight()


        w = frameWidth * 5  #ws * 0.2
        h = 250  #ws * 0.1
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        toplevel.geometry('%dx%d+%d+%d' % (w, h, x, 0))
        toplevel.wm_attributes("-transparentcolor", "black")
        toplevel.attributes('-topmost', 'true')
        toplevel.overrideredirect(True)
        toplevel.after(timelimit, lambda: toplevel.destroy())

if __name__ == "__main__":
    root = Tk()
    p = PopupMaker()
    tierInfo = [{"name":"방금잡은해산물", "tier":"Gold 5"}, {"name":"방금잡은해산물", "tier":"Gold 5"}, {"name":"방금잡은해산물", "tier":"Gold 5"}, {"name":"방금잡은해산물", "tier":"Gold 5"}, {"name":"방금잡은해산물", "tier":"Gold 5"}]
    p.showTierInfo(tierInfo, 5000)