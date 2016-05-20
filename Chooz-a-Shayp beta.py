#!/usr/bin/env python3
__author__ = 'javier'
from turtle import *
from tkinter import *
from math import *
import xml.etree.ElementTree as Et
from tkinter import messagebox

root = Tk()
root.iconbitmap("icon.ico")
# text_file1 = open("settings.txt", "r")
# text_value1 = text_file1.readlines()
# speed1 = 5

# tree = ET.parse("chzashp.xml")
# xmlroot = tree.getroot()
# defcol = str(text_value1[1])
# print(text_value1[1])
# text_file1.close()
# ###############################xml handling####################


class Xml:
    def __init__(self, filename, subsection):
        self.tree = Et.parse(filename)
        self.file_name = filename
        self.section = subsection
        self.xmlroot = self.tree.getroot()

    def read_xml(self, mode=None, returntype=None):
        for self.settings in self.xmlroot.findall(self.section):
            self.value = self.settings.find(mode).text
        print(self.value)
        return returntype(self.value)

    def write_xml(self, element, new_value):
        for self.element in self.xmlroot.iter(element):
            self.element.text = new_value
            self.tree.write(self.file_name)


# ##############################Draw Engine####################################

class DrawEngine:
    def custom(self, majestic, angle, dst, sides, poop1):
        self.a = 0
        t.speed(poop1)
        while self.a < sides:
            t.color(majestic)
            t.forward(dst)
            t.left(angle)
            self.a += 1

    def gvt(self, majestic, poop1):
        self.a = 0
        self.sides = 5
        t.speed(poop1)
        while (self.a < 5):
            t.color(majestic)
            t.forward(checks.check_dst(entry_3.get(), self.sides, False))
            t.left(72)
            t.write("nsa is watching you")
            self.a += 1

    def cube(self, majestic, poop1):
        self.a = 0
        self.sides = 9
        self.dst = checks.check_dst(entry_3.get(), self.sides, False)
        t.speed(poop1)
        t.color(majestic)
        while self.a < 5:
            t.forward(self.dst)
            if self.a != 4:
                t.left(90)
            self.a += 1
        t.left(45)
        t.forward(self.dst / 1.5)
        t.left(45)
        t.forward(self.dst)
        t.left(90)
        t.forward(self.dst)
        t.left(45)
        t.forward(self.dst / 1.5)
        t.speed(poop1 * 900)
        t.left(135)
        t.forward(self.dst)
        t.left(45)
        t.speed(poop1)
        t.forward(self.dst / 1.5)
        t.speed(poop1 * 900)
        t.left(180)
        t.forward(self.dst / 1.5)
        t.right(45)
        t.forward(self.dst)
        t.left(90)
        t.forward(self.dst)
        t.left(90)
        t.speed(poop1)

    def circle(self, speed=None, color=None, rad=None, **kwargs):
        for key, value in kwargs.items():
            print("%s = %s" % (key, value))
            setattr(self, key, value)
        t.color(color)
        t.speed(speed)
        t.circle(rad)


# ###############################Shape presets###############################################

def dist_draw(color, angle, sides, speed):
    dst = checks.check_dst(entry_3.get(), sides, False)
    draw.custom(color, angle, dst, sides, speed)


def square(color, speed):
    angle = 90
    sides = 4
    dist_draw(color, angle, sides, speed)


def hexagon(color, speed):
    angle = 60
    sides = 6
    dist_draw(color, angle, sides, speed)


def triangle(color, speed):
    angle = 120
    sides = 3
    dist_draw(color, angle, sides, speed)


def pentagon(color, speed):
    # majestic = entry_1.get()
    angle = 72
    sides = 5
    dist_draw(color, angle, sides, speed)


