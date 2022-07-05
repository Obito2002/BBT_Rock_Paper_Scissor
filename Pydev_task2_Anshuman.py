#Pydev  task->2
#Anshuman Mishra 1st yr IT
import os
import sys
from tkinter import * 
from PIL import ImageTk, Image 
import random

#creating the intro window
root=Tk()

root.geometry("800x600")
root.title("THE GAME OF CHANCES ")
root.iconbitmap("c:/users/ANSHUMAN/desktop/task_2/bazinga_icon.ico")
global avatar_list
#Importing the avatar
avatar1=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/nikola-tesla@64px.png"))
avatar2=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/charlie-chaplin@64px.png"))
avatar3=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/batman@64px.png"))
avatar4=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/trinity@64px.png"))
avatar5=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/robot-02@64px.png"))
avatar6=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/malcolm-x@64px.png"))
avatar7=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/cristiano-ronaldo@64px.png"))

avatar_list=[avatar1,avatar2,avatar3,avatar4,avatar5,avatar6,avatar7]

#importing rock ppr scissor spock lizard 

 
global j 
j=0
global k 
k=0 

    
def new_win3(us):
    global win3
    win3=Toplevel()
    win3.geometry("900x600")
    score=us
    win3.title("THE GAME OF CHANCES ")
    win3.iconbitmap("c:/users/ANSHUMAN/desktop/task_2/bazinga_icon.ico")
    Lbl3=LabelFrame(win3,labelanchor= "n",bd=5,bg="#CDF0EA",width= 750, height= 600)
    Lbl3.pack(expand= True , fill= BOTH)
    player_score = Label(win3,
           text = ("Player Score :" + str(score)),
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
    player_score.place(relx=.36 , rely =.120 )
    exit_button=Button(win3, text= " EXIT "  , padx= 60 , pady =30 ,relief = SOLID, command= exit )
    exit_button.place(relx=.25,rely=.4)
    restart=Button(win3, text="RESTART" , padx= 60 , pady=30 ,relief = SOLID , command= restart_game )
    restart.place(relx= .6, rely = .4)


def restart_game():
    #global win3
    """win3.destroy()
    root.destroy()
    os.startfile("C:/Users/ANSHUMAN/desktop/intro_window.py")"""
    python=sys.executable
    os.execl(python, python , * sys.argv)
    
    
    



def final():
    us=user_score
    win2.destroy()
    new_win3(us)

    



def display_umove():
    rock_raw=Image.open("C:/Users/ANSHUMAN/Desktop/task_2/rock.png")
    rock0=rock_raw.resize((60,60))
    rock=ImageTk.PhotoImage(rock0)

    scissor_raw=Image.open("C:/Users/ANSHUMAN/Desktop/task_2/scissor.png")
    scissor0=scissor_raw.resize((60,60))
    scissor=ImageTk.PhotoImage(scissor0)

    paper_raw=Image.open("C:/Users/ANSHUMAN/Desktop/task_2/paper.png")
    paper0=paper_raw.resize((60,60))
    paper=ImageTk.PhotoImage(paper0)

    liz_raw=Image.open("C:/Users/ANSHUMAN/Desktop/task_2/lizard.png")
    liz0=liz_raw.resize((60,60))
    liz=ImageTk.PhotoImage(liz0)

    spock_raw=Image.open("C:/Users/ANSHUMAN/Desktop/task_2/spock.png")
    spock0=spock_raw.resize((60,60))
    spock=ImageTk.PhotoImage(spock0)

    global moves
    moves= [rock , scissor , paper , liz , spock ]
    global user_move
    user_move=Label(win2,image=moves[j],width=60,height=60)
    user_move.place(relx= .35 , rely =.45 )

def display_cmove():
    global moves
    global k
    global comp_move
    comp_move=Label(win2,image=moves[k])
    comp_move.place(relx= .6, rely = .45)

global user_score
user_score =0

global comp_score
comp_score=0

global diff
diff = 0
global i 
i=0
global win2

def deletewin2():
    global diff
    global win2
    if diff==3:
        final()
#Game window
def game_win(num):
    uname=name.get()
    
    
    global win2                                   
    win2=Toplevel()     
    
    win2.geometry("900x600")                                    
    win2.title("THE GAME OF CHANCES ")
    win2.iconbitmap("c:/users/ANSHUMAN/desktop/task_2/bazinga_icon.ico")
    
    Lbl2=LabelFrame(win2,text= "The Match",font= ('century 20 bold '),labelanchor= "n",bd=5,bg="#CDF0EA",width= 750, height= 600)
    Lbl2.pack(expand= True , fill= BOTH)

    r1=Button(win2, text= " Rock  "  , padx= 40 , pady =20,  relief = SOLID,command=rock )
    r1.place(relx= 0.08 ,rely=.1)
    sci1=Button(win2, text= "Scissor"  , padx= 40 , pady =20,relief = SOLID, command=scissor )
    sci1.place(relx= 0.08 ,rely=.22)
    p1=Button(win2, text= " Paper "  , padx= 40 , pady =20 ,relief = SOLID, command=paper )
    p1.place(relx= 0.08 ,rely=.34)
    liz1=Button(win2, text= "Lizzard"  , padx= 40 , pady =20 ,relief = SOLID, command= lizzard)
    liz1.place(relx= 0.08 ,rely=.46)
    spock1=Button(win2, text= " Spock "  , padx= 40 , pady =20 ,relief = SOLID, command= spock )
    spock1.place(relx= 0.08 ,rely=.58)

    r2=Button(win2, text= " Rock  "  , padx= 40 , pady =20 ,relief= SUNKEN )
    r2.place(relx=0.79 ,rely=.1)
    sci2=Button(win2, text= "Scissor"  , padx= 40 , pady =20 ,relief= SUNKEN)
    sci2.place(relx=0.79 ,rely=.22)
    p2=Button(win2, text= " Paper "  , padx= 40 , pady =20,relief= SUNKEN )
    p2.place(relx=0.79 ,rely=.34)
    liz2=Button(win2, text= "Lizzard"  , padx= 40 , pady =20,relief= SUNKEN )
    liz2.place(relx=0.79 ,rely=.46)
    spock2=Button(win2, text= " Spock "  , padx= 40 , pady =20,relief= SUNKEN )
    spock2.place(relx=0.79 ,rely=.58)
    
    #Importing the avatar
    avatar1=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/nikola-tesla@64px.png"))
    avatar2=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/charlie-chaplin@64px.png"))
    avatar3=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/batman@64px.png"))
    avatar4=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/trinity@64px.png"))
    avatar5=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/robot-02@64px.png"))
    avatar6=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/malcolm-x@64px.png"))
    avatar7=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/cristiano-ronaldo@64px.png"))

    avatar_list=[avatar1,avatar2,avatar3,avatar4,avatar5,avatar6,avatar7]
    show_avatar2=Label(win2,image=  avatar_list[num])
    show_avatar2.place(relx=.26,rely=.1)
    avatarC=ImageTk.PhotoImage(Image.open("C:/Users/ANSHUMAN/Desktop/task_2/avatars/robot-01@64px.png"))
    avatarComp=Label(win2,image= avatarC)
    avatarComp.place(relx=.6, rely=.1)

    vs=Label(win2,text="VS", font= ('century 15 bold ') , bg = "#C490E4")
    vs.place(relx= .49, rely =.35)

    namelbl=Label(win2, text = uname , font='century 12 bold ' , bg="#C490E4",borderwidth = 2,relief=SOLID)
    namelbl.place(relx=0.28,rely=0.35)

    computerlbl=Label(win2, text= "Machine",font ='century 12 bold ', bg= "#C490E4",borderwidth = 2, relief=SOLID)
    computerlbl.place(relx=.635,rely=.35)

    
    display_umove()
    display_cmove()
    global result_window
    result_window = Label(win2,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
    result_window.place(relx=.3655 , rely =.60 )

    points=Label(win2,text="POINTS :", font='century 18 bold ', bg='#CDF0EA')
    points.place(relx=.1 , rely=.8)
    
    global uscore
    global user_score
    global comp_score
    uscore=Label(win2,text="0" ,font = "normal 18 bold",bg = "white",width = 10 ,borderwidth = 2,relief = "solid")
    uscore.place(relx=.3, rely=.8)

    separator = Label (win2, text =":", font='century 22 bold ', bg='#CDF0EA' )
    separator.place(relx=.5,rely=.8)

    global cscore
    cscore=Label(win2,text="0" ,font = "normal 18 bold",bg = "white",width = 10 ,borderwidth = 2,relief = "solid")
    cscore.place(relx=.54, rely=.8)
     
    
    win2.mainloop()



#rock ppr sci spo liz button definitions
def rock():
    comp=random.randint(0,4)
    global k 
    k=comp
    global j 
    j=0
    user_move.destroy()
    comp_move.destroy()
    display_umove()
    display_cmove()
    
    global user_score
    global comp_score
    global diff
    if diff>= 3:
        deletewin2()

    else  :
        if comp == 0 :
            result_window.config(text="Tie")
            result_window.place(relx=.3655 , rely =.60 )
        elif comp == 2 or comp == 4:
            result_window.config(text="You Lost!")
            result_window.place(relx=.3655 , rely =.60 )
            comp_score+=1
            cscore.config(text=str(comp_score))
            cscore.place(relx=.54, rely=.8)
            diff+=1

        elif comp == 1 or comp == 3:
            result_window.config(text="You Won!")
            result_window.place(relx=.3655 , rely =.60 )
            user_score+=1
            uscore.config(text=str(user_score))
            uscore.place(relx=.3, rely=.8)
        


def scissor():
    comp=random.randint(0,4)
    global k 
    k=comp
    global j 
    j=1
    user_move.destroy()
    comp_move.destroy()
    display_umove()
    display_cmove()

    global user_score
    global comp_score
    global diff
    if diff>= 3:
        deletewin2()
    else:
        if comp == 1 :
            result_window.config(text="Tie")
            result_window.place(relx=.3655 , rely =.60 )
        elif comp == 0 or comp == 4:
            result_window.config(text="You Lost!")
            result_window.place(relx=.3655 , rely =.60 )
            comp_score+=1
            cscore.config(text=str(comp_score))
            cscore.place(relx=.54, rely=.8)
            diff+=1
        elif comp == 2 or comp == 3:
            result_window.config(text="You Won!")
            result_window.place(relx=.3655 , rely =.60 )
            user_score+=1
            uscore.config(text=str(user_score))
            uscore.place(relx=.3, rely=.8)

def paper():
    comp=random.randint(0,4)
    global k 
    k=comp
    global j 
    j=2
    user_move.destroy()
    comp_move.destroy()
    display_umove()
    display_cmove()
    
    global user_score
    global comp_score
    global diff
    if diff>= 3:
        deletewin2()

    else:
        if comp == 2 :
            result_window.config(text="Tie")
            result_window.place(relx=.3655 , rely =.60 )
        elif comp == 1 or comp == 3:
            result_window.config(text="You Lost!")
            result_window.place(relx=.3655 , rely =.60 )
            comp_score += 1
            cscore.config(text=str(comp_score))
            cscore.place(relx=.54, rely=.8)
            diff+=1
        elif comp == 4 or comp == 0:
            result_window.config(text="You Won!")
            result_window.place(relx=.3655 , rely =.60 ) 
            user_score+=1     
            uscore.config(text=str(user_score))
            uscore.place(relx=.3, rely=.8)  

def lizzard():
    comp=random.randint(0,4)
    global k 
    k=comp
    global j 
    j=3
    user_move.destroy()
    comp_move.destroy()
    display_umove()
    display_cmove()
    
    global user_score
    global comp_score
    global diff
    if diff>= 3:
        deletewin2()
    else:

        if comp == 3 :
            result_window.config(text="Tie")
            result_window.place(relx=.3655 , rely =.60 )
        elif comp == 0 or comp == 1:
            result_window.config(text="You Lost!")
            result_window.place(relx=.3655 , rely =.60 )
            comp_score+=1
            cscore.config(text=str(comp_score))
            cscore.place(relx=.54, rely=.8)
            diff+=1
        elif comp == 2 or comp == 4:
            result_window.config(text="You Won!")
            result_window.place(relx=.3655 , rely =.60 )
            user_score+=1
            uscore.config(text=str(user_score))
            uscore.place(relx=.3, rely=.8)

def spock():
    comp=random.randint(0,4)
    global k 
    k=comp
    global j 
    j=4
    user_move.destroy()
    comp_move.destroy()
    display_umove()
    display_cmove()
    
    global user_score
    global comp_score
    global diff
    if diff>= 3:
        deletewin2()
    else:
        if comp == 4 :
            result_window.config(text="Tie")
            result_window.place(relx=.3655 , rely =.60 )
        elif comp == 3 or comp == 2:
            result_window.config(text="You Lost!")
            result_window.place(relx=.3655 , rely =.60 )
            comp_score+=1
            cscore.config(text=str(comp_score))
            cscore.place(relx=.54, rely=.8)
            diff+=1
        elif comp == 0 or comp == 1:
            result_window.config(text="You Won!")
            result_window.place(relx=.3655 , rely =.60 )
            user_score+=1
            uscore.config(text=str(user_score))
            uscore.place(relx=.3, rely=.8)




#avatar select buttons next and back
def forward():
    show_avatar.destroy()
    global i 
    if i<6:
        i +=1
    show_avtr()
def back():
    show_avatar.destroy()
    global i 
    if i>0:
        i -=1
    show_avtr()


#Label for the in-game boundary / styling the window :
Lbl=LabelFrame(root, text= "A GAME OF \nCHANCES",font= ('century 20 bold '),labelanchor= "n",bd=5,bg="#CDF0EA",width= 750, height= 450)
Lbl.pack(expand= True , fill= BOTH)

quote=Label(Lbl, text="\" U think you can defeat me humaaaaaan ?! ........ Haa...Highly illogical !! \"",font= ("Helvetica 14 italic bold" ) , bg="#CDF0EA"   )
quote.place(relx=.08, rely = .02)

quote2= Label(Lbl, text= "Anyways.. as you have summoned me, lets settle this...... " , font=("Helvetica 14 bold") , bg="#CDF0EA")
quote2.place(relx=0.18, rely=.12)


def show_avtr():
    global avatar_list
    global  show_avatar
    show_avatar=Label(Lbl,image=avatar_list[i])
    show_avatar.place(relx=0.42, rely=.2)

show_avtr()

#Nxt and Back button for srooling through the avatars
nxt=Button(Lbl , text=" >> ",font= ('century 10 bold '), padx=7 , pady=7 ,bg="#F7DBF0", command= forward)
back=Button(Lbl , text=" << ",font= ('century 10 bold '), padx=7 , pady=7 ,bg ="#F7DBF0",command = back)
nxt.place(relx=.599999,rely=.32)
back.place(relx=.34,rely=.32)

#Label teling the user to select their avatar and enter user name in the box below
enter=Label(Lbl,text= "Choose your avatar \n & \n Enter your name :",font= ('century 10 bold ') , bg="#CDF0EA")
enter.place(relx=.42 , rely=.47)

#name entry box
def get_name():
    global name 
    name=Entry(Lbl,width=48,borderwidth=5)
    name.place(relx=.32 , rely= .6) 
    
get_name()




#The start game button
start=Button(Lbl, text="Begin!" ,font= ('century 15 bold '), padx=80 , pady=30 , bg= "#BEAEE2", command= lambda : game_win(i) )
start.place(relx=.36, rely=.7)

root.mainloop()

