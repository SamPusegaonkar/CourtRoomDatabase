from tkinter import *
from tkinter import messagebox
from pymysql import *
from tkinter.font import Font

class GUI(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        self.title('Court Case Database')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, addCase,findCase,modifyCase,deleteCase):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self, parent)
        self.controller=controller

        self.add = PhotoImage(file = "Add1.gif")
        self.find = PhotoImage(file = "Find1.gif")
        self.modify = PhotoImage(file = "Modify1.gif")
        self.delete = PhotoImage(file = "Delete1.gif")

        self.background1=Label(self,image=self.add,borderwidth=1, relief="solid",highlightbackground="white")
        self.background1.grid(row=0,column=0)
        self.background2=Label(self,image=self.find,borderwidth=1, relief="solid",highlightbackground="white")
        self.background2.grid(row=0,column=1)
        self.background3=Label(self,image=self.modify,borderwidth=1, relief="solid",highlightbackground="white")
        self.background3.grid(row=1,column=0)
        self.background4=Label(self,image=self.delete,borderwidth=1, relief="solid",highlightbackground="white")
        self.background4.grid(row=1,column=1)

        self.myFont = Font(family="Adam.CG PRO", size=18)

        self.Button1=Button(self.background1,text="Add a case",command=lambda: controller.show_frame("addCase"),font=self.myFont,bg="white").place(relx=0.5, rely=0.5, anchor=CENTER)
        self.Button2=Button(self.background2,text="Find a case",command=lambda: controller.show_frame("findCase"),font=self.myFont,bg="white").place(relx=0.5, rely=0.5, anchor=CENTER)
        self.Button3=Button(self.background3,text="Modify a case",command=lambda: controller.show_frame("modifyCase"),font=self.myFont,bg="white").place(relx=0.5, rely=0.5, anchor=CENTER)
        self.Button4=Button(self.background4,text="Delete a case",command=lambda: controller.show_frame("deleteCase"),font=self.myFont,bg="white").place(relx=0.5, rely=0.5, anchor=CENTER)

class addCase(Frame):

    def addEntry(self):

        try:
            connection=connect(host="localhost",user="root",passwd='root',db='court_room')
            cursor=connection.cursor()
            print(self.judge_name_Entry.get(),self.judge_case_Entry.get(),self.judge_id_Entry.get())
            sql=('insert into judge(f_name,case_number,id) values("%s","%s","%s");' %(self.judge_name_Entry.get(),self.judge_case_Entry.get(),self.judge_id_Entry.get()))
            cursor.execute(sql)
            connection.commit()
            connection=connect(host="localhost",user="root",passwd='root',db='court_room')
            cursor=connection.cursor()
            sql=('insert into suspect(f_name,phone_nummber,case_number,address) values("%s","%s","%s","%s");' %(self.suspect_name_Entry.get(),self.suspect_phone_Entry.get(),self.judge_case_Entry.get(),self.suspect_address_Entry.get()))
            cursor.execute(sql)
            connection.commit()
            connection=connect(host="localhost",user="root",passwd='root',db='court_room')
            cursor=connection.cursor()
            sql=('insert into victim(f_name,phone_nummber,case_number,address) values("%s","%s","%s","%s");' %(self.victim_name_Entry.get(),self.victim_phone_Entry.get(),self.judge_case_Entry.get(),self.victim_address_Entry.get()))
            cursor.execute(sql)
            connection.commit()
            messagebox.showinfo("Add", "Record Added!")
        except Exception as e:

            messagebox.showinfo("Add", "Error!")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.add = PhotoImage(file = "Adddd.gif")

        self.myFont = Font(family="Adam.CG PRO", size=10)
        self.myFont1 = Font(family="Adam.CG PRO", size=20)
        self.myFont2 = Font(family="Adam.CG PRO", size=25)
        self.background1=Label(self,image=self.add)
        self.background1.place(x=0, y=0, relwidth=1, relheight=1)

        self.backButton=Button(self.background1,text="Back",command=lambda: controller.show_frame("StartPage"),font=self.myFont1)
        self.backButton.grid(row=0,column=0)

        self.title=Label(self.background1,text="Enter the details",font=self.myFont2)
        self.title.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.suspect_name_label=Label(self.background1,text="Suspect Name",font=self.myFont)
        self.suspect_name_label.place(relx=0.01, rely=0.4)
        self.suspect_name_Entry=Entry(self.background1,font=self.myFont)
        self.suspect_name_Entry.place(relx=0.12, rely=0.4)
        self.suspect_name_Entry.focus()

        self.suspect_address_label=Label(self.background1,text="Address",font=self.myFont)
        self.suspect_address_label.place(relx=0.01, rely=0.5)
        self.suspect_address_Entry=Entry(self.background1,font=self.myFont)
        self.suspect_address_Entry.place(relx=0.12, rely=0.5)


        self.suspect_phone_label=Label(self.background1,text="Phone No.",font=self.myFont)
        self.suspect_phone_label.place(relx=0.01, rely=0.6)
        self.suspect_phone_Entry=Entry(self.background1,font=self.myFont,)
        self.suspect_phone_Entry.place(relx=0.12, rely=0.6)


        self.judge_name_label=Label(self.background1,text="Judge Name",font=self.myFont)
        self.judge_name_label.place(relx=0.35 ,rely=0.4)
        self.judge_name_Entry=Entry(self.background1,font=self.myFont)
        self.judge_name_Entry.place(relx=0.47, rely=0.4)


        self.judge_id_label=Label(self.background1,text="Judge ID",font=self.myFont)
        self.judge_id_label.place(relx=0.35, rely=0.5)
        self.judge_id_Entry=Entry(self.background1,font=self.myFont)
        self.judge_id_Entry.place(relx=0.47, rely=0.5)


        self.judge_case_label=Label(self.background1,text="Case ID",font=self.myFont)
        self.judge_case_label.place(relx=0.35, rely=0.6)
        self.judge_case_Entry=Entry(self.background1,font=self.myFont)
        self.judge_case_Entry.place(relx=0.47, rely=0.6)


        self.victim_name_label=Label(self.background1,text="Victim Name",font=self.myFont)
        self.victim_name_label.place(relx=0.68, rely=0.4)
        self.victim_name_Entry=Entry(self.background1,font=self.myFont)
        self.victim_name_Entry.place(relx=0.81, rely=0.4)


        self.victim_address_label=Label(self.background1,text="Address",font=self.myFont)
        self.victim_address_label.place(relx=0.68, rely=0.5)
        self.victim_address_Entry=Entry(self.background1,font=self.myFont)
        self.victim_address_Entry.place(relx=0.81, rely=0.5)


        self.victim_phone_label=Label(self.background1,text="Phone No.",font=self.myFont)
        self.victim_phone_label.place(relx=0.68, rely=0.6)
        self.victim_phone_Entry=Entry(self.background1,font=self.myFont)
        self.victim_phone_Entry.place(relx=0.81, rely=0.6)


        self.submit=Button(self.background1,text="Submit",font=self.myFont1,command=self.addEntry)
        self.submit.place(relx=0.8, rely=0.85)
        self.result=StringVar()