# ##########################################Checks and Defaults Checks###############################################
class Checks:
    def __init__(self, obj):
        print("defining object " + obj + " as class Checks")

    def check_dst(self, dst, sides, circle):
        self.dst = dst
        if self.dst == "":
            self.dst = xmlSettings.read_xml("distance", int)
        if chck1.get() == 1:
            if circle is True:
                self.dst = (float(self.dst) / pi) / 2  # radius for using distance as perimeter
            else:
                self.dst = float(self.dst) / sides
            print("distance = ", self.dst)
        if chck2.get() == 1:
            if circle is True:
                t.color("magenta")
                t.penup()
                t.goto(t.xcor() + int((xmlTemps.read_xml("temp1", int)) / 2), t.ycor())
                t.pendown()
                t.color(checks.check_short(entry_1.get()))
            else:
                float(self.dst)
                t.color("magenta")
                t.penup()
                t.goto(t.xcor() + int((xmlTemps.read_xml("temp1", int)) / 2 - (self.dst / 2)), t.ycor())
                t.pendown()
                t.color(checks.check_short(entry_1.get()))
        if chck3.get() == 1:
            if circle is True:
                if xmlTemps.read_xml("shape", str) == "circle":  # is and was a circle
                    float(self.dst)
                    t.color("magenta")
                    t.penup()
                    t.goto(t.xcor(), t.ycor() +
                           int(xmlTemps.read_xml("temp2", float) -
                               float(self.dst)))
                    t.pendown()
                    t.color(checks.check_short(entry_1.get()))
                else:  # is but wasnt a circle
                    t.color("magenta")
                    t.penup()
                    t.goto(t.xcor(), t.ycor() +
                           int(xmlTemps.read_xml("temp1", float) /
                               (2.0 * tan(pi / float(xmlTemps.read_xml("temp2", float)))))
                           - self.dst)
                    t.pendown()
                    t.color(checks.check_short(entry_1.get()))
            else:
                if xmlTemps.read_xml("shape", str) == "circle":  # isnt but was a circle
                    float(self.dst)
                    t.color("magenta")
                    t.penup()
                    t.goto(t.xcor(), t.ycor() +
                           int(xmlTemps.read_xml("temp2", float) -
                               float(self.dst) /
                               (2.0 * tan(pi / float(sides)))))
                    t.pendown()
                    t.color(checks.check_short(entry_1.get()))
                else:  # isnt and wasnt a circle (default(original formula))
                    float(self.dst)
                    t.color("magenta")
                    t.penup()
                    t.goto(t.xcor(), t.ycor() +
                           int(xmlTemps.read_xml("temp1", float) /
                               (2.0 * tan(pi / float(xmlTemps.read_xml("temp2", float)))) -
                               float(self.dst) /
                               (2.0 * tan(pi / float(sides)))))
                    t.pendown()
                    t.color(checks.check_short(entry_1.get()))
        if circle is True:
            xmlTemps.write_xml("temp1", "0")
            xmlTemps.write_xml("shape", "circle")
            xmlTemps.write_xml("temp2", str(int(self.dst)))
        else:
            xmlTemps.write_xml("temp1", str(int(self.dst)))
            xmlTemps.write_xml("shape", "nope")
            xmlTemps.write_xml("temp2", str(int(sides)))
        return float(self.dst)

    def check_speed(self, speed1):
        if speed1 == "":
            self.speed2 = xmlSettings.read_xml("speed", int)
        else:
            self.speed2 = entry_5.get()
        return int(self.speed2)

    def check_short(self, color):
        # majestic = entry_1.get()

        if color == "pl":
            self.color = "purple"

        elif color == "bl":
            self.color = "blue"

        elif color == "gr":
            self.color = "green"

        elif color == "rd":
            self.color = "red"

        elif color == "pk":
            self.color = "pink"

        elif color == "yl":
            self.color = "yellow"

        elif color == "eraser":
            self.color = "white"

        elif color == "mg":
            self.color = "magenta"
        elif color == "":
            # text_file1 = open("settings.txt", "r")
            # text_value1 = text_file1.readlines()
            # defcol = str(text_value1[1])
            # text_file1.close()
            # temp_file = open("temp.txt", "w")
            # temp_file.write(defcol)
            self.color = str(xmlSettings.read_xml("color", str))
            print(color)
        else:
            self.color = color
        return self.color

    def check_shape(self, event):  # ultimate check!
        try:
            print(listbx.lstbx_shape.get(ACTIVE))
            if listbx.lstbx_shape.get(ACTIVE) == "pentagon":
                pentagon(checks.check_short(entry_1.get()), checks.check_speed(entry_5.get()))
            elif listbx.lstbx_shape.get(ACTIVE) == "square":
                square(checks.check_short(entry_1.get()), checks.check_speed(entry_5.get()))
            elif listbx.lstbx_shape.get(ACTIVE) == "triangle":
                triangle(checks.check_short(entry_1.get()), checks.check_speed(entry_5.get()))
            elif listbx.lstbx_shape.get(ACTIVE) == "government":
                draw.gvt(checks.check_short(entry_1.get()), checks.check_speed(entry_5.get()))
            elif listbx.lstbx_shape.get(ACTIVE) == "cube":
                draw.cube(checks.check_short(entry_1.get()), checks.check_speed(entry_5.get()))
            elif listbx.lstbx_shape.get(ACTIVE) == "circle":
                draw.circle(color=checks.check_short(entry_1.get()), speed=checks.check_speed(entry_5.get()),
                            rad=checks.check_dst(entry_3.get(), 999, True))
            elif listbx.lstbx_shape.get(ACTIVE) == "hexagon":
                hexagon(checks.check_short(entry_1.get()), checks.check_speed(entry_5.get()))
        except ValueError:
            messagebox.showerror("ValueError",
                                 "Value Error\n  (Try converting values for  \ndistance or speed to integers)",
                                 parent=root, )


