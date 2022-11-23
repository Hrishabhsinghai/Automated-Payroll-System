from tkinter import*
from tkinter import messagebox
import pymysql #pip install pymysql
import time
  
class EmployeeSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Automated Payroll System | By Hrishabh")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title = Label(self.root, text="Automated Payroll System",
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
        self.var_name = StringVar()

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
  
        btn_search = Button(Frame1,text="Search",command=self.search,
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

        lbl_name = Label(Frame1,text="name",
        font=("times new roman",20)
        ,bg="white",fg="black").place(x=10,y=170)

        text_name = Entry(Frame1,
        font=("times new roman",15),textvariable=self.var_name
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

        self.txt_address = Text(Frame1,
        font=("times new roman",15)
        ,bg="lightyellow",fg="black")
        self.txt_address.place(x=150,y=425,width=505,height=100)
   
    #--------------------------Frame2------------------------------------
       
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_totaldays = StringVar()
        self.var_absent = StringVar()
        self.var_Medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_net_salary = StringVar()

        Frame2 = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=580,height=300)

        title3=Label(Frame2,text="Employee salary Details",
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

        lbl_salary = Label(Frame2,text="salary",
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

        lbl_absent = Label(Frame2,text="absent",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=300,y=120,)

        text_absent = Entry(Frame2,
        font=("times new roman",15),textvariable=self.var_absent
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

        lbl_net_salary = Label(Frame2,text="Net salary",
        font=("times new roman",18)
        ,bg="white",fg="black").place(x=300,y=180,)

        text_net_salary = Entry(Frame2,
        font=("times new roman",15),textvariable=self.var_net_salary
        ,bg="lightyellow",fg="black").place(x=420,y=180,width=100)

        btn_calculate = Button(Frame2,text="Calculate",command=self.calculate,
        font=("times new roman",20)
        ,bg="orange",fg="white").place(x=150,y=225,height=30,width=120)

        btn_save = Button(Frame2,text="Save",command=self.add,
        font=("times new roman",20)
        ,bg="green",fg="white").place(x=285,y=225,height=30,width=120)

        btn_clear = Button(Frame2,text="clear",
        font=("times new roman",20)
        ,bg="grey",fg="black").place(x=420,y=225,height=30,width=120)

        btn_update = Button(Frame2,text="Update",
        font=("times new roman",20)
        ,bg="blue",fg="white").place(x=150,y=260,height=30,width=120)

        btn_delete = Button(Frame2,text="Delete",command=self.delete,
        font=("times new roman",20)
        ,bg="red",fg="white").place(x=285,y=260,height=30,width=120)

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

        #================salary frame=================================
        sal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_Frame.place(x=251,y=2,width=322,height=300)
        title_sal=Label(sal_Frame,text="salary Reciept",
        font=("times new roman",20,)
        ,bg="#686868",fg="white",anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        sal_Frame2 = Frame(sal_Frame,bg='white',bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)

        sample = f'''\tCompany Name, xyz\n\tAddress: xyz, Floor4
-----------------------------------------
Employee ID\t\t:  xxx
salary\t\t:  mm-yyyy
Generated on\t\t: dd-mm-yyyy
-----------------------------------------
Total Days\t\t:  xx
Total Present\t\t:  xx
Total Absents\t\t:  xx 
Convence\t\t:  Rs.xxxx
PF\t\t:  Rs.xxxx
Gross Payment\t\t:  Rs.xxxx
Net salary\t\t:  Rs.xxxx
-----------------------------------------
This is the computer Generated slip, not required any signature
'''

        scroll_y = Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_recipt = Text(sal_Frame2,font=("times new roman",15),bg='lightyellow',yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)
        self.txt_salary_recipt.insert(END, sample)

        btn_print = Button(sal_Frame,text="Print",
        font=("times new roman",20)
        ,bg="lightblue",fg="white").place(x=180,y=262,height=30,width=120)



        self.check_connection()

#====================All functions Start here===========================

    def search(self):
        try:
            con = pymysql.connect(host = 'localhost',user='root', password='',db = 'ems')
            cur=con.cursor()
            cur.execute("Select * from emp_salary where e_id=%s",(self.var_code.get()))
            rows = cur.fetchone()
            #print(rows)
                
            if rows == None:
                messagebox.showerror("Error", 'Invalid Employee ID, please try with another ID',parent = self.root) 
            else:
                self.var_code.set(rows[0])
                self.var_designation.set(rows[1])
                self.var_name.set(rows[2])
                self.var_Age.set(rows[3])
                self.var_Gender.set(rows[4])
                self.var_Email.set(rows[5])
                self.var_hired.set(rows[6])
                self.var_DOJ.set(rows[7])
                self.var_DOB.set(rows[8])                   
                self.var_Experience.set(rows[9])
                self.var_proof.set(rows[10])               
                self.var_Contact.set(rows[11])                   
                self.var_Status.set(rows[12])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,rows[13])

                self.var_month.set(rows[14])
                self.var_year.set(rows[15])
                self.var_salary.set(rows[16])
                self.var_totaldays.set(rows[17])
                self.var_absent.set(rows[18])
                self.var_Medical.set(rows[19])
                self.var_pf.set(rows[20])
                self.var_convence.set(rows[21])
                self.var_net_salary.set(rows[22])
                file_=open('salary_recipt/'+str(rows[23]),'r')
                self.txt_salary_recipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_recipt.insert(END,i)
                file_.close()
         
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')



    def delete(self):
        try:
            con = pymysql.connect(host = 'localhost',user='root', password='',db = 'ems')
            cur=con.cursor()
            cur.execute("Select * from emp_salary where e_id=%s",(self.var_code.get()))
            rows = cur.fetchone()
            #print(rows)
                
            if rows == None:
                messagebox.showerror("Error", 'Invalid Employee ID, please try with another ID',parent = self.root) 
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete?")
                if op>1:
                    cur.execute("DELETE from emp_salary where e_id=%s",(self.var_emp_code.get()))
                    con.commit()
                    con.close()
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')

    
    def add(self):
        if self.var_code.get()=='' or self.var_salary.get()=='' or self.var_name=='':
            messagebox.showerror("Error","All details are required")
        else:
            try:
                con = pymysql.connect(host = 'localhost',user='root', password='',db = 'ems')
                cur=con.cursor()
                cur.execute("Select * from emp_salary where e_id=%s",(self.var_code.get()))
                rows = cur.fetchone()
                #print(rows)
                
                if rows != None:
                    messagebox.showerror("Error", 'This employee ID is already available in our record,try again with another ID',parent = self.root) 
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_code.get(),
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_Age.get(),
                        self.var_Gender.get(),
                        self.var_Email.get(),
                        self.var_hired.get(),
                        self.var_DOJ.get(),
                        self.var_DOB.get(),                   
                        self.var_Experience.get(),
                        self.var_proof.get(),               
                        self.var_Contact.get(),                   
                        self.var_Status.get(),
                        self.txt_address.get('1.0',END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_totaldays.get(),
                        self.var_absent.get(),
                        self.var_Medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_code.get()+".txt"
                        
                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('salary_recipt/'+str(self.var_code.get())+".txt",'w')
                    file_.write(self.txt_salary_recipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success",'Record added successfully')


            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')

    def calculate(self):

                per_day = int(self.var_salary.get())/int(self.var_totaldays.get())
                work_day = int(self.var_totaldays.get())-int(self.var_absent.get())
                sal_ = per_day * work_day
                deduct = int(self.var_Medical.get())+int(self.var_pf.get())
                addition = int(self.var_convence.get())
                net_sal = sal_ - deduct + addition
                self.var_net_salary.set(str(round(net_sal,2)))
                new_sample=f'''\tCompany Name, XYZ\n\tAddress: XYZ,Floor4
----------------------------------------------
Employee Id\t\t:  {self.var_code.get()}
salary of\t\t:  {self.var_month.get()}-{self.var_year.get()}
Generated On:  {str(time.strftime("%d-%M-%Y"))}
----------------------------------------------
Total Days\t\t:  {self.var_totaldays.get()}
Total Presents\t\t:  {str(int(self.var_totaldays.get())-int(self.var_absent.get()))}
Total absents\t\t:  {self.var_absent.get()}
Convence\t\t:  {self.var_convence.get()}
Medical\t\t:  {self.var_Medical.get()}
PF\t\t:  {self.var_pf.get()}
Gross Payment\t\t:  {self.var_salary.get()}
Net salary\t\t:  {self.var_convence.get()}
----------------------------------------------
This is computer generated slip, not required any signature
'''
                self.txt_salary_recipt.delete('1.0',END)
                self.txt_salary_recipt.insert(END,new_sample)
  
    def check_connection(self):
        try:
            con = pymysql.connect(host = 'localhost',user='root', password='',db = 'ems')
            cur=con.cursor()
            cur.execute("Select * from emp_salary")
            rows = cur.fetchall()
            print(rows)    
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')


root = Tk()
obj=EmployeeSystem(root)
root.mainloop()