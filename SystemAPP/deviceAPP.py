import requests
from tkinter import *

app = Tk()
response = requests.get('http://127.0.0.1:8000/get-order-data/')

def change_text():
    response = requests.get('http://127.0.0.1:8000/get-order-data/')
    text.config(text=response.json())
    app.after(1000, change_text)

text = Label(app, text=response.json())
text.pack()

change_text()
app.mainloop()