# #######################################custom event#########################################################
def custom1(event):
    try:
        if slide_sides.get() != 0:
            sides = slide_sides.get()
        else:
            sides = entry_4.get()
        angle = entry_2.get()
        distance = checks.check_dst(entry_3.get(), int(sides), False)
        if angle == "":
            angle = 360 / int(sides)
            print("angle = ", angle)
        draw.custom(checks.check_short(entry_1.get()), float(angle), float(distance), int(sides),
                    checks.check_speed(entry_5.get()))
    except ValueError:
        messagebox.showerror("ValueError", "Value Error\n(Try adding a value for sides)",
                             parent=root, )


# ##########################################Turtle Events##########################################

class TurtleEvents:
    def __init__(self, increments=50):
        self.increments = increments

    def Continue(self, event):
        self.stop = True
        t.pendown()

    def clear1(self, event):
        t.clear()

    def reset1(self, event):
        t.reset()

    def repos1(self, event):
        t.penup()
        t.speed(999)
        t.goto(0, 0)
        t.speed(checks.check_speed(entry_5.get()))
        t.pendown()

    def moveUp(self, event):
        self.stop = False
        t.penup()
        while self.stop is False:
            t.color("magenta")
            t.goto(t.xcor(), t.ycor() + self.increments)
            t.color(checks.check_short(entry_1.get()))

    def moveDown(self, event):
        self.stop = False
        t.penup()
        while self.stop is False:
            t.color("magenta")
            t.goto(t.xcor(), t.ycor() - self.increments)
            t.color(checks.check_short(entry_1.get()))

    def moveLeft(self, event):
        self.stop = False
        t.penup()
        while self.stop is False:
            t.color("magenta")
            t.goto(t.xcor() - self.increments, t.ycor())
            t.color(checks.check_short(entry_1.get()))

    def moveRight(self, event):
        self.stop = False
        t.penup()
        while self.stop is False:
            t.color("magenta")
            t.goto(t.xcor() + self.increments, t.ycor())
            t.color(checks.check_short(entry_1.get()))


# ############################################Settings Window######################################################

def settingsWin(event):
    if settings.setted is False:
        settings.set()
        settings.render()
        settings.master.lift ()
    else:
        settings.master.lift ()
    settings.master.call("wm", "attributes", ".", "-topmost", True)
    settings.master.after_idle(settings.master.call, "wm", "attributes", ".", "-topmost", False)

class SettingsWindow:
    def __init__(self):
        self.setted = False

    def set(self):
        self.setted = True
        self.title = "advanced settings"
        self.master = Tk()
        self.frame_color = xmlSettings.read_xml("framecol", str)
        self.frame_st = Frame(self.master, bg=self.frame_color)
        self.entry_st = Entry(self.frame_st)
        self.label_st = Label(self.frame_st, text="change xml file values:", bg=self.frame_color)
        self.button_st = Button(self.frame_st, text="set default color")
        self.button_st.bind("<Button-1>", self.poop2)
        self.button_st2 = Button(self.frame_st, text="set default speed")
        self.button_st2.bind("<Button-1>", self.poop4)
        self.button_st3 = Button(self.frame_st, text="set default distance")
        self.button_st3.bind("<Button-1>", self.poop6)
        self.label_st2 = Label(self.frame_st, text="this changes the xml values\nin the chzashp.xml file",
                               bg=self.frame_color)

    def close(self):
        self.setted = False
        self.master.destroy()

    def poop6(self, event):
        xmlSettings.write_xml("distance", self.entry_st.get())

    def poop2(self, event):
        xmlSettings.write_xml("color", self.entry_st.get())

    def poop4(self, event):
        xmlSettings.write_xml("speed", self.entry_st.get())

    def render(self):
        self.master.title(self.title)
        self.frame_st.pack(expand=TRUE)
        self.master.title("advanced settings")
        self.label_st.pack()
        self.entry_st.pack()
        self.button_st.bind("<Button-1>", self.poop2)
        self.button_st.pack()
        self.button_st2.bind("<Button-1>", self.poop4)
        self.button_st2.pack()
        self.button_st3.bind("<Button-1>", self.poop6)
        self.button_st3.pack()
        self.label_st2.pack()
        self.master.bind("<Pause>", lambda e: self.master.destroy())
        self.master.bind("<Escape>", lambda e: self.master.destroy())
        self.master.protocol("WM_DELETE_WINDOW", self.close)
        # self.check_box


