import turtle
turtle.bgcolor("black")
turtle.pensize(5)
turtle.speed(0.5)
turtle.shape("turtle")

for i in range(6):
    for colors in ["crimson","cyan","indigo","gold","magenta","chartreuse","teal"]:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)
       
t=turtle.Turtle()
t.penup()
t.goto(0,-300)
t.pendown()
t.color("white")
style=("Comic Sans MS",30,"normal")
t.write("Welcome To TurboGames\n Where dreams come to life",font=style,align="center",move=True)

t.hideturtle()
turtle.exitonclick()


#Login page

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file="C:\\Users\\pc\\Pictures\\Project\\game4.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open("C:\\Users\\pc\\Pictures\\Project\\game_logo.png") 
        img1=img1.resize((90,80),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=185,width=100,height=90)

        get_str=Label(frame,text="Welcome to TurboGamez",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=20,y=110)

        #label

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        

        #small logos

        img2=Image.open("C:\\Users\\pc\\Pictures\\Project\\Icon.png") 
        img2=img2.resize((20,20),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img3=Image.open("C:\\Users\\pc\\Pictures\\Project\\Password.png") 
        img3=img3.resize((20,20),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lblimg1.place(x=650,y=393,width=25,height=25)

        #login button

        loginbtn=Button(frame,command=self.login,text="Login",font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")   
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        
        #register button

        registerbtn=Button(frame,text="Don't have an account? Register",font=("Times New Roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")   
        registerbtn.place(x=65,y=350,width=200)

        #forgot password

        forgotbtn=Button(frame,text="Forgot Password?",font=("Times New Roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")   
        forgotbtn.place(x=85,y=380,width=160)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","Fill in the information")
        elif self.txtuser.get()=="Turbocycle" and self.txtpass.get()=="abcd":
            messagebox.showinfo("Success","Welcome to TurboGamez")
            self.root.destroy()
            return
        else:
            messagebox.showerror("Invalid","Enter the correct username and password")

if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()



from tkinter import *
from tkinter import ttk
import tkinter
import mysql.connector
from mysql.connector import connection
from tkinter import messagebox
from mysql.connector import cursor



class TurboGameSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Turbo Gamez System")
        self.root.geometry("1550x800+0+0")


        #==========Variables===============

        self.member_var=StringVar()
        self.refnumber_var=StringVar()
        self.username_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.userid_var=StringVar()
        self.region_var=StringVar()
        self.platform_var=StringVar()
        self.serialnumber_var=StringVar()
        self.title_var=StringVar()
        self.publisher_var=StringVar()
        self.releasedate_var=StringVar()
        self.version_var=StringVar()
        self.lastupdate_var=StringVar()
        self.futureupdate_var=StringVar()
        self.price_var=StringVar()



        lbltitle=Label(self.root,text="TURBO GAMEZ",bg="lavender",fg="purple",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="lavender")
        frame.place(x=0,y=130,width=1550,height=400)

        #Data Frame Left

        DataFrameLeft=LabelFrame(frame,text="Games Information",bg="lavender",fg="purple",bd=20,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=360)

        lblMember=Label(DataFrameLeft,bg="lavender",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",15,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin","MVP++","VIP","Normal","First timer")
        comMember.grid(row=0,column=1)

        lblPRN=Label(DataFrameLeft,bg="lavender",text="Reference No.",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPRN.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.refnumber_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        username=Label(DataFrameLeft,bg="lavender",text="Username",font=("times new roman",15,"bold"),padx=2,pady=6)
        username.grid(row=2,column=0,sticky=W)
        txtusername=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.username_var,width=29)
        txtusername.grid(row=2,column=1)

        firstname=Label(DataFrameLeft,bg="lavender",text="First Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        firstname.grid(row=3,column=0,sticky=W)
        txtfirstname=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.firstname_var,width=29)
        txtfirstname.grid(row=3,column=1)

        lastname=Label(DataFrameLeft,bg="lavender",text="Last Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        lastname.grid(row=4,column=0,sticky=W)
        txtlastname=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.lastname_var,width=29)
        txtlastname.grid(row=4,column=1)

        userid=Label(DataFrameLeft,bg="lavender",text="User ID number",font=("times new roman",15,"bold"),padx=2,pady=6)
        userid.grid(row=5,column=0,sticky=W)
        txtuserid=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.userid_var,width=29)
        txtuserid.grid(row=5,column=1)

        lblRegion=Label(DataFrameLeft,bg="lavender",text="Region",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblRegion.grid(row=6,column=0,sticky=W)
        comRegion=ttk.Combobox(DataFrameLeft,textvariable=self.region_var,font=("times new roman",15,"bold"),width=27,state="readonly")
        comRegion["value"]=("Africa","Asia","Europe","Oceania","North America","South America")
        comRegion.grid(row=6,column=1)

        lblPlatform=Label(DataFrameLeft,bg="lavender",text="Platform",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPlatform.grid(row=7,column=0,sticky=W)
        comPlatform=ttk.Combobox(DataFrameLeft,textvariable=self.platform_var,font=("times new roman",15,"bold"),width=27,state="readonly")
        comPlatform["value"]=("Windows","MacOS","PS4","PS5","Nintendo Switch","Linux","XBOX One","XBOX Series S/X")
        comPlatform.grid(row=7,column=1) #29:09

        gamenumber=Label(DataFrameLeft,bg="lavender",text="Serial Number",font=("times new roman",15,"bold"),padx=2,pady=6)
        gamenumber.grid(row=0,column=3,sticky=W)
        txtgamenumber=Entry(DataFrameLeft,textvariable=self.serialnumber_var,font=("times new roman",15,"bold"),width=28)
        txtgamenumber.grid(row=0,column=4)
 
        gamename=Label(DataFrameLeft,bg="lavender",text="Game Title",font=("times new roman",15,"bold"),padx=2,pady=6)
        gamename.grid(row=1,column=3,sticky=W)
        txtgamename=Entry(DataFrameLeft,textvariable=self.title_var,font=("times new roman",15,"bold"),width=28)
        txtgamename.grid(row=1,column=4)

        publisher=Label(DataFrameLeft,bg="lavender",text="Publisher",font=("times new roman",15,"bold"),padx=2,pady=6)
        publisher.grid(row=2,column=3,sticky=W)
        txtpublisher=Entry(DataFrameLeft,textvariable=self.publisher_var,font=("times new roman",15,"bold"),width=28)
        txtpublisher.grid(row=2,column=4)

        releasedate=Label(DataFrameLeft,bg="lavender",text="Release date",font=("times new roman",15,"bold"),padx=2,pady=6)
        releasedate.grid(row=3,column=3,sticky=W)
        txtreleasedate=Entry(DataFrameLeft,textvariable=self.releasedate_var,font=("times new roman",15,"bold"),width=28)
        txtreleasedate.grid(row=3,column=4)

        currentversion=Label(DataFrameLeft,bg="lavender",text="Version",font=("times new roman",15,"bold"),padx=2,pady=6)
        currentversion.grid(row=4,column=3,sticky=W)
        txtcurrentversion=Entry(DataFrameLeft,textvariable=self.version_var,font=("times new roman",15,"bold"),width=28)
        txtcurrentversion.grid(row=4,column=4)

        lupdate=Label(DataFrameLeft,bg="lavender",text="Last Update",font=("times new roman",15,"bold"),padx=2,pady=6)
        lupdate.grid(row=5,column=3,sticky=W)
        txtlupdate=Entry(DataFrameLeft,textvariable=self.lastupdate_var,font=("times new roman",15,"bold"),width=28)
        txtlupdate.grid(row=5,column=4)

        fupdate=Label(DataFrameLeft,bg="lavender",text="Future Update",font=("times new roman",15,"bold"),padx=2,pady=6)
        fupdate.grid(row=6,column=3,sticky=W)
        txtfupdate=Entry(DataFrameLeft,textvariable=self.futureupdate_var,font=("times new roman",15,"bold"),width=28)
        txtfupdate.grid(row=6,column=4)

        price=Label(DataFrameLeft,bg="lavender",text="Price",font=("times new roman",15,"bold"),padx=2,pady=6)
        price.grid(row=7,column=3,sticky=W)
        txtprice=Entry(DataFrameLeft,textvariable=self.price_var,font=("times new roman",15,"bold"),width=28)
        txtprice.grid(row=7,column=4)



        #Data Frame Right

        DataFrameRight=LabelFrame(frame,text="Game details",bg="lavender",fg="purple",bd=20,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameRight.place(x=910,y=5,width=600,height=360)

        self.txtBox=Text(DataFrameRight, font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listGames=["Minecraft","Grand Theft Auto 5","Red Dead Redemption II","Fortnite","FIFA 21","Overwatch","Sims 4","Genshin Impact","Animal Crossing","WWE 2K20","WWE 2K19","WWE 2K Battlegrounds","The Legend of Zelda: Breath of the Wild","The Last Of Us 2","God Of War","CyberPunk","Marvel's Avengers","Marvel's Spider-Man: Miles Morales","Watch Dogs: Legion","Assassin's Creed Valhalla: Wrath of the Druids","Assassin's Creed: The Rebel Collection","Among Us","Rocket League","Call of Duty: Warzone","Call of Duty:Cold War","Apex Legends","Hitman 3","It Takes Two","NBA 2K20","Among Us","Ghost of Tsushima","Fall Guys","Tony Hawk's Pro Skater","Fall Guys","Microsoft Flight Simulator","Crash Bandicoot 4: It's About Time","Resident Evil 3","Valorant"]


        def SelectGame(event=""):
            value1=str(listbox.get(listbox.curselection()))
            x=value1
            if (x=="Minecraft"):
                self.serialnumber_var.set("TURBO1")
                self.title_var.set("Minecraft")
                self.publisher_var.set("Mojang")
                self.releasedate_var.set("18 November 2011")
                self.version_var.set("1.17.1")
                self.lastupdate_var.set("June 8 2021")
                self.futureupdate_var.set("December 2021")
                self.price_var.set("26.95$")

            if (x=="Grand Theft Auto 5"):
                self.serialnumber_var.set("Turbo2")
                self.title_var.set("Grand Theft Auto 5")
                self.publisher_var.set("Rockstar Games")
                self.releasedate_var.set("17-09-2013")
                self.version_var.set("To be filled")
                self.lastupdate_var.set("To be filled")
                self.futureupdate_var.set("To be filled")
                self.price_var.set("30$")

            if (x=="Sims 4"):
                self.serialnumber_var.set("Turbo7")
                self.title_var.set("Sims 4")
                self.publisher_var.set("EA Games")
                self.releasedate_var.set("2-9-2014")
                self.version_var.set("Sims 411 Recap")
                self.lastupdate_var.set("6-8-2021")
                self.futureupdate_var.set("Not announced")
                self.price_var.set("360$ with all expansions")

            if (x=="WWE 2K20"):
                self.serialnumber_var.set("Turbo10")
                self.title_var.set("WWE 2K20")
                self.publisher_var.set("2K")
                self.releasedate_var.set("22-10-2019")
                self.version_var.set("2.5")
                self.lastupdate_var.set("Nil")
                self.futureupdate_var.set("Never")
                self.price_var.set("22$")

            if (x=="Genshin Impact"):
                self.serialnumber_var.set("Turbo8")
                self.title_var.set("Genshin Impact")
                self.publisher_var.set("MiHoYo")
                self.releasedate_var.set("28-09-2020")
                self.version_var.set("To be filled")
                self.lastupdate_var.set("To be filled")
                self.futureupdate_var.set("To be filled")
                self.price_var.set("Free")

            if (x=="Among Us"):
                self.serialnumber_var.set("Turbo33")
                self.title_var.set("Among Us")
                self.publisher_var.set("InnerSloth LLC")
                self.releasedate_var.set("15 June 2018")
                self.version_var.set("2021.6.30")
                self.lastupdate_var.set("1 month ago")
                self.futureupdate_var.set("To be announced")
                self.price_var.set("5$")

            if (x=="Fortnite"):
                self.serialnumber_var.set("Turbo4")
                self.title_var.set("Fortnite")
                self.publisher_var.set("Epic Games")
                self.releasedate_var.set("25-07-2017")
                self.version_var.set("Ch2S7")
                self.lastupdate_var.set("8-6-2021")
                self.futureupdate_var.set("12-9-2021")
                self.price_var.set("Free")

            

                
        
        listbox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listbox.bind("<<ListboxSelect>>",SelectGame)
        listbox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listbox.yview)

        for item in listGames:
            listbox.insert(END,item)



 
        #Button Frame
        
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="lavender")
        Framebutton.place(x=0,y=530,width=1550,height=70)

        btnAddData=Button(Framebutton,text="Add Data",command=self.add_data,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,text="Show Data",command=self.showData,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,text="Update",command=self.update,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,text="Delete",command=self.delete,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,text="Reset",command=self.reset,font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,text="Exit",font=("arial",12,"bold"),command=self.exit,width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5) 


        #Information Frame
        
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="lavender")
        FrameDetails.place(x=0,y=600,width=1550,height=195)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="lavender")
        Table_frame.place(x=0,y=2,width=1480,height=510)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,columns=("membertype","regno","username","firstname","lastname","userid","region","platform","serialno","title","publisher","releasedate","version","lastupdate","futureupdate","price"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=TOP,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("regno",text="Registration Number")
        self.library_table.heading("username",text="Username")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("userid",text="User ID")
        self.library_table.heading("region",text="Region")
        self.library_table.heading("platform",text="Platform")
        self.library_table.heading("serialno",text="Serial Number")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("publisher",text="Publisher")
        self.library_table.heading("releasedate",text="Release Date")
        self.library_table.heading("version",text="Version")
        self.library_table.heading("lastupdate",text="Last Update")
        self.library_table.heading("futureupdate",text="Future Update")
        self.library_table.heading("price",text="Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("regno",width=200)
        self.library_table.column("username",width=200)
        self.library_table.column("firstname",width=200)
        self.library_table.column("lastname",width=200)
        self.library_table.column("userid",width=100)
        self.library_table.column("region",width=200)
        self.library_table.column("platform",width=100)
        self.library_table.column("serialno",width=100)
        self.library_table.column("title",width=300)
        self.library_table.column("publisher",width=300)
        self.library_table.column("releasedate",width=100)
        self.library_table.column("version",width=100)
        self.library_table.column("lastupdate",width=100)
        self.library_table.column("futureupdate",width=100)
        self.library_table.column("price",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into gamesystem values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.member_var.get(),self.refnumber_var.get(),self.username_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.userid_var.get(),self.region_var.get(),self.platform_var.get(),self.serialnumber_var.get(),self.title_var.get(),self.publisher_var.get(),self.releasedate_var.get(),self.version_var.get(),self.lastupdate_var.get(),self.futureupdate_var.get(),self.price_var.get()))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","User registered")

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update gamesystem set member=%s,username=%s,firstname=%s,lastname=%s,userid=%s,region=%s,platform=%s,serialnumber=%s,title=%s,publisher=%s,releasedate=%s,version=%s,lastupdate=%s,futureupdate=%s,price=%s where refnumber=%s",(self.member_var.get(),self.username_var.get(),self.firstname_var.get(),self.lastname_var.get(),self.userid_var.get(),self.region_var.get(),self.platform_var.get(),self.serialnumber_var.get(),self.title_var.get(),self.publisher_var.get(),self.releasedate_var.get(),self.version_var.get(),self.lastupdate_var.get(),self.futureupdate_var.get(),self.price_var.get(),self.refnumber_var.get(),))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close

        messagebox.showinfo("Task Successful","Order has been updated")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from gamesystem")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content["values"]

        self.member_var.set(row[0])
        self.refnumber_var.set(row[1])
        self.username_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.userid_var.set(row[5])
        self.region_var.set(row[6])
        self.platform_var.set(row[7])
        self.serialnumber_var.set(row[8])
        self.title_var.set(row[9])
        self.publisher_var.set(row[10])
        self.releasedate_var.set(row[11])
        self.version_var.set(row[12])
        self.lastupdate_var.set(row[13])
        self.futureupdate_var.set(row[14])
        self.price_var.set(row[15])

    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"Reference no.\t\t"+self.refnumber_var.get()+"\n")
        self.txtBox.insert(END,"Username\t\t"+self.username_var.get()+"\n")
        self.txtBox.insert(END,"First Name\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"User ID\t\t"+self.userid_var.get()+"\n")
        self.txtBox.insert(END,"Region\t\t"+self.region_var.get()+"\n")
        self.txtBox.insert(END,"Platform\t\t"+self.platform_var.get()+"\n")
        self.txtBox.insert(END,"Serial Number\t\t"+self.serialnumber_var.get()+"\n")
        self.txtBox.insert(END,"Title\t\t"+self.title_var.get()+"\n")
        self.txtBox.insert(END,"Publisher\t\t"+self.publisher_var.get()+"\n")
        self.txtBox.insert(END,"Release Date\t\t"+self.releasedate_var.get()+"\n")
        self.txtBox.insert(END,"Version\t\t"+self.version_var.get()+"\n")
        self.txtBox.insert(END,"Last Update\t\t"+self.lastupdate_var.get()+"\n")
        self.txtBox.insert(END,"Future Update\t\t"+self.futureupdate_var.get()+"\n")
        self.txtBox.insert(END,"Price\t\t"+self.price_var.get()+"\n")

    def reset(self):
        self.member_var.set("")
        self.refnumber_var.set("")
        self.username_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.userid_var.set("")
        self.region_var.set("")
        self.platform_var.set("")
        self.serialnumber_var.set("")
        self.title_var.set("")
        self.publisher_var.set("")
        self.releasedate_var.set("")
        self.version_var.set("")
        self.lastupdate_var.set("")
        self.futureupdate_var.set("")
        self.price_var.set("")
        self.txtBox.delete("1.0",END)

    def exit(self):
        iExit=tkinter.messagebox.askyesno("Turbo Game System","Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.refnumber_var.get()=="" or self.userid_var.get()=="":
            messagebox.showerror("Error","First, select the member to be deleted")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
            my_cursor=conn.cursor()
            query="delete from gamesystem where refnumber=%s"
            value=(self.refnumber_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","User has been deleted")
                 
        
                                                                                                                                        

        
        
if __name__=="__main__":
    root=Tk()
    obj=TurboGameSystem(root)
    root.mainloop()
