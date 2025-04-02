from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()
    # print(email,password)
    if email == 'sanjay@gmail.com' and password == 'sanjay123':
        messagebox.showinfo('Yeah','Login Successful')
    else:
        messagebox.showerror('Error','Login Failed')


root = Tk()
root.title('Login Form')
root.iconbitmap('logos.jpg')
# root.minsize(400,400)
root.geometry('300x500')
root.configure(background='#0096DC')
img = Image.open('flipkart_logo.png')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

text_label = Label(root,text='Flipkart',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

email_label = Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root,width=40)
email_input.pack(ipady=5,pady=(1,15))

password_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input = Entry(root,width=40)
password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root,text='Longin Here',bg='white',fg='black',width=12,height=2,command=handle_login)
login_btn.pack(pady=(10,10))
login_btn.config(font=('verdana',10))



root.mainloop()


# from tkinter import *
# from PIL import ImageTk, Image

# root = Tk()
# root.title('Login Form')
# root.iconbitmap('logos.jpg')
# # root.minsize(400,400)

# root.geometry('300x500')
# root.configure(background='#0096DC')

# # Open and resize the image
# original_img = Image.open('flipkart_logo.png')
# resized_img = original_img.resize((100, 100))  # Resize using PIL Image
# img = ImageTk.PhotoImage(resized_img)

# # Add the image to a Label
# img_label = Label(root, image=img)
# img_label.pack()

# root.mainloop()
