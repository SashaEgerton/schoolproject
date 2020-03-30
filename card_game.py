from tkinter import *
from random import randint

root = Tk()

app_window = Frame(root, width=400, height=600, padx=25, pady=25)
app_window.grid(row=0, column=0, columnspan=2)

# card frame
card_frame = Frame(root, highlightbackground='black', highlightthickness=1, width=300, height=500)
card_frame.place(x=200, y=300, anchor='center')

# card cells
card_cell1 = Frame(card_frame, width=50, height=50)
card_cell2 = Frame(card_frame, width=200, height=400)
card_cell3 = Frame(card_frame, width=50, height=50)

# place card cells
card_cell1.grid(row=0, column=0, sticky='NW')
card_cell2.grid(row=1, column=1, sticky='NW')
card_cell3.grid(row=2, column=2, sticky='NW')

# cell labels
label1  = Label(card_cell1,  font=('Default', 40), text='')
label2  = Label(card_cell2,  font=('Default', 200), text='')
label3  = Label(card_cell3,  font=('Default', 40), text='')


def get_color(suit):
    return 'black' if suit % 2 else 'red'


def get_value(value):
    if value == 1:
        return 'A'
    elif value == 11:
        return 'J'
    if value == 12:
        return 'Q'
    if value == 13:
        return 'K'
    else:
        return f'{value}'


def get_suit(suit):
    return ['♠', '♥', '♣', '♦'][suit - 1]


def show_label1(suit, value):
    global label1
    label1['fg'] = get_color(suit)
    label1['text'] = get_value(value)
    label1.place(x=25, y=25, anchor='center')


def show_label2(suit, value):
    global label2
    label2['fg'] = get_color(suit)
    label2['text'] = get_suit(suit)
    label2.place(x=100, y=200, anchor='center')


def show_label3(suit, value):
    global label3
    label3['fg'] = get_color(suit)
    label3['text'] = get_value(value)
    label3.place(x=25, y=25, anchor='center')


def draw_card():
    suit = randint(1, 4)
    value = randint(1, 13)
    show_label1(suit, value)
    show_label2(suit, value)
    show_label3(suit, value)


# window buttons
draw_button = Button(root, text='Random Card', command=draw_card)
draw_button.grid(row=1, column=0)

quit_button = Button(root, text='QUIT', command=root.quit)
quit_button.grid(row=1, column=1)

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

draw_card()

root.mainloop()
