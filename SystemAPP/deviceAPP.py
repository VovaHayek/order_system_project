import requests
from tkinter import *

app = Tk()
rest_name = 'mcdonalds'
response = requests.get(f'http://127.0.0.1:8000/get-order-data?restaurant={rest_name}')

def change_text():
    response = requests.get(f'http://127.0.0.1:8000/get-order-data?restaurant={rest_name}')
    text.config(text=response.json())
    app.after(1000, change_text)

text = Label(app, text=response.json())
text.pack()

change_text()
app.mainloop()