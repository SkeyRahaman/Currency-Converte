# Import Module
from tkinter import *
from tkinter import ttk
import requests
import configuration as cn


# function to get all the country names for convertion with the help of api from "fixer.io"
def get_options():
    response = requests.get("http://data.fixer.io/api/symbols?access_key={}".format(cn.access_key))
    options = []
    loop = response.json()['symbols']
    for a in loop:
        options.append(loop[a] + "(" + a + ")")
    return tuple(sorted(options))


# function to get the current exchange rate with the help of api from "fixer.io"
def get_rate(from_="USD", to_="INR"):
    response = requests.get("http://data.fixer.io/api/latest?access_key={}&symbols=".format(cn.access_key) + \
                            from_ + "," + to_ + "&format=1")

    return response.json()['rates'][from_], response.json()['rates'][to_]


# function to update the result feild
def hi(update_point, from_="Indian Rupee(INR)", to_="United States Dollar(USD)", converting_amount=00):
    if not converting_amount:
        converting_amount = 1
    from_rate, to_rate = get_rate(from_, to_)
    update_point.configure(text=round((float(converting_amount) / from_rate * to_rate), 10))


# create root window
root = Tk()

# root window title and dimension
root.title("Currency Conveter")

# adding a label to the root window
#heading
Label(root, text='Currency Conveter', bg='red', width=15, height=0,
      font=("Times", 50, "bold")).grid(row=0, column=1, columnspan=3)
#spaces beside heading and below heading
Label(root, text='', bg='pink', width=10, height=5).grid(row=0, column=0)
Label(root, text='', bg='pink', width=10, height=5).grid(row=0, column=4)
Label(root, text='', width=10, height=2).grid(row=1, column=4)

# Dropdown menu options
options = get_options()

# datatype of menu text
clicked_from = StringVar()
clicked_to = StringVar()

# Create Dropdown menu

from_currency = ttk.Combobox(root, width=27, textvariable=clicked_from, style='Custom.TMenubutton',
                             values=tuple(options))
from_currency.current(68)
from_currency.grid(row=2, column=1)

to_currency = ttk.Combobox(root, width=27, textvariable=clicked_to, style='Custom.TMenubutton',
                           values=tuple(options))
to_currency.current(158)
to_currency.grid(row=2, column=3)

from_amount = Entry()
from_amount.insert(0, 1)
from_amount.grid(row=3, column=1)

Label(root, text='To', width=5, font=("Times", 20, "bold")).grid(row=3, column=2)

ans = Label(root, text='00', width=30)
ans.grid(row=3, column=3)

Label(root, text='', height=5).grid(row=4, column=2)

convert_btn = Button(root, text="Convert", font=('', 13), width=25, bg="pink",
                     command=lambda: hi(from_=from_currency.get()[-4:-1], converting_amount=from_amount.get(),
                                        to_=to_currency.get()[-4:-1], update_point=ans)).grid(row=7,
                                                                                              column=3)
from_currency.bind("<<ComboboxSelected>>",
                   lambda _: hi(from_=from_currency.get()[-4:-1], converting_amount=from_amount.get(),
                                to_=to_currency.get()[-4:-1], update_point=ans))
to_currency.bind("<<ComboboxSelected>>",
                 lambda _: hi(from_=from_currency.get()[-4:-1], converting_amount=from_amount.get(),
                              to_=to_currency.get()[-4:-1], update_point=ans))
Label(root, text='', width=10, height=5).grid(row=8, column=4)
Label(root, text='Thank you for using', width=15, height=0).grid(row=9, column=1, columnspan=3)
hi(from_=from_currency.get()[-4:-1], converting_amount=from_amount.get(),
   to_=to_currency.get()[-4:-1], update_point=ans)

root.mainloop()
