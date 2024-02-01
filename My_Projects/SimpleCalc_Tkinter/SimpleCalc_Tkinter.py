from tkinter import *


class Calc:

    def __init__(self):

        self.window = Tk()
        self.window.title("Calc")
        self.window.resizable(0, 0)
        # self.window.config(bg="#1d2f38")

        self.screen_numbers = Entry(
            self.window, font="Arial 20 bold", bg="#273f47", fg="white", width=26)
        self.screen_numbers.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        self.button_1 = Button(self.frame, bg="dark orange", bd=0,
                               text="1", font="Arial 20 bold", fg="White", width=5, height=2, command=lambda: self.touch("1"))

        self.button_2 = Button(self.frame, bg="dark orange", bd=0,
                               text="2", font="Arial 20 bold", fg="White", width=5, height=2, command=lambda: self.touch("2"))

        self.button_3 = Button(self.frame, bg="dark orange", bd=0,
                               text="3", font="Arial 20 bold", fg="White", width=5, height=2, command=lambda: self.touch("3"))

        self.button_4 = Button(self.frame, bg="dark orange", bd=0,
                               text="4", font="Arial 20 bold", fg="White", width=5, height=2, command=lambda: self.touch("4"))

        self.button_5 = Button(self.frame, bg="dark orange", bd=0,
                               text="5", font="Arial 20 bold", fg="White", width=5, height=2, command=lambda: self.touch("5"))

        self.button_6 = Button(self.frame, bg="dark orange", bd=0,
                               text="6", font="Arial 20 bold", fg="White", width=5, height=2, command=lambda: self.touch("6"))

        self.button_7 = Button(self.frame, bg="dark orange", bd=0,
                               text="7", font="Arial 20 bold", fg="White", width=5, height=2, command=lambda: self.touch("7"))

        self.button_8 = Button(self.frame, bg="dark orange", bd=0,
                               text="8", font="Arial 20 bold", fg="White", width=5, height=2, command=lambda: self.touch("8"))

        self.button_9 = Button(self.frame, bg="dark orange", bd=0,
                               text="9", font="Arial 20 bold", fg="White", width=5, height=2, command=lambda: self.touch("9"))

        self.button_0 = Button(self.frame, bg="dark orange", bd=0,
                               text="0", font="Arial 20 bold", fg="white", width=5, height=2, command=lambda: self.touch("0"))

        self.button_div = Button(self.frame, bg="dark orange", bd=0,
                                 text="/", font="Arial 20 bold", fg="white", width=5, height=2, command=lambda: self.touch("/"))

        self.button_mul = Button(self.frame, bg="dark orange", bd=0,
                                 text="*", font="Arial 20 bold", fg="white", width=5, height=2, command=lambda: self.touch("*"))

        self.button_sub = Button(self.frame, bg="dark orange", bd=0,
                                 text="-", font="Arial 20 bold", fg="white", width=5, height=2, command=lambda: self.touch("-"))

        self.button_add = Button(self.frame, bg="dark orange", bd=0,
                                 text="+", font="Arial 20 bold", fg="white", width=5, height=2, command=lambda: self.touch("+"))

        self.button_equal = Button(self.frame, bg="dark orange", bd=0,
                                   text="=", font="Arial 20 bold", fg="white", width=5, height=2, command=self.total)

        self.button_dot = Button(self.frame, bg="dark orange", bd=0,
                                 text=".", font="Arial 20 bold", fg="white", width=5, height=2, command=lambda: self.touch("."))

        self.button_clean = Button(self.frame, bg="dark orange", bd=0,
                                   text="C", font="Arial 20 bold", fg="white", width=11, height=2, command=self.Clean)

        self.button_rewind = Button(self.frame, bg="dark orange", bd=0,
                                    text="<=", font="Arial 20 bold", fg="white", width=11, height=2, command=self.Rewind)

        self.button_1.grid(row=0, column=0, padx=2, pady=2)
        self.button_2.grid(row=0, column=1, padx=2, pady=2)
        self.button_3.grid(row=0, column=2, padx=2, pady=2)
        self.button_4.grid(row=1, column=0, padx=2, pady=2)
        self.button_5.grid(row=1, column=1, padx=2, pady=2)
        self.button_6.grid(row=1, column=2, padx=2, pady=2)
        self.button_7.grid(row=2, column=0, padx=2, pady=2)
        self.button_8.grid(row=2, column=1, padx=2, pady=2)
        self.button_9.grid(row=2, column=2, padx=2, pady=2)
        self.button_0.grid(row=3, column=1, padx=2, pady=2)
        self.button_div.grid(row=0, column=3, padx=2, pady=2)
        self.button_mul.grid(row=1, column=3, padx=2, pady=2)
        self.button_sub.grid(row=2, column=3, padx=2, pady=2)
        self.button_add.grid(row=3, column=3, padx=2, pady=2)
        self.button_equal.grid(row=3, column=2, padx=2, pady=2)
        self.button_dot.grid(row=3, column=0, padx=2, pady=2)
        self.button_clean.grid(row=4, column=0, columnspan=2, padx=2)
        self.button_rewind.grid(row=4, column=2, columnspan=2, padx=2)

        self.window.mainloop()

    def touch(self, num):
        self.screen_numbers.insert(END, num)

    def Clean(self):
        self.screen_numbers.delete(0, END)

    def total(self):
        res = eval(self.screen_numbers.get())
        self.screen_numbers.delete(0, END)
        self.screen_numbers.insert(0, str(res))

    def Rewind(self):
        current_content = self.screen_numbers.get()

        if current_content:
            updated_content = current_content[:-1]

            self.screen_numbers.delete(0, END)
            self.screen_numbers.insert(0, updated_content)


Calc()
