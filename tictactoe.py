from tkinter import *
import sqlite3  as db
import random 

def Drop():
    con=db.connect("gameData.db")
    cur=con.cursor()
    cur.execute('drop table playerData')

def close():
    print(NameX.get())
    con=db.connect("gameData.db")
    cur=con.cursor()
    cur.execute("create table playerData(NameX varchar,NameO varchar )")
    cur.execute('insert into playerData values(?,?)',(NameX.get(),NameO.get()))
    con.commit()
    cur.execute('select * from playerData')
    t=(cur.fetchall())
    windowE.destroy()
    game()
    
def E():
    heading=Label(windowE,text="Welcome to TicTacToe Game",font=("arial",20),bg="Lime green",fg="green").grid(row=0,column=1)
    l4=Label(windowE,text="Enter Players Name",font=("arial",20),bg="Lime green",fg="green").grid(row=1,column=1,ipady=10)

    lP1=Label(windowE,text="Player X",font=("arial",20),bg="Lime green",fg="green").grid(row=2,column=0,ipady=10,ipadx=50)
    ent = Entry(windowE,textvariable=NameX,font=('arial',20),bg="pink",fg="green").grid(row=2,column=1,pady=10)

    lP2=Label(windowE,text="Player O",font=("arial",20),bg="Lime green",fg="green").grid(row=3,column=0,ipady=10,ipadx=50)
    ent = Entry(windowE,textvariable=NameO,font=('arial',20),bg="pink",fg="green").grid(row=3,column=1,pady=10)                                             

    button=Button(windowE,text="OK",font=("arial",20),command=close,fg="blue").grid(row=4,column=1,pady=10)
    l5=Label(windowE,text="A siddhant shah production",bg="green",fg="lime green").grid(row=5,column=1,pady=40)
    mainloop() 

