import tkinter as tk

from sf2_homepage import Homepage

class EmpowerU(tk.Tk):
    def __init__(self,title,width,height,color):
        super().__init__()
        super().title(title)
        super().geometry(f"{width}x{height}")
        super().configure(bg=color)

        self.homepage = Homepage(master=self, image_path="./images/logo.png")
        self.show_homepage()

    def show_homepage(self):
        self.homepage.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_homepage(self):
        self.homepage.place_forget()




root = EmpowerU(title="EmpowerU System", width=750, height=500,color="orange")
root.mainloop()