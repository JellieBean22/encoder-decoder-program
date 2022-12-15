#COMPLETE!!
from tkinter import Tk, Label, StringVar, Entry, Button #or *
import base64
import pyperclip as pc #clipboard wasn't working

#create a window
root = Tk()
#set window width and height
root.geometry('500x400')
#set fixed size of the window
root.resizable(0,0)
#set the title
root.title('Jay\'s Projects')
root.config(background = 'light blue')

#Display text users can't modify
Label(root, text = 'Message Encoder / Decoder', font = 'arial 16 bold', bg = 'light blue').place(x = 100, y = 20)
#Label(root, text = 'Encode / Decode', font = 'arial 20 bold', bg = 'light blue').place(x = 150, y = 10)
#Label(root, text = 'Jay', font = 'arial 16').pack(side = BOTTOM)

#this variable stores the message 
Text = StringVar() #msg
#stores the private key
private_key = StringVar() #key
#used to select whether to code or decode
mode = StringVar()
#stores the result
Result = StringVar()



def Encode(key, root):
    enc = []
    #the loop runs for the length of the message
    for i in range(len(root)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(root[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode(''.join(enc).encode()).decode()


def Decode(key, root):
    deco = []
    root = base64.urlsafe_b64decode(root).decode()
    
    for i in range(len(root)):
        key_c = key[i % len(key)]
        deco.append(chr((256 + ord(root[i]) - ord(key_c)) % 256))
    return ''.join(deco)


def Enc():
    str(Result.set(Encode(private_key.get(), Text.get())))
    Entry(root, font = 'calibri 12', textvariable = Result, fg = 'black', bg = 'white', width = 20, bd = 2, relief = 'sunken').place(x = 300, y = 180)

def Dec():
    Result.set(Decode(private_key.get(), Text.get()))
    Entry(root, font = 'calibri 12', textvariable = Result, fg = 'black', bg = 'white', width = 20, bd = 2, relief = 'sunken').place(x = 300, y = 180)
    

def Copy():
    pc.copy(str(Result.get()))
    Entry(root, font = 'calibri 12', textvariable = Result, fg = 'gray', bg = 'white', width = 20, bd = 2, relief = 'sunken').place(x = 300, y = 180)
    Result.set('copied!')
    

#stops the mainloop to quit the program
def Exit():
    root.destroy()

#set all variables to empty strings
def Reset():
    Text.set('')
    private_key.set('')
    mode.set('')
    result_ent = Entry(root, font = 'calibri 12', textvariable = Result, fg = 'gray', bg = 'white', width = 20, bd = 2, relief = 'sunken').place(x = 300, y = 180)
    Result.set('Encrypted Message')


msg_lbl = Label(root, font = 'arial 14 bold', text = 'Message', bg = 'light blue').place(x = 20, y = 100)
msg_ent = Entry(root, font = 'calibri 12', textvariable = Text, bg = 'white', bd = 2, relief = 'sunken').place(x = 300, y = 100)

key_lbl = Label(root, font = 'arial 14 bold', text = 'Pre-Shared Key', bg = 'light blue').place(x = 20, y = 140)
key_ent = Entry(root, font = 'calibri 12', textvariable = private_key, bg = 'white', bd = 2, relief = 'sunken').place(x = 300, y = 140)

#mode_lbl = Label(root, font = 'arial 14 bold', text = '(e)ncode | (d)ecode', bg = 'light blue').place(x = 20, y = 180)
#mode_ent = Entry(root, font = 'calibri 12', textvariable = mode, bg = 'white').place(x = 300, y = 180)

result_ent = Entry(root, font = 'calibri 12', textvariable = Result, fg = 'gray', bg = 'white', width = 20, bd = 2, relief = 'sunken').place(x = 300, y = 180)
#result_btn = Button(root, font = 'calibri 14 bold', text = 'Result', bg = 'dark blue', fg = 'white', command = Answer).place(x = 20, y = 220)
Result.set('Encrypted Message')

reset_btn = Button(root, font = 'arial 12', text = 'Reset', padx = 2, width = 6, pady = 2, cursor = 'hand1' , fg = 'white', bg = 'LimeGreen', command = Reset).place(x = 300, y = 260)

ex_btn = Button(root, font = 'arial 12 bold', text = 'Exit', padx = 2, width = 6, pady = 2, cursor = 'hand1', fg = 'white', bg = 'OrangeRed', command = Exit).place(x = 400, y = 260)

enc_btn = Button(root, font = 'arial 12', text = 'Encode', bg = 'blue', fg = 'white', cursor = 'hand2', command = Enc).place(x = 20, y = 180)
dec_btn = Button(root, font = 'arial 12', text = 'Decode', bg = 'alice blue', cursor = 'hand2', command = Dec).place(x = 100, y = 180)

copy_btn= Button(root, font = 'arial 12', text = 'copy', bg = 'magenta', fg = 'white', command = Copy).place(x = 420, y = 205)

root.mainloop()
