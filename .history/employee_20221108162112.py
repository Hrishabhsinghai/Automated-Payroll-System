from tkinter import*
class EmployeeSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Payroll Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title = Label(self.root, text="Payroll Management System",
        font=("Microsoft JhengHei",30,"bold")
        ,bg="#404040",fg="white",padx=20).place(x=0,y=0,relwidth=1)
  
    #----------------------------Frame1----------------------------------
        Frame1 = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=750,height=620)
        title2=Label(Frame1,text="Employee Details",
        font=("times new roman",20,)
        ,bg="#686868",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_code = Label(Frame1,text="Designation",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=120)

        text_code = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=225,y=74,width=200)
  
        btn_search = Button(Frame1,text="Search",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=440,y=70,height=30)

        lbl_code = Label(Frame1,text="Employee Code",
        font=("times new roman",20,)
        ,bg="white",fg="black").place(x=10,y=70)

        lbl_designation = Label(Frame1,text="Designation",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=120)

        text_designation = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=150,y=125,width=200)

        lbl_DOB = Label(Frame1,text="D.O.B",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=120,)

        text_DOB = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=450,y=125)

        lbl_Name = Label(Frame1,text="Name",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=170)

        text_Name = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=150,y=175,width=200)

        lbl_DOJ = Label(Frame1,text="D.O.J",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=170,)

        text_DOJ = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=450,y=175)

        lbl_Experience = Label(Frame1,text="Experience",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=220)

        text_Experience = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=150,y=225,width=200)

        lbl_Age = Label(Frame1,text="Age",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=220,)

        text_Age = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=450,y=225)

        lbl_Gender = Label(Frame1,text="Gender",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=270)

        text_Gender = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=150,y=275,width=200)

        lbl_Proof = Label(Frame1,text="ID Prof.",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=270)

        text_Proof = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=450,y=275)

        lbl_Email = Label(Frame1,text="E-mail",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=320)

        text_Email = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=150,y=325,width=200)

        lbl_Contact = Label(Frame1,text="Ph. No.",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=320)

        text_Contact = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=450,y=325)

        lbl_hired = Label(Frame1,text="Hired Location",
        font=("times new roman",17)
        ,bg="white",fg="black").place(x=10,y=372)

        text_hired = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=150,y=375,width=200)

        lbl_Status = Label(Frame1,text="Status",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=370)

        text_Status = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=450,y=375)

        lbl_Address = Label(Frame1,text="Address",
        font=("times new roman",17)
        ,bg="white",fg="black").place(x=10,y=422)

        text_Address = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=150,y=425,width=505,height=100)
   
    #--------------------------Frame2------------------------------------
        Frame2 = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=580,height=300)

        title3=Label(Frame2,text="Employee Salary Details",
        font=("times new roman",20,)
        ,bg="#686868",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_month = Label(Frame2,text="Month",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=10,y=60)

        text_month = Entry(Frame2,
        font=("times new roman",18)
        ,bg="lightyellow",fg="black").place(x=90,y=62,width=100)

        lbl_year = Label(Frame2,text="Year",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=210,y=60)

        text_year = Entry(Frame2,
        font=("times new roman",18)
        ,bg="lightyellow",fg="black").place(x=270,y=62,width=100)

        lbl_salary = Label(Frame2,text="Salary",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=380,y=60)

        text_salary = Entry(Frame2,
        font=("times new roman",18)
        ,bg="lightyellow",fg="black").place(x=460,y=62,width=100)  
        # btn_search = Button(Frame2,text="Search",
        # font=("times new roman",20)
        # ,bg="white",fg="black").place(x=440,y=70,height=30)

        # lbl_code = Label(Frame2,text="Employee Code",
        # font=("times new roman",20,)
        # ,bg="white",fg="black").place(x=10,y=70)

        lbl_totaldays = Label(Frame2,text="Total Days",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=10,y=120)

        text_totaldays = Entry(Frame2,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=170,y=120,width=100)

        lbl_Absents = Label(Frame2,text="Absents",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=300,y=120,)

        text_Absents = Entry(Frame2,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=420,y=120,width=100)

        lbl_Medical = Label(Frame2,text="Medical",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=10,y=150)

        text_Medical = Entry(Frame2,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=170,y=150, width=100)

        lbl_pf = Label(Frame2,text="PF",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=300,y=150,)

        text_pf = Entry(Frame2,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=420,y=150,width=100)

        lbl_convence = Label(Frame2,text="Convence",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=10,y=180)

        text_convence = Entry(Frame2,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=170,y=180, width=100)

        lbl_netsalary = Label(Frame2,text="Net Salary",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=300,y=180,)

        text_netsalary = Entry(Frame2,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black").place(x=420,y=180,width=100)

        btn_Calculate = Button(Frame2,text="Calculate",
        font=("times new roman",20)
        ,bg="orange",fg="white").place(x=150,y=240,height=30,width=120)

        btn_add = Button(Frame2,text="Add",
        font=("times new roman",20)
        ,bg="green",fg="white").place(x=285,y=240,height=30,width=120)

        btn_clear = Button(Frame2,text="clear",
        font=("times new roman",20)
        ,bg="grey",fg="black").place(x=420,y=240,height=30,width=120)
    #--------------------------Frame3------------------------------------

        Frame3 = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,width=580,height=310)

    #=======================calculator frame=============================

    Cal_Frame = Frame(Frame3,bg="white",bd=2,relief=RIDGE)
    Cal_Frame.place(x=5,y=5,width=400,height=305)
    txt_Result=Entry(Cal_Frame,bg="lightyellow", font=("times new roman",20,"bold"))
    txt_Result.place(x=0,y=0,relwidth=1,height=40)

root = Tk()
obj=EmployeeSystem(root)
root.mainloop()
