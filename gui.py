from tkinter import*
import tkinter.font as font
from PIL import Image,ImageTk
import speech_to_text
import text_to_speech
import action

root=Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#7B68EE")


#ask func
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'User--->'+ user_val+"\n")
    if bot_val != None:
        text.insert(END , "BOT <---"+str(bot_val)+"\n")
    if bot_val == "ok sir, Thank you!" :
        root.destroy()

def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'User--->'+ send+"\n")
    if bot != None:
        text.insert(END , "BOT <---"+str(bot)+"\n")
    if bot == "ok sir, Thank you!" :
        root.destroy()


def del_text():
    text.delete("1.0" , "end")
    entry.delete(0, END)

#frame

frame=LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised")
frame.grid(row=0,column=1,padx=45,pady=10)
frame.config(bg="#6F8FAF")
#text label
text_label=Label(frame, text="AI Assistant",font=("comic sans ms", 14, "bold") , bg="#FFDAB9")
text_label.grid(row=0,column=0,padx=20,pady=10)

#image
image=ImageTk.PhotoImage(Image.open("avatar.jpg"))
image_label=Label(frame,image=image)
image_label.grid(row=1,column=0,pady=20)

#Adding text widget
text=Text(root,font=('courier 10 bold'), bg="#356696")
text.grid(row=2,column=0)
text.place(x=100,y=380, width=375 , height = 100)

#entry widget

entry=Entry(root , justify = CENTER)
entry.place(x=100 , y= 500 , width=375 , height= 30)


myFont = font.Font(weight="bold")

#button 1

Button1 = Button(root, text = "ASK", bg = "#356696", pady = 16 , padx = 40 , borderwidth= 3, relief = SOLID , command = ask)
Button1['font'] = myFont
Button1.place(x = 50, y= 575)



#Button2
Button2 = Button(root, text = "SEND", bg = "#356696", pady = 16 , padx = 40 , borderwidth= 3, relief = SOLID , command = send)
Button2['font'] = myFont
Button2.place(x = 400, y= 575)

#Button3
Button3 = Button(root, text = "DELETE", bg = "#356696", pady = 16 , padx = 40 , borderwidth= 3, relief = SOLID , command = del_text)
Button3['font'] = myFont
Button3.place(x = 225, y= 575)

text_to_speech.text_to_speech("Welcome to the world of AI Assistant")
print("Welcome to the world of AI Assistant")

root.mainloop()