# #########################search and list engine#################################
class ListBox:
    def __init__(self, listforbx):
        self.lstbx_list = listforbx

    def updateList(self):
        self.search_term = self.searchvar.get()
        # Just a list to populate the listbox
        # self.lstbx_list = ["pentagon", "square", "triangle", "government", "cube", "circle"]
        self.lstbx_shape.delete(0, END)
        for self.shape in self.lstbx_list:
            if self.search_term.lower() in self.shape.lower():
                self.lstbx_shape.insert(END, self.shape)
        if self.searchvar.get() != "":
            self.lstbx_shape.selection_set(0)

    def main(self):
        self.frame_shape = LabelFrame(root, text="shape presets")
        self.frame_shape.grid(row=0, column=2, rowspan=5)

        self.scrl_shape = Scrollbar(self.frame_shape)
        self.lstbx_shape = Listbox(self.frame_shape, height=4, yscrollcommand=self.scrl_shape.set)

        self.searchvar = StringVar()
        self.searchvar.trace("w", lambda name, index, mode: self.updateList())
        self.searchentry = Entry(self.frame_shape, textvariable=self.searchvar)
        # self.lstbx_list = ["pentagon", "square", "triangle", "government", "cube", "circle"]
        # for self.shape in self.lstbx_list:
        # self.lstbx_shape.insert(END, self.shape)
        self.updateList()  #populate list
        self.searchentry.grid()
        self.lstbx_shape.grid()
        self.scrl_shape.grid(row=1, column=2, sticky=N + S)
        self.scrl_shape.config(command=self.lstbx_shape.yview)

        self.button_draw = Button(self.frame_shape, text="draw")
        self.button_draw.bind("<Button-1>", checks.check_shape)
        self.button_draw.grid()


# ###############################################defining check button variables###############################################
def prnt():
    print(chck1.get())


def prnt2():
    print(chck2.get())


def prnt3():
    print(chck3.get())


def slide1(event):
    print(slide_sides.get())

# ###############################################window close handling###############################################


# or toplevel.protocol(...

def handler(event):
    if messagebox.askokcancel("Quit?", "Are you sure you want to quit?"):
        quit()

root.protocol("WM_DELETE_WINDOW", lambda :handler(None))

# ###############################################start executables###############################################
chck1 = IntVar()
chck2 = IntVar()
chck3 = IntVar()
chck4 = IntVar()
slide_sides = IntVar()

# ########################################defining objects#######################################
draw = DrawEngine()
xmlSettings = Xml("chzashp.xml", "defaults")
xmlTemps = Xml("chzashp.xml", "temporaries")# defines object and Opens Defaults section in xml file
checks = Checks("checks")
event = TurtleEvents(increments=xmlSettings.read_xml(mode="increments", returntype=int))
settings = SettingsWindow()
listbx = ListBox(["pentagon", "square", "triangle", "government", "cube", "circle", "hexagon"])
# defines object and Defines the list for the preset menu
# ################################################setting turtle canvas###############################################
canvas = ScrolledCanvas(root)
canvas.grid(row=10, columnspan=3)
screen = TurtleScreen(canvas)
screen.screensize(1000, 1000)
t = RawTurtle(screen)
# t.hideturtle()
# ################################################key bindings###############################################
# t.circle(100)
root.bind("<Escape>", handler)
root.bind("<Pause>", lambda e: quit())
root.bind("<Right>", event.moveRight)
root.bind("<KeyRelease-Right>", event.Continue)
root.bind("<Left>", event.moveLeft)
root.bind("<KeyRelease-Left>", event.Continue)
root.bind("<Up>", event.moveUp)
root.bind("<KeyRelease-Up>", event.Continue)
root.bind("<Down>", event.moveDown)
root.bind("<KeyRelease-Down>", event.Continue)

# ################################################main###############################################

root.title("Chooz-a-Shayp beta 8")
label_1 = Label(root, text="Chose a color")
entry_1 = Entry(root)
label_2 = Label(root, text="Chose an angle")
entry_2 = Entry(root)
label_3 = Label(root, text="Chose a distance")
entry_3 = Entry(root)
label_4 = Label(root, text="Chose sides")
entry_4 = Entry(root)
label_5 = Label(root, text="speed")
entry_5 = Entry(root)


