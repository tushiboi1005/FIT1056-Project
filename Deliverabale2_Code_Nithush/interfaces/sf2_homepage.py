import tkinter as tk

class Homepage(tk.Frame):
    def __init__(self, master, image_path):
        """
        Constructor for the HomePage class.

        Parameter(s):
        - master: master widget of this widget instance
        - image_path: str, path of the logo image file
        """
        super().__init__(master=master)
        self.master = master
        self.image_path = image_path

        # self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        # self.logo_label = tk.Label(master=self, image=self.logo_photoimage, width=128, height=128)
        # self.logo_label.place(x=0,y=0,relwidth=1,relheight=1)

        self.welcome = tk.Label(master=self,font="Arial",text="Welcome to EmpowerU!!!",bg="yellow")
        self.welcome.place(relx=0.4,rely=0.6,relwidth=0.3,relheight=0.1)

        self.learner_login =tk.Button(master=self, text="Learner login")
        self.learner_login.place(relx=0.3,rely=0.4,relwidth=0.1,relheight=0.05)
        self.tutor_login =tk.Button(master=self, text="Tutor login")
        self.tutor_login.place(relx=0.5,rely=0.4,relwidth=0.1,relheight=0.05)
        self.admin_login =tk.Button(master=self, text="Admin login")
        self.admin_login.place(relx=0.7,rely=0.4,relwidth=0.1,relheight=0.05)



    def llogin(self):
        pass
    def tlogin(self):
        pass
    def alogin(self):
        None