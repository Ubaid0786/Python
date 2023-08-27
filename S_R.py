from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")
    
def logout():
    os.system("shutdown -l")  # Corrected the shutdown command for logout
    
def shut_down():
     os.system("shutdown /s /t 1")
    
st = Tk()  # Corrected the case of Tk()
st.title("shutDown App")
st.geometry("500x500")
st.config(bg="grey")
r_button = Button(st, text="Restart", font=("Times New Roman", 20, "bold"),
                  relief=RAISED, cursor="plus", command=restart)
r_button.place(x=150, y=60, height=50, width=200)

rt_button = Button(st, text="Restart Time", font=("Times New Roman", 20, "bold"),
                   relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=150, y=170, height=50, width=200)

lg_button = Button(st, text="Log out", font=("Times New Roman", 20, "bold"), 
                   relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=150, y=270, height=50, width=200)

st_button = Button(st, text="Shut down", font=("Times New Roman", 20, "bold"), 
                   relief=RAISED, cursor="plus", command=shut_down)
st_button.place(x=150, y=370, height=50, width=200)

st.mainloop()