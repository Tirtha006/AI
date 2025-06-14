from tkinter import*
chat=Tk()
chat.title("CHATBOT")

def send():
    Message="you:"+e.get()
    user=e.get().lower()
    txt.insert(END,Message+"\n")

    if user=="hello":
        txt.insert(END,"Bot:hi\n")
    elif user=="hi" or user=="hii"or user=="hiii":
        txt.insert(END,"Bot:hello\n")
    elif user=="how are you doing?":
        txt.insert(END,"Bot:i am doing good!and you\n")
    elif user=="fine"or user=="great"or user=="good":
        txt.insert(END,"Bot:Great!how can i help you?")
    else:
        txt.insert(END,"Bot:Sorry i didnt get you")

txt=Text()
txt.grid(row=0,column=0)

e=Entry(width=100)
e.grid(row=1,column=0)

send_button=Button(text="Send",command=send)
send_button.grid(row=1,column=1)

chat.mainloop()