button_5 = Button(root, text="custom", width=10)
button_5.bind("<Button-1>", custom1)
button_5.grid(row=5, column=1)

button_up = Button(root, text="up", width=3)
button_down = Button(root, text="down", width=3)
button_left = Button(root, text="left", width=4)
button_right = Button(root, text="right", width=4)
button_set = Button(root, text="settings")

button_up.bind("<Button-1>", event.moveUp)
button_up.bind("<ButtonRelease-1>", event.Continue)
button_down.bind("<Button-1>", event.moveDown)
button_down.bind("<ButtonRelease-1>", event.Continue)
button_left.bind("<Button-1>", event.moveLeft)
button_left.bind("<ButtonRelease-1>", event.Continue)
button_right.bind("<Button-1>", event.moveRight)
button_right.bind("<ButtonRelease-1>", event.Continue)
button_set.bind("<Button-1>", settingsWin)

label_1.grid(row=0, sticky=E)
entry_1.grid(row=0, column=1)
label_2.grid(row=1, sticky=E)
entry_2.grid(row=1, column=1)
label_3.grid(row=2, sticky=E)
entry_3.grid(row=2, column=1)
label_4.grid(row=3, sticky=E)
entry_4.grid(row=3, column=1)
label_5.grid(row=4, sticky=E)
entry_5.grid(row=4, column=1)
button_up.grid(row=6, column=1)
button_left.grid(row=7, column=1, sticky=W)
button_right.grid(row=7, column=1, sticky=E)
button_down.grid(row=8, column=1)
button_set.grid(row=5, column=0)

frame_sides = LabelFrame(root, text="sides")
frame_sides.grid(row=6, column=0, rowspan=2)
slider_sides = Scale(frame_sides, variable=slide_sides, command=slide1, orient=HORIZONTAL, to=50)
slider_sides.grid()

# #########################search and list engine#################################

listbx.main()
# ##########################advanced frame#######################################

frame_check = LabelFrame(root, bd=2, text="advanced")
frame_check.grid(row=5, column=2, rowspan=4)
check_box = Checkbutton(frame_check, text="set distance\nas perimeter"
                        , variable=chck1, command=prnt, justify=LEFT, width=10)
check_box.grid(sticky=W)
check_box2 = Checkbutton(frame_check, text="use center x"
                         , variable=chck2, command=prnt2, justify=LEFT, width=10)
check_box2.grid(sticky=W)
check_box3 = Checkbutton(frame_check, text="use center y"
                         , variable=chck3, command=prnt3, justify=LEFT, width=10)
check_box3.grid(sticky=W)

button_reset = Button(frame_check, text="reset", bg="red", fg="white", activebackground="pink", height=0, width=6)
button_reset.bind("<Button-1>", event.reset1)
button_reset.grid(row=0, column=1)

button_clear = Button(frame_check, text="clear", bg="red", fg="white", activebackground="pink", height=1, width=6)
button_clear.bind("<Button-1>", event.clear1)
button_clear.grid(row=1, column=1)

button_repos = Button(frame_check, text="reset pos", bg="red", fg="white", activebackground="pink", height=1, width=6)
button_repos.bind("<Button-1>", event.repos1)
button_repos.grid(row=2, column=1)

# #############################################advanced###########################################
def open_adv(event):
    def open():
        global hidden
        # hidden = 0
        # label_6 = Label(frame_adv, text="turtle command strart\n with t.\nex.:t.color('red')", bg="orange")
        label_6.grid()
        # entry_6 = Entry(frame_adv)
        entry_6.grid()

        # button_adv = Button(frame_adv, text="execute")
        button_adv.bind("<Button-1>", lambda e:exec(entry_6.get()))
        button_adv.grid()
        hidden = 0

    def hide():
        global hidden
        label_6.grid_forget()
        entry_6.grid_forget()
        button_adv.grid_forget()
        hidden = 1

    if hidden == 0: hide()
    elif hidden == 1: open()

hidden = 1

frame_adv = LabelFrame(root, bd=2, text="advanced...")
frame_adv.grid(row=8, column=0, rowspan=2)
frame_adv.bind("<Button-1>", open_adv)

label_dum = Label(frame_adv, text="")
label_dum.grid()

label_6 = Label(frame_adv, text="turtle command strart\n with t.\nex.:t.color('red')", bg="orange")
entry_6 = Entry(frame_adv)
button_adv = Button(frame_adv, text="execute")
button_adv.bind("<Button-1>", lambda e:exec(entry_6.get()))

# superu=input("Choose a shape: ")

mainloop()

# input()