class findCase(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        self.add = PhotoImage(file = "Adddd.gif")
        self.myFont2 = Font(family="Adam.CG PRO", size=25)
        self.background1=Label(self,image=self.add)
        self.background1.place(x=0, y=0, relwidth=1, relheight=1)

        self.myFont = Font(family="Adam.CG PRO", size=14)
        self.myFont1 = Font(family="Adam.CG PRO", size=10)

        self.backButton=Button(self.background1,text="Back",command=lambda: controller.show_frame("StartPage"),font=self.myFont)
        self.backButton.grid(row=0,column=0)

        self.search=Entry(self.background1,font=self.myFont)
        self.search.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.var = IntVar()
        self.R1 = Radiobutton(self.background1, text="Case Number", variable=self.var, value=1,
                          command=self.find ,font=self.myFont)
        self.R1.place( x=50,y=100 )
        self.R2 = Radiobutton(self.background1, text="Judge", variable=self.var, value=2,
                          command=self.find ,font=self.myFont)
        self.R2.place( x=50,y=200 )

        self.R3 = Radiobutton(self.background1, text="Suspect", variable=self.var, value=3,
                          command=self.find ,font=self.myFont)
        self.R3.place(x=50,y=300)

        self.R4 = Radiobutton(self.background1, text="Victim", variable=self.var, value=4,
                          command=self.find ,font=self.myFont)
        self.R4.place(x=50,y=400)

        self.click=Button(self.background1,text="Search",command=self.find,font=self.myFont)
        self.click.place(relx=0.7 , rely=0.1, anchor=CENTER)

    def find(self):
        if(self.var.get()==1):
            self.click=Button(self.background1,text="Search",command=self.find,font=self.myFont)
            self.click.place(relx=0.7 , rely=0.1, anchor=CENTER)
            case_no=self.search.get()
            if(case_no!=""):
                try:
                    connection=connect(host="localhost",user="root",passwd='root',db='court_room')
                    cursor=connection.cursor()
                    sql=('select * from suspect where case_number="%s"' %(case_no))
                    cursor.execute(sql)
                    suspect_result=cursor.fetchone()
                    print(suspect_result)
                    sql=('select * from judge where case_number="%s"' %(case_no))
                    cursor.execute(sql)
                    judge_result=cursor.fetchone()
                    print(judge_result)
                    sql=('select * from victim where case_number="%s"' %(case_no))
                    cursor.execute(sql)
                    victim_result=cursor.fetchone()
                    print(victim_result)
                    sql=('select * from verdict where case_number="%s"' %(case_no))
                    cursor.execute(sql)
                    verdict_result=cursor.fetchone()
                    print(verdict_result)
                    if judge_result is not None and suspect_result is not None and victim_result is not None and verdict_result is not None:

                        suspect_result=list(suspect_result)
                        k=suspect_result[0]
                        l=suspect_result[1]
                        m=suspect_result[2]
                        n=suspect_result[3]
                        self.label21=Label(self.background1,text="Suspect Name",font=self.myFont1)
                        self.label21.place(x=250,y=90)
                        self.label22=Label(self.background1,text=k,font=self.myFont1)
                        self.label22.place(x=390,y=90)
                        self.label23=Label(self.background1,text="Last Name",font=self.myFont1)
                        self.label23.place(x=250,y=140)
                        self.label24=Label(self.background1,text=l,font=self.myFont1)
                        self.label24.place(x=390,y=140)
                        self.label25=Label(self.background1,text="Phone Number",font=self.myFont1)
                        self.label25.place(x=250,y=190)
                        self.label26=Label(self.background1,text=m,font=self.myFont1)
                        self.label26.place(x=390,y=190)
                        self.label27=Label(self.background1,text="Case Number",font=self.myFont1)
                        self.label27.place(x=250,y=240)
                        self.label28=Label(self.background1,text=n,font=self.myFont1)
                        self.label28.place(x=390,y=240)

                        verdict_result=list(verdict_result)
                        z=verdict_result[0]
                        y=verdict_result[2]
                        self.labela=Label(self.background1,text="Judgement",font=self.myFont1)
                        self.labela.place(x=250,y=290)
                        self.labelb=Label(self.background1,text=z,font=self.myFont1)
                        self.labelb.place(x=390,y=290)
                        self.labelc=Label(self.background1,text="IPC Penal Code",font=self.myFont1)
                        self.labelc.place(x=250,y=340)
                        self.labeld=Label(self.background1,text=y,font=self.myFont1)
                        self.labeld.place(x=390,y=340)

                        judge_result=list(judge_result)
                        a=judge_result[0]
                        b=judge_result[1]
                        c=judge_result[2]
                        d=judge_result[3]
                        e=judge_result[4]
                        f=judge_result[5]
                        g=judge_result[6]
                        h=judge_result[7]
                        i=judge_result[8]
                        j=judge_result[9]
                        self.label1=Label(self.background1,text="Judge First Name",font=self.myFont1)
                        self.label1.place(x=490,y=90)
                        self.label2=Label(self.background1,text=a,font=self.myFont1)
                        self.label2.place(x=630,y=90)
                        self.label3=Label(self.background1,text="Judge Last Name",font=self.myFont1)
                        self.label3.place(x=490,y=140)
                        self.label4=Label(self.background1,text=b,font=self.myFont1)
                        self.label4.place(x=630,y=140)
                        self.label5=Label(self.background1,text="Street Address",font=self.myFont1)
                        self.label5.place(x=490,y=190)
                        self.label6=Label(self.background1,text=c,font=self.myFont1)
                        self.label6.place(x=630,y=190)
                        self.label7=Label(self.background1,text="Area Address",font=self.myFont1)
                        self.label7.place(x=490,y=240)
                        self.label8=Label(self.background1,text=d,font=self.myFont1)
                        self.label8.place(x=630,y=240)
                        self.label9=Label(self.background1,text="Qualification",font=self.myFont1)
                        self.label9.place(x=490,y=290)
                        self.label10=Label(self.background1,text=e,font=self.myFont1)
                        self.label10.place(x=630,y=290)
                        self.label11=Label(self.background1,text="DOB",font=self.myFont1)
                        self.label11.place(x=490,y=340)
                        self.label12=Label(self.background1,text=f,font=self.myFont1)
                        self.label12.place(x=630,y=340)
                        self.label13=Label(self.background1,text="Judge Age",font=self.myFont1)
                        self.label13.place(x=490,y=390)
                        self.label14=Label(self.background1,text=g,font=self.myFont1)
                        self.label14.place(x=630,y=390)
                        self.label15=Label(self.background1,text="Judge Salary",font=self.myFont1)
                        self.label15.place(x=490,y=440)
                        self.label16=Label(self.background1,text=h,font=self.myFont1)
                        self.label16.place(x=630,y=440)
                        self.label17=Label(self.background1,text="Judge Case Number",font=self.myFont1)
                        self.label17.place(x=490,y=490)
                        self.label18=Label(self.background1,text=i,font=self.myFont1)
                        self.label18.place(x=630,y=490)
                        self.label19=Label(self.background1,text="Judge ID",font=self.myFont1)
                        self.label19.place(x=490,y=540)
                        self.label20=Label(self.background1,text=j,font=self.myFont1)
                        self.label20.place(x=630,y=540)
                        victim_result=list(victim_result)
                        o=victim_result[0]
                        p=victim_result[1]
                        q=victim_result[2]
                        r=victim_result[3]
                        self.label29=Label(self.background1,text="Victim Name",font=self.myFont1)
                        self.label29.place(x=760,y=90)
                        self.label30=Label(self.background1,text=o,font=self.myFont1)
                        self.label30.place(x=870,y=90)
                        self.label31=Label(self.background1,text="Last Name",font=self.myFont1)
                        self.label31.place(x=760,y=140)
                        self.label32=Label(self.background1,text=p,font=self.myFont1)
                        self.label32.place(x=870,y=140)
                        self.label33=Label(self.background1,text="Phone Number",font=self.myFont1)
                        self.label33.place(x=760,y=190)
                        self.label34=Label(self.background1,text=q,font=self.myFont1)
                        self.label34.place(x=870,y=190)
                        self.label35=Label(self.background1,text="Case Number",font=self.myFont1)
                        self.label35.place(x=760,y=240)
                        self.label36=Label(self.background1,text=r,font=self.myFont1)
                        self.label36.place(x=870,y=240)

                    else:

                        messagebox.showinfo("Find", "No record found!")
                except Exception as e:
                    print(e)
        if(self.var.get()==2):
            judge_detail=self.search.get()
            if(judge_detail!=""):
                try:
                    connection=connect(host="localhost",user="root",passwd='root',db='court_room')
                    cursor=connection.cursor()
                    print('abc')
                    sql=('select * from judge where f_name="%s" or l_name="%s" or street="%s" or area="%s" or qualification="%s" or dob="%s" or age="%s" or Salary="%s" or case_number="%s" or id="%s"' %(judge_detail,judge_detail,judge_detail,judge_detail,judge_detail,judge_detail,judge_detail,judge_detail,judge_detail,judge_detail))
                    cursor.execute(sql)
                    result=cursor.fetchone()

                    print(result)
                    if(result is not None):
                        result=list(result)
                        a=result[0]
                        b=result[1]
                        c=result[2]
                        d=result[3]
                        e=result[4]
                        f=result[5]
                        g=result[6]
                        h=result[7]
                        i=result[8]
                        j=result[9]
                        self.label37=Label(self.background1,text="Judge First Name",font=self.myFont1)
                        self.label37.place(x=400,y=100)
                        self.label38=Label(self.background1,text=a,font=self.myFont1)
                        self.label38.place(x=540,y=100)
                        self.label39=Label(self.background1,text="Judge Last Name",font=self.myFont1)
                        self.label39.place(x=400,y=150)
                        self.label40=Label(self.background1,text=b,font=self.myFont1)
                        self.label40.place(x=540,y=150)
                        self.label41=Label(self.background1,text="Judge Street Name",font=self.myFont1)
                        self.label41.place(x=400,y=200)
                        self.label42=Label(self.background1,text=c,font=self.myFont1)
                        self.label42.place(x=540,y=200)
                        self.label43=Label(self.background1,text="Judge Area Name",font=self.myFont1)
                        self.label43.place(x=400,y=250)
                        self.label44=Label(self.background1,text=d,font=self.myFont1)
                        self.label44.place(x=540,y=250)
                        self.label45=Label(self.background1,text="Judge Qualification",font=self.myFont1)
                        self.label45.place(x=400,y=300)
                        self.label46=Label(self.background1,text=e,font=self.myFont1)
                        self.label46.place(x=540,y=300)
                        self.label47=Label(self.background1,text="Judge DOB",font=self.myFont1)
                        self.label47.place(x=400,y=350)
                        self.label48=Label(self.background1,text=f,font=self.myFont1)
                        self.label48.place(x=540,y=350)
                        self.label49=Label(self.background1,text="Judge Age",font=self.myFont1)
                        self.label49.place(x=400,y=400)
                        self.label50=Label(self.background1,text=g,font=self.myFont1)
                        self.label50.place(x=540,y=400)
                        self.label51=Label(self.background1,text="Judge Salary",font=self.myFont1)
                        self.label51.place(x=400,y=450)
                        self.label52=Label(self.background1,text=h,font=self.myFont1)
                        self.label52.place(x=540,y=450)
                        self.label53=Label(self.background1,text="Judge Case Number",font=self.myFont1)
                        self.label53.place(x=400,y=500)
                        self.label54=Label(self.background1,text=i,font=self.myFont1)
                        self.label54.place(x=540,y=500)
                        self.label55=Label(self.background1,text="Judge ID",font=self.myFont1)
                        self.label55.place(x=400,y=550)
                        self.label56=Label(self.background1,text=j,font=self.myFont1)
                        self.label56.place(x=540,y=550)
                        return
                    else:

                        messagebox.showinfo("Find ", "No record found!")
                except Exception as e:
                    print(e)
        if(self.var.get()==3):
            suspect_detail=self.search.get()
            if(suspect_detail!=""):
                try:

                    connection=connect(host="localhost",user="root",passwd='root',db='court_room')
                    cursor=connection.cursor()
                    sql=('select * from suspect where f_name="%s" or l_name="%s"  or phone_nummber="%s" or case_number="%s" ' %(suspect_detail,suspect_detail,suspect_detail,suspect_detail))
                    cursor.execute(sql)
                    result=cursor.fetchone()
                    print(result)
                    if(result is not None):
                        result=list(result)
                        a=result[0]
                        b=result[1]
                        c=result[2]
                        d=result[3]
                        self.label65=Label(self.background1,text="Suspect Name",font=self.myFont1)
                        self.label65.place(x=400,y=100)
                        self.label66=Label(self.background1,text=a,font=self.myFont1)
                        self.label66.place(x=540,y=100)
                        self.label67=Label(self.background1,text="Last Name",font=self.myFont1)
                        self.label67.place(x=400,y=150)
                        self.label68=Label(self.background1,text=b,font=self.myFont1)
                        self.label68.place(x=540,y=150)
                        self.label69=Label(self.background1,text="Phone no",font=self.myFont1)
                        self.label69.place(x=400,y=200)
                        self.label70=Label(self.background1,text=c,font=self.myFont1)
                        self.label70.place(x=540,y=200)
                        self.label71=Label(self.background1,text="Case ID",font=self.myFont1)
                        self.label71.place(x=400,y=250)
                        self.label72=Label(self.background1,text=d,font=self.myFont1)
                        self.label72.place(x=540,y=250)
                    else:

                        messagebox.showinfo("Find", "No record found!")

                except Exception as e:
                    print(e)
        if(self.var.get()==4):
            victim_detail=self.search.get()
            if(victim_detail != ""):
                try:
                    connection=connect(host="localhost",user="root",passwd='root',db='court_room')
                    cursor=connection.cursor()

                    sql=('select * from victim where f_name="%s" or l_name="%s" or phone_nummber="%s" or case_number="%s"' %(victim_detail,victim_detail,victim_detail,victim_detail))

                    cursor.execute(sql)
                    result=cursor.fetchone()

                    if(result is not None):
                        result=list(result)
                        a=result[0]
                        b=result[1]
                        c=result[2]
                        d=result[3]
                        self.label57=Label(self.background1,text="Victim Name",font=self.myFont1)
                        self.label57.place(x=400,y=100)
                        self.label58=Label(self.background1,text=a,font=self.myFont1)
                        self.label58.place(x=540,y=100)
                        self.label59=Label(self.background1,text="Last Name",font=self.myFont1)
                        self.label59.place(x=400,y=150)
                        self.label60=Label(self.background1,text=b,font=self.myFont1)
                        self.label60.place(x=540,y=150)
                        self.label61=Label(self.background1,text="Phone no",font=self.myFont1)
                        self.label61.place(x=400,y=200)
                        self.label62=Label(self.background1,text=c,font=self.myFont1)
                        self.label62.place(x=540,y=200)
                        self.label63=Label(self.background1,text="Case ID",font=self.myFont1)
                        self.label63.place(x=400,y=250)
                        self.label64=Label(self.background1,text=d,font=self.myFont1)
                        self.label64.place(x=540,y=250)

                    else:
                        messagebox.showinfo("Find", "No Record Found!")

                except Exception as e:
                    print(e)
class modifyCase(Frame):
    def check(self,event):
        if(self.variable.get()=="Judge"):
            self.variable2 = StringVar(self)
            self.variable2.set(self.Judge_Options[0])
            self.list2 = OptionMenu(self, self.variable2, "f_name","l_ame","Street","Area","Qualification","DOB","age","salary","case_number","ID",command=self.check1)
            self.list2.place(x=300,y=120)
            self.labelq=Label(self,text="Select a column",font=self.myFont)
            self.labelq.place(x=270,y=80)
        elif(self.variable.get()=="Suspect"):
            self.variable3 = StringVar(self)
            self.variable3.set(self.Suspect_Options[0])
            self.list3 = OptionMenu(self, self.variable3,"f_name","l_name","Phone_Nummber","Case_Number","address",command=self.check1)
            self.list3.place(x=300,y=120)
            self.labelq=Label(self,text="Select a column",font=self.myFont)
            self.labelq.place(x=270,y=80)
        elif(self.variable.get()=="Victim"):
            self.variable4 = StringVar(self)
            self.variable4.set(self.Victim_Options[0])
            self.list4 = OptionMenu(self, self.variable4, "f_name","l_ame","phone_nummber","case_number","address",command=self.check1)
            self.list4.place(x=300,y=120)
            self.labelq=Label(self,text="Select a column",font=self.myFont)
            self.labelq.place(x=270,y=80)
    def check1(self,event):
        self.search1=Entry(self.background1,font=self.myFont)
        self.search1.place(x=450,y=120)
        self.labelr=Label(self,text="Search the value",font=self.myFont)
        self.labelr.place(x=480,y=80)
        self.button=Button(self.background1,command=self.update,text="Next",font=self.myFont)
        self.button.place(x=800,y=120)
    def update(self):
        try:
            connection=connect(host="localhost",user="root",passwd='root',db='court_room')
            cursor=connection.cursor()
            print(self.variable2.get(),self.variable.get(),self.variable2.get(),self.search1.get())
            sql=('select %s from %s where %s="%s"' %(self.variable2.get(),self.variable.get(),self.variable2.get(),self.search1.get()))
            cursor.execute(sql)
            result=cursor.fetchone()
            self.labely=Label(self,text="Old Entry",font=self.myFont)
            self.labely.place(x=250,y=250)
            self.labelz=Label(self,text=result,font=self.myFont)
            self.labelz.place(x=400,y=250)
            self.labelp=Label(self,text="NEW Entry",font=self.myFont)
            self.labelp.place(x=250,y=350)
            self.labelf=Entry(self,font=self.myFont)
            self.labelf.place(x=400,y=350)
            self.labeld=Button(self,text="Update",command=self.enter,font=self.myFont)
            self.labeld.place(x=700,y=350)
        except Exception as e:
            print(e)
    def enter(self):
        try:
            connection=connect(host="localhost",user="root",passwd='root',db='court_room')
            cursor=connection.cursor()
            print(self.variable.get(),self.variable2.get(),self.labelf.get(),self.variable2.get(),self.search1.get())
            sql=('update %s set %s="%s" WHERE %s="%s"' %(self.variable.get(),self.variable2.get(),self.labelf.get(),self.variable2.get(),self.search1.get()))
            cursor.execute(sql)
            connection.commit()
            messagebox.showinfo("Modify", "Record Modified!")
        except Exception as e:
            print(e)
            messagebox.showinfo("Modify", "Error!")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.add = PhotoImage(file = "Adddd.gif")
        self.myFont2 = Font(family="Adam.CG PRO", size=25)
        self.background1=Label(self,image=self.add)
        self.background1.place(x=0, y=0, relwidth=1, relheight=1)

        self.myFont = Font(family="Adam.CG PRO", size=14)
        self.myFont1 = Font(family="Adam.CG PRO", size=10)
        self.myFont2 = Font(family="Adam.CG PRO", size=18)
        self.backButton=Button(self.background1,text="Back",command=lambda: controller.show_frame("StartPage"),font=self.myFont)
        self.backButton.grid(row=0,column=0)

        self.labelp=Label(self,text="Select a table",font=self.myFont)
        self.labelp.place(x=70,y=80)
        self.OPTIONS = ["Judge","Suspect","Victim"]
        self.Judge_Options=["First Name","Last Name","Street","Area","Qualification","DOB","Age","Salary","Case Number","ID"]
        self.Suspect_Options=["First Name","Last Name","Phone Number","Case Number"]
        self.Victim_Options=["First Name","Last Name","Phone Number","Case Number"]
        self.variable = StringVar(self)
        self.variable.set(self.OPTIONS[0])
        self.list1 = OptionMenu(self, self.variable, "Judge","Suspect","Victim",command=self.check)
        self.list1.place(x=100,y=120)

class deleteCase(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.add = PhotoImage(file = "Adddd.gif")
        self.myFont2 = Font(family="Adam.CG PRO", size=25)
        self.background1=Label(self,image=self.add)
        self.background1.place(x=0, y=0, relwidth=1, relheight=1)

        self.myFont = Font(family="Adam.CG PRO", size=14)
        self.myFont1 = Font(family="Adam.CG PRO", size=10)

        self.backButton=Button(self.background1,text="Back",command=lambda: controller.show_frame("StartPage"),font=self.myFont)
        self.backButton.grid(row=0,column=0)

        self.search=Entry(self.background1,font=self.myFont)

        self.search.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.click=Button(self.background1,text="Search",command=self.find,font=self.myFont)
        self.click.place(relx=0.7 , rely=0.1, anchor=CENTER)

        self.var = IntVar()
        self.R1 = Radiobutton(self.background1, text="Case Number", variable=self.var, value=1,
                          command=self.find ,font=self.myFont)
        self.R1.place( x=50,y=100 )
        self.R2 = Radiobutton(self.background1, text="Judge", variable=self.var, value=2,
                          command=self.find ,font=self.myFont)
        self.R2.place( x=50,y=200 )

        self.R3 = Radiobutton(self.background1, text="Suspect", variable=self.var, value=3,
                          command=self.find ,font=self.myFont)
        self.R3.place(x=50,y=300)

        self.R4 = Radiobutton(self.background1, text="Victim", variable=self.var, value=4,
                          command=self.find ,font=self.myFont)
        self.R4.place(x=50,y=400)
    def delete(self):

        try:
            connection=connect(host="localhost",user="root",passwd='root',db='court_room')
            cursor=connection.cursor()
            sql=('delete from suspect where case_number=%s' %(self.search.get()))
            cursor.execute(sql)
            connection.commit()
            sql=('delete from judge where case_number=%s' %(self.search.get()))
            cursor.execute(sql)
            connection.commit()
            sql=('delete from victim where case_number=%s' %(self.search.get()))
            cursor.execute(sql)
            connection.commit()
            messagebox.showinfo("Delete", "Record Deleted!")
        except Exception as e:
            print(e)
            messagebox.showinfo("Delete", "Error!")


    def find(self):
        if(self.var.get()==1):
            self.click=Button(self.background1,text="Search",command=self.find,font=self.myFont)
            self.click.place(relx=0.7 , rely=0.1, anchor=CENTER)
            case_no=self.search.get()
            if(case_no!=""):
                try:
                    connection=connect(host="localhost",user="root",passwd='root',db='court_room')
                    cursor=connection.cursor()
                    sql=('select * from suspect where case_number="%s"' %(case_no))
                    cursor.execute(sql)
                    suspect_result=cursor.fetchone()
                    print(suspect_result)
                    sql=('select * from judge where case_number="%s"' %(case_no))
                    cursor.execute(sql)
                    judge_result=cursor.fetchone()
                    print(judge_result)
                    sql=('select * from victim where case_number="%s"' %(case_no))
                    cursor.execute(sql)
                    victim_result=cursor.fetchone()
                    print(victim_result)
                    if judge_result is not None and suspect_result is not None and victim_result is not None:

                        suspect_result=list(suspect_result)
                        k=suspect_result[0]
                        l=suspect_result[1]
                        m=suspect_result[2]
                        n=suspect_result[3]
                        self.label21=Label(self.background1,text="Suspect Name",font=self.myFont1)
                        self.label21.place(x=250,y=90)
                        self.label22=Label(self.background1,text=k,font=self.myFont1)
                        self.label22.place(x=390,y=90)
                        self.label23=Label(self.background1,text="Last Name",font=self.myFont1)
                        self.label23.place(x=250,y=140)
                        self.label24=Label(self.background1,text=l,font=self.myFont1)
                        self.label24.place(x=390,y=140)
                        self.label25=Label(self.background1,text="Phone Number",font=self.myFont1)
                        self.label25.place(x=250,y=190)
                        self.label26=Label(self.background1,text=m,font=self.myFont1)
                        self.label26.place(x=390,y=190)
                        self.label27=Label(self.background1,text="Case Number",font=self.myFont1)
                        self.label27.place(x=250,y=240)
                        self.label28=Label(self.background1,text=n,font=self.myFont1)
                        self.label28.place(x=390,y=240)
                        judge_result=list(judge_result)
                        a=judge_result[0]
                        b=judge_result[1]
                        c=judge_result[2]
                        d=judge_result[3]
                        e=judge_result[4]
                        f=judge_result[5]
                        g=judge_result[6]
                        h=judge_result[7]
                        i=judge_result[8]
                        j=judge_result[9]
                        self.label1=Label(self.background1,text="Judge First Name",font=self.myFont1)
                        self.label1.place(x=490,y=90)
                        self.label2=Label(self.background1,text=a,font=self.myFont1)
                        self.label2.place(x=630,y=90)
                        self.label3=Label(self.background1,text="Judge Last Name",font=self.myFont1)
                        self.label3.place(x=490,y=140)
                        self.label4=Label(self.background1,text=b,font=self.myFont1)
                        self.label4.place(x=630,y=140)
                        self.label5=Label(self.background1,text="Street Address",font=self.myFont1)
                        self.label5.place(x=490,y=190)
                        self.label6=Label(self.background1,text=c,font=self.myFont1)
                        self.label6.place(x=630,y=190)
                        self.label7=Label(self.background1,text="Area Address",font=self.myFont1)
                        self.label7.place(x=490,y=240)
                        self.label8=Label(self.background1,text=d,font=self.myFont1)
                        self.label8.place(x=630,y=240)
                        self.label9=Label(self.background1,text="Qualification",font=self.myFont1)
                        self.label9.place(x=490,y=290)
                        self.label10=Label(self.background1,text=e,font=self.myFont1)
                        self.label10.place(x=630,y=290)
                        self.label11=Label(self.background1,text="DOB",font=self.myFont1)
                        self.label11.place(x=490,y=340)
                        self.label12=Label(self.background1,text=f,font=self.myFont1)
                        self.label12.place(x=630,y=340)
                        self.label13=Label(self.background1,text="Judge Age",font=self.myFont1)
                        self.label13.place(x=490,y=390)
                        self.label14=Label(self.background1,text=g,font=self.myFont1)
                        self.label14.place(x=630,y=390)
                        self.label15=Label(self.background1,text="Judge Salary",font=self.myFont1)
                        self.label15.place(x=490,y=440)
                        self.label16=Label(self.background1,text=h,font=self.myFont1)
                        self.label16.place(x=630,y=440)
                        self.label17=Label(self.background1,text="Judge Case Number",font=self.myFont1)
                        self.label17.place(x=490,y=490)
                        self.label18=Label(self.background1,text=i,font=self.myFont1)
                        self.label18.place(x=630,y=490)
                        self.label19=Label(self.background1,text="Judge ID",font=self.myFont1)
                        self.label19.place(x=490,y=540)
                        self.label20=Label(self.background1,text=j,font=self.myFont1)
                        self.label20.place(x=630,y=540)
                        victim_result=list(victim_result)
                        o=victim_result[0]
                        p=victim_result[1]
                        q=victim_result[2]
                        r=victim_result[3]
                        self.label29=Label(self.background1,text="Victim Name",font=self.myFont1)
                        self.label29.place(x=760,y=90)
                        self.label30=Label(self.background1,text=o,font=self.myFont1)
                        self.label30.place(x=870,y=90)
                        self.label31=Label(self.background1,text="Last Name",font=self.myFont1)
                        self.label31.place(x=760,y=140)
                        self.label32=Label(self.background1,text=p,font=self.myFont1)
                        self.label32.place(x=870,y=140)
                        self.label33=Label(self.background1,text="Phone Number",font=self.myFont1)
                        self.label33.place(x=760,y=190)
                        self.label34=Label(self.background1,text=q,font=self.myFont1)
                        self.label34.place(x=870,y=190)
                        self.label35=Label(self.background1,text="Case Number",font=self.myFont1)
                        self.label35.place(x=760,y=240)
                        self.label36=Label(self.background1,text=r,font=self.myFont1)
                        self.label36.place(x=870,y=240)
                        self.clicka=Button(self.background1,text="Delete",command=self.delete,font=self.myFont)
                        self.clicka.place(x=870,y=500)

                    else:

                        messagebox.showinfo("Delete", "No record found!")
                except Exception as e:
                    print(e)
        if(self.var.get()==2):
            judge_detail=self.search.get()
            if(judge_detail!=""):
                try:
                    connection=connect(host="localhost",user="root",passwd='root',db='court_room')
                    cursor=connection.cursor()
                    print('abc')
                    sql=('select * from judge where f_name="%s" or l_name="%s" or street="%s" or area="%s" or qualification="%s" or dob="%s" or age="%s" or Salary="%s" or case_number="%s" or id="%s"' %(judge_detail,judge_detail,judge_detail,judge_detail,judge_detail,judge_detail,judge_detail,judge_detail,judge_detail,judge_detail))
                    cursor.execute(sql)
                    result=cursor.fetchone()

                    print(result)
                    if(result is not None):
                        result=list(result)

                        a=result[0]
                        b=result[1]
                        c=result[2]
                        d=result[3]
                        e=result[4]
                        f=result[5]
                        g=result[6]
                        h=result[7]
                        i=result[8]
                        j=result[9]
                        self.label37=Label(self.background1,text="Judge First Name",font=self.myFont1)
                        self.label37.place(x=400,y=100)
                        self.label38=Label(self.background1,text=a,font=self.myFont1)
                        self.label38.place(x=540,y=100)
                        self.label39=Label(self.background1,text="Judge Last Name",font=self.myFont1)
                        self.label39.place(x=400,y=150)
                        self.label40=Label(self.background1,text=b,font=self.myFont1)
                        self.label40.place(x=540,y=150)
                        self.label41=Label(self.background1,text="Judge Street Name",font=self.myFont1)
                        self.label41.place(x=400,y=200)
                        self.label42=Label(self.background1,text=c,font=self.myFont1)
                        self.label42.place(x=540,y=200)
                        self.label43=Label(self.background1,text="Judge Area Name",font=self.myFont1)
                        self.label43.place(x=400,y=250)
                        self.label44=Label(self.background1,text=d,font=self.myFont1)
                        self.label44.place(x=540,y=250)
                        self.label45=Label(self.background1,text="Judge Qualification",font=self.myFont1)
                        self.label45.place(x=400,y=300)
                        self.label46=Label(self.background1,text=e,font=self.myFont1)
                        self.label46.place(x=540,y=300)
                        self.label47=Label(self.background1,text="Judge DOB",font=self.myFont1)
                        self.label47.place(x=400,y=350)
                        self.label48=Label(self.background1,text=f,font=self.myFont1)
                        self.label48.place(x=540,y=350)
                        self.label49=Label(self.background1,text="Judge Age",font=self.myFont1)
                        self.label49.place(x=400,y=400)
                        self.label50=Label(self.background1,text=g,font=self.myFont1)
                        self.label50.place(x=540,y=400)
                        self.label51=Label(self.background1,text="Judge Salary",font=self.myFont1)
                        self.label51.place(x=400,y=450)
                        self.label52=Label(self.background1,text=h,font=self.myFont1)
                        self.label52.place(x=540,y=450)
                        self.label53=Label(self.background1,text="Judge Case Number",font=self.myFont1)
                        self.label53.place(x=400,y=500)
                        self.label54=Label(self.background1,text=i,font=self.myFont1)
                        self.label54.place(x=540,y=500)
                        self.label55=Label(self.background1,text="Judge ID",font=self.myFont1)
                        self.label55.place(x=400,y=550)
                        self.label56=Label(self.background1,text=j,font=self.myFont1)
                        self.label56.place(x=540,y=550)
                        self.clicka=Button(self.background1,text="Delete",command=self.delete,font=self.myFont)
                        self.clicka.place(x=870,y=500)
                    else:

                        messagebox.showinfo("Delete", "No record found!")
                except Exception as e:
                    print(e)
        if(self.var.get()==3):
            suspect_detail=self.search.get()
            if(suspect_detail!=""):
                try:

                    connection=connect(host="localhost",user="root",passwd='root',db='court_room')
                    cursor=connection.cursor()
                    sql=('select * from suspect where f_name="%s" or l_name="%s"  or phone_nummber="%s" or case_number="%s" ' %(suspect_detail,suspect_detail,suspect_detail,suspect_detail))
                    cursor.execute(sql)
                    result=cursor.fetchone()
                    print(result)
                    if(result is not None):
                        result=list(result)
                        a=result[0]
                        b=result[1]
                        c=result[2]
                        d=result[3]
                        self.label65=Label(self.background1,text="Suspect Name",font=self.myFont1)
                        self.label65.place(x=400,y=100)
                        self.label66=Label(self.background1,text=a,font=self.myFont1)
                        self.label66.place(x=540,y=100)
                        self.label67=Label(self.background1,text="Last Name",font=self.myFont1)
                        self.label67.place(x=400,y=150)
                        self.label68=Label(self.background1,text=b,font=self.myFont1)
                        self.label68.place(x=540,y=150)
                        self.label69=Label(self.background1,text="Phone no",font=self.myFont1)
                        self.label69.place(x=400,y=200)
                        self.label70=Label(self.background1,text=c,font=self.myFont1)
                        self.label70.place(x=540,y=200)
                        self.label71=Label(self.background1,text="Case ID",font=self.myFont1)
                        self.label71.place(x=400,y=250)
                        self.label72=Label(self.background1,text=d,font=self.myFont1)
                        self.label72.place(x=540,y=250)
                        self.clicka=Button(self.background1,text="Delete",command=self.delete,font=self.myFont)
                        self.clicka.place(x=870,y=500)
                    else:

                        messagebox.showinfo("Delete", "No record found!")

                except Exception as e:
                    print(e)
        if(self.var.get()==4):
            victim_detail=self.search.get()
            if(victim_detail != ""):
                try:
                    connection=connect(host="localhost",user="root",passwd='root',db='court_room')
                    cursor=connection.cursor()

                    sql=('select * from victim where f_name="%s" or l_name="%s" or phone_nummber="%s" or case_number="%s"' %(victim_detail,victim_detail,victim_detail,victim_detail))

                    cursor.execute(sql)
                    result=cursor.fetchone()

                    if(result is not None):
                        result=list(result)
                        a=result[0]
                        b=result[1]
                        c=result[2]
                        d=result[3]
                        self.label57=Label(self.background1,text="Victim Name",font=self.myFont1)
                        self.label57.place(x=400,y=100)
                        self.label58=Label(self.background1,text=a,font=self.myFont1)
                        self.label58.place(x=540,y=100)
                        self.label59=Label(self.background1,text="Last Name",font=self.myFont1)
                        self.label59.place(x=400,y=150)
                        self.label60=Label(self.background1,text=b,font=self.myFont1)
                        self.label60.place(x=540,y=150)
                        self.label61=Label(self.background1,text="Phone no",font=self.myFont1)
                        self.label61.place(x=400,y=200)
                        self.label62=Label(self.background1,text=c,font=self.myFont1)
                        self.label62.place(x=540,y=200)
                        self.label63=Label(self.background1,text="Case ID",font=self.myFont1)
                        self.label63.place(x=400,y=250)
                        self.label64=Label(self.background1,text=d,font=self.myFont1)
                        self.label64.place(x=540,y=250)
                        self.clicka=Button(self.background1,text="Delete",command=self.delete,font=self.myFont)
                        self.clicka.place(x=870,y=500)
                    else:

                        messagebox.showinfo("Delete", "No record found!")
                except Exception as e:
                    print(e)
obj=GUI()
obj.mainloop()