def game():
    
    def win(X):
        def playagain():
            window.destroy()        
            windowW.destroy()
            game()
        
        def close2():
            window.destroy()
            windowW.destroy()
        
            
        windowW =Tk()

        windowW.config(bg = "lime green")
        windowW.geometry('700x350+250+120')

        l2=Label(windowW,font=("bold",40),text=X,fg="#008000",bg="Lime green").pack(pady=50,padx=200)
        l3=Label(windowW,font=("bold",50),text="Winner!",fg="#008000",bg="Lime green").pack()

        b3=Button(windowW,text="Play again",border=0.2,font=("bold",25),fg="#008000",bg="Lime green",command=playagain).pack(side="left",padx=15)
        b2=Button(windowW,text="Quit",border=0.2,font=("bold",25),fg="#008000",bg="Lime green",command=close2).pack(side="right",padx=15)
        mainloop()

    def click(n,butto):
      #n=textvariable
        lis=[]
        print(n.get())
        def computer():
            
            for j in (a,b,c,d,e,f,g,h,i):
                 
                if(j.get()==""):
                    lis.append(j)
             
                        
        
        if((TurnName.get())==(X+"  Turn")):
            n.set("X")
            TurnName.set(O+" Turn")
            butto.config(fg="red")
            butto.config(state="disable")
            Winer=X
            
        elif("computer"== O):
            computer()
                   
            ComputerSelect=(random.choice(lis))
            ComputerSelect.set("O")
            
            TurnName.set(X+"  Turn")
            Winer=O


        else:

            n.set("O")
            TurnName.set(X+"  Turn")
            Winer=O
            butto.config(fg="red")
            butto.config(state="disable")
            
        
        #i know these codes can be make to one  line but i have think to think of recursive to solve this i try it in next version
        if((a.get()==b.get()==c.get() =="X") or (a.get()==b.get()==c.get() =="O")):
            win(Winer)
            
        elif((a.get()==i.get()==e.get() =="X") or (a.get()==i.get()==e.get() =="O")):
            win(Winer)

        elif((g.get()==e.get()==c.get() =="X") or (g.get()==e.get()==c.get() =="O")):
            win(Winer)

        elif((f.get()==d.get()==e.get() =="X") or (f.get()==d.get()==e.get() =="O")):
            win(Winer)

        elif((i.get()==h.get()==g.get() =="X") or (i.get()==h.get()==g.get() =="O")):
            win(Winer)

        elif((a.get()==d.get()==g.get() =="X") or (a.get()==d.get()==g.get() =="O")):
            win(Winer)

        elif((h.get()==b.get()==e.get() =="X") or (h.get()==b.get()==e.get() =="O")):
            win(Winer)

        elif((i.get()==f.get()==c.get() =="X") or (i.get()==f.get()==c.get() =="O")):
            win(Winer)
            
    window = Tk()
    window.config(bg = "green")
    TurnName = StringVar()

    a = StringVar()
    b = StringVar()
    c = StringVar()
    d = StringVar()
    e = StringVar()
    f = StringVar()
    g = StringVar()
    h = StringVar()    
    i = StringVar()

    winner = []

    con=db.connect("gameData.db")
    cur=con.cursor()

    cur.execute('select * from playerData')
    t=(cur.fetchall())

    X=t[0][0]
    O=t[0][1]
    
    TurnName.set(X+"  Turn")

    
    buttonX = 9
    buttony = 3    
    buttonBg ="Lime green"
    buttonFg = "green"
    window.geometry('860x690+220+0')
    frame=Frame(window)
    frame.grid(row=0,column=1)

    l=Label(frame,textvariable=TurnName,font=("arial",15),bg="yellow",fg="green").grid(row=0,column=0)    
        
    #buttons
    #i know these button can be make to one but i have think wait for  the next version,i will not disappoint you

    b0= Button(window,border="0",textvariable=a,font=("arial",40),width=buttonX,height=buttony,bg=buttonBg,command=lambda: click(a,b0))
    b0.grid(row=1,column=0,padx=1,pady=1)

    b1= Button(window,border="0",textvariable=b,font=("arial",40),width=buttonX,height=buttony,bg=buttonBg,command=lambda: click(b,b1))
    b1.grid(row=1,column=1,padx=1,pady=1)

    b2= Button(window,border="0",textvariable=c,font=("arial",40),width=buttonX,height=buttony,bg=buttonBg,command=lambda: click(c,b2))
    b2.grid(row=1,column=2,padx=1,pady=1)

    b3= Button(window,border="0",textvariable=d,font=("arial",40),width=buttonX,height=buttony,bg=buttonBg,command=lambda: click(d,b3))
    b3.grid(row=2,column=0,padx=1,pady=1)

    b4= Button(window,border="0",textvariable=e,font=("arial",40),width=buttonX,height=buttony,bg=buttonBg,command=lambda: click(e,b4))
    b4.grid(row=2,column=1,padx=1,pady=1)

    b5= Button(window,border="0",textvariable=f,font=("arial",40),width=buttonX,height=buttony,bg=buttonBg,command=lambda: click(f,b5))
    b5.grid(row=2,column=2,padx=1,pady=1)

    b6= Button(window,border="0",textvariable=g,font=("arial",40),width=buttonX,height=buttony,bg=buttonBg,command=lambda: click(g,b6))
    b6.grid(row=3,column=0,padx=1,pady=1)

    b7= Button(window,border="0",textvariable=h,font=("arial",40),width=buttonX,height=buttony,bg=buttonBg,command=lambda: click(h,b7))
    b7.grid(row=3,column=1,padx=1,pady=1)

    b8= Button(window,border="0",textvariable=i,font=("arial",40),width=buttonX,height=buttony,bg=buttonBg,command=lambda: click(i,b8))
    b8.grid(row=3,column=2)
    mainloop()

#main

windowE =Tk()
NameX = StringVar()
NameO = StringVar()
windowE.config(bg = "lime green")
windowE.geometry('700x350+250+120')
E()
Drop()
