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

        self.var_code = StringVar()
        self.var_designation = StringVar()
        self.var_DOB = StringVar()
        self.var_DOJ = StringVar()
        self.var_Experience = StringVar()
        self.var_Age = StringVar()
        self.var_Gender = StringVar()
        self.var_proof = StringVar()
        self.var_Email = StringVar()
        self.var_Contact = StringVar()
        self.var_hired = StringVar()
        self.var_Status = StringVar()
        self.var_Name = StringVar()




        Frame1 = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=750,height=620)
        title2=Label(Frame1,text="Employee Details",
        font=("times new roman",20,)
        ,bg="#686868",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_code = Label(Frame1,text="Designation",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=120)

        text_code = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_code
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
        font=("times new roman",15),textvariable=self.var_designation
        ,bg="lightyellow",fg="black").place(x=150,y=125,width=200)

        lbl_DOB = Label(Frame1,text="D.O.B",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=120,)

        text_DOB = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_DOB
        ,bg="lightyellow",fg="black").place(x=450,y=125)

        lbl_Name = Label(Frame1,text="Name",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=170)

        text_Name = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_Name
        ,bg="lightyellow",fg="black").place(x=150,y=175,width=200)

        lbl_DOJ = Label(Frame1,text="D.O.J",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=170,)

        text_DOJ = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_DOJ
        ,bg="lightyellow",fg="black").place(x=450,y=175)

        lbl_Experience = Label(Frame1,text="Experience",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=220)

        text_Experience = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_Experience
        ,bg="lightyellow",fg="black").place(x=150,y=225,width=200)

        lbl_Age = Label(Frame1,text="Age",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=220,)

        text_Age = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_Age
        ,bg="lightyellow",fg="black").place(x=450,y=225)

        lbl_Gender = Label(Frame1,text="Gender",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=270)

        text_Gender = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_Gender
        ,bg="lightyellow",fg="black").place(x=150,y=275,width=200)

        lbl_proof = Label(Frame1,text="ID Prof.",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=270)

        text_proof = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_proof
        ,bg="lightyellow",fg="black").place(x=450,y=275)

        lbl_Email = Label(Frame1,text="E-mail",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=320)

        text_Email = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_Email
        ,bg="lightyellow",fg="black").place(x=150,y=325,width=200)

        lbl_Contact = Label(Frame1,text="Ph. No.",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=320)

        text_Contact = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_Contact
        ,bg="lightyellow",fg="black").place(x=450,y=325)

        lbl_hired = Label(Frame1,text="Hired Location",
        font=("times new roman",17)
        ,bg="white",fg="black").place(x=10,y=372)

        text_hired = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_hired
        ,bg="lightyellow",fg="black").place(x=150,y=375,width=200)

        lbl_Status = Label(Frame1,text="Status",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=360,y=370)

        text_Status = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_Status
        ,bg="lightyellow",fg="black").place(x=450,y=375)

        lbl_address = Label(Frame1,text="Address",
        font=("times new roman",17)
        ,bg="white",fg="black").place(x=10,y=422)

        self.txt_address = Entry(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black")
        self.txt_address.place(x=150,y=425,width=505,height=100)
   
    #--------------------------Frame2------------------------------------
       

        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_totaldays = StringVar()
        self.var_Absents = StringVar()
        self.var_Medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_netsalary = StringVar()

        Frame2 = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=580,height=300)

        title3=Label(Frame2,text="Employee Salary Details",
        font=("times new roman",20,)
        ,bg="#686868",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_month = Label(Frame2,text="Month",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=10,y=60)

        text_month = Entry(Frame2,
        font=("times new roman",18),textvariable=self.var_month
        ,bg="lightyellow",fg="black").place(x=90,y=62,width=100)

        lbl_year = Label(Frame2,text="Year",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=210,y=60)

        text_year = Entry(Frame2,
        font=("times new roman",18),textvariable=self.var_year
        ,bg="lightyellow",fg="black").place(x=270,y=62,width=100)

        lbl_salary = Label(Frame2,text="Salary",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=380,y=60)

        text_salary = Entry(Frame2,
        font=("times new roman",18),textvariable=self.var_salary
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
        font=("times new roman",15),textvariable=self.var_totaldays
        ,bg="lightyellow",fg="black").place(x=170,y=120,width=100)

        lbl_Absents = Label(Frame2,text="Absents",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=300,y=120,)

        text_Absents = Entry(Frame2,
        font=("times new roman",15),textvariable=self.var_Absents
        ,bg="lightyellow",fg="black").place(x=420,y=120,width=100)

        lbl_Medical = Label(Frame2,text="Medical",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=10,y=150)

        text_Medical = Entry(Frame2,
        font=("times new roman",15),textvariable=self.var_Medical
        ,bg="lightyellow",fg="black").place(x=170,y=150, width=100)

        lbl_pf = Label(Frame2,text="PF",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=300,y=150,)

        text_pf = Entry(Frame2,
        font=("times new roman",15),textvariable=self.var_pf
        ,bg="lightyellow",fg="black").place(x=420,y=150,width=100)

        lbl_convence = Label(Frame2,text="Convence",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=10,y=180)

        text_convence = Entry(Frame2,
        font=("times new roman",15),textvariable=self.var_convence
        ,bg="lightyellow",fg="black").place(x=170,y=180, width=100)

        lbl_netsalary = Label(Frame2,text="Net Salary",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=300,y=180,)

        text_netsalary = Entry(Frame2,
        font=("times new roman",15),textvariable=self.var_netsalary
        ,bg="lightyellow",fg="black").place(x=420,y=180,width=100)

        btn_Calculate = Button(Frame2,text="Calculate",command=self.calculate,
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

        self.var_text=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_text.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_text.set(res)
            self.var_operator='' 

        def clear_cal():
            self.var_text.set('')
            self.var_operator='' 


        Cal_Frame = Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        Cal_Frame.place(x=2,y=2,width=247,height=300)

        txt_Result=Entry(Cal_Frame,bg="lightyellow",textvariable=self.var_text,font=("times new roman",20,"bold"),justify=RIGHT)
        txt_Result.place(x=0,y=0,relwidth=1,height=50)

        btn_7=Button(Cal_Frame,text='7',command=lambda:btn_click(7),font=("italic",15,"bold")).place(x=0,y=52,w=60,h=60)
        btn_8=Button(Cal_Frame,text='8',command=lambda:btn_click(8),font=("italic",15,"bold")).place(x=61,y=52,w=60,h=60)
        btn_9=Button(Cal_Frame,text='9',command=lambda:btn_click(9),font=("italic",15,"bold")).place(x=122,y=52,w=60,h=60)
        btn_div=Button(Cal_Frame,text='/',command=lambda:btn_click('/'),font=("italic",15,"bold")).place(x=183,y=52,w=60,h=60)

        btn_4=Button(Cal_Frame,text='4',command=lambda:btn_click(4),font=("italic",15,"bold")).place(x=0,y=112,w=60,h=60)
        btn_5=Button(Cal_Frame,text='5',command=lambda:btn_click(5),font=("italic",15,"bold")).place(x=61,y=112,w=60,h=60)
        btn_6=Button(Cal_Frame,text='6',command=lambda:btn_click(6),font=("italic",15,"bold")).place(x=122,y=112,w=60,h=60)
        btn_mul=Button(Cal_Frame,text='*',command=lambda:btn_click('*'),font=("italic",15,"bold")).place(x=183,y=112,w=60,h=60)

        btn_1=Button(Cal_Frame,text='1',command=lambda:btn_click(1),font=("italic",15,"bold")).place(x=0,y=172,w=60,h=60)
        btn_2=Button(Cal_Frame,text='2',command=lambda:btn_click(2),font=("italic",15,"bold")).place(x=61,y=172,w=60,h=60)
        btn_3=Button(Cal_Frame,text='3',command=lambda:btn_click(3),font=("italic",15,"bold")).place(x=122,y=172,w=60,h=60)
        btn_sub=Button(Cal_Frame,text='-',command=lambda:btn_click('-'),font=("italic",15,"bold")).place(x=183,y=172,w=60,h=60)

        btn_0=Button(Cal_Frame,text='0',command=lambda:btn_click(0),font=("italic",15,"bold")).place(x=0,y=232,w=60,h=60)
        btn_dot=Button(Cal_Frame,text='C',command=clear_cal,font=("italic",15,"bold")).place(x=61,y=232,w=60,h=60)
        btn_add=Button(Cal_Frame,text='+',command=lambda:btn_click('+'),font=("italic",15,"bold")).place(x=122,y=232,w=60,h=60)
        btn_equal=Button(Cal_Frame,text='=',command=result,font=("italic",15,"bold")).place(x=183,y=232,w=60,h=60)

        #================Salary frame=================================
        sal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_Frame.place(x=251,y=2,width=322,height=300)
        title_sal=Label(sal_Frame,text="Salary Reciept",
        font=("times new roman",20,)
        ,bg="#686868",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        sal_Frame2 = Frame(sal_Frame,bg='white',bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)

        scroll_y = Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_recipt = Text(sal_Frame2,font=("times new roman",15),bg='lightyellow',yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)

        btn_print = Button(sal_Frame,text="Print",
        font=("times new roman",20)
        ,bg="lightblue",fg="white").place(x=180,y=262,height=30,width=120)
    
    def calculate(self):
        #============Frame1 variables===============
        print(self.var_code.get(),
        self.var_designation.get(),
        self.var_DOB.get(),
        self.var_DOJ.get(),
        self.var_Experience.get(),
        self.var_Age.get(),
        self.var_Gender.get(),
        self.var_proof.get(),
        self.var_Email.get(),
        self.var_Contact.get(),
        self.var_hired.get(),
        self.var_Status.get(),
        self.var_Name.get(),
        #=============Frame2 variable===============  
        self.var_month.get(),
        self.var_year.get(),
        self.var_salary.get(),
        self.var_totaldays.get(),
        self.var_Absents.get(),
        self.var_Medical.get(),
        self.var_pf.get(),
        self.var_convence.get(),
        self.var_netsalary.get(),
        self.txt_address.get('1.0',END)
        )

root = Tk()
obj=EmployeeSystem(root)
root.mainloop()
