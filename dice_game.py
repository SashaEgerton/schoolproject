from tkinter import *
from random import randint

root = Tk()

app_window = Frame(root, width=400, height=400, padx=25, pady=25)
app_window.grid(row=0, column=0, columnspan=2)

# dice frame
dice_frame = Frame(root, highlightbackground='black', highlightthickness=1, width=300, height=300)
dice_frame.place(x=200, y=200, anchor='center')

# dice cells
dice_cell1 = Frame(dice_frame, width=100, height=100)
dice_cell2 = Frame(dice_frame, width=100, height=100)
dice_cell3 = Frame(dice_frame, width=100, height=100)
dice_cell4 = Frame(dice_frame, width=100, height=100)
dice_cell5 = Frame(dice_frame, width=100, height=100)
dice_cell6 = Frame(dice_frame, width=100, height=100)
dice_cell7 = Frame(dice_frame, width=100, height=100)

# place dice cells
dice_cell1.grid(row=0, column=0, sticky='NW')
dice_cell2.grid(row=1, column=0, sticky='NW')
dice_cell3.grid(row=2, column=0, sticky='NW')
dice_cell4.grid(row=0, column=2, sticky='NW')
dice_cell5.grid(row=1, column=2, sticky='NW')
dice_cell6.grid(row=2, column=2, sticky='NW')
dice_cell7.grid(row=1, column=1, sticky='NW')

# cell labels
label1 = None
label2 = None
label3 = None
label4 = None
label5 = None
label6 = None
label7 = None


def show_label1(active):
    global label1
    if label1 is not None:
        label1.destroy()
    if active:
        label1 = Label(dice_cell1, font=('Default', 40), text='●')
        label1.place(x=50, y=50, anchor='center')


def show_label2(active):
    global label2
    if label2 is not None:
        label2.destroy()
    if active:
        label2 = Label(dice_cell2, font=('Default', 40), text='●')
        label2.place(x=50, y=50, anchor='center')


def show_label3(active):
    global label3
    if label3 is not None:
        label3.destroy()
    if active:
        label3 = Label(dice_cell3, font=('Default', 40), text='●')
        label3.place(x=50, y=50, anchor='center')


def show_label4(active):
    global label4
    if label4 is not None:
        label4.destroy()
    if active:
        label4 = Label(dice_cell4, font=('Default', 40), text='●')
        label4.place(x=50, y=50, anchor='center')


def show_label5(active):
    global label5
    if label5 is not None:
        label5.destroy()
    if active:
        label5 = Label(dice_cell5, font=('Default', 40), text='●')
        label5.place(x=50, y=50, anchor='center')


def show_label6(active):
    global label6
    if label6 is not None:
        label6.destroy()
    if active:
        label6 = Label(dice_cell6, font=('Default', 40), text='●')
        label6.place(x=50, y=50, anchor='center')


def show_label7(active):
    global label7
    if label7 is not None:
        label7.destroy()
    if active:
        label7 = Label(dice_cell7, font=('Default', 40), text='●')
        label7.place(x=50, y=50, anchor='center')


def clear_dice():
    show_label1(False)
    show_label2(False)
    show_label3(False)
    show_label4(False)
    show_label5(False)
    show_label6(False)
    show_label7(False)


def throw_dice():
    clear_dice()

    value = randint(1, 6)
    if value == 1:
        show_label7(True)
    elif value == 2:
        show_label1(True)
        show_label6(True)
    elif value == 3:
        show_label1(True)
        show_label6(True)
        show_label7(True)
    elif value == 4:
        show_label1(True)
        show_label3(True)
        show_label4(True)
        show_label6(True)
    elif value == 5:
        show_label1(True)
        show_label3(True)
        show_label4(True)
        show_label6(True)
        show_label7(True)
    elif value == 6:
        show_label1(True)
        show_label2(True)
        show_label3(True)
        show_label4(True)
        show_label5(True)
        show_label6(True)


# window buttons
throw_button = Button(root, text='Throw Dice', command=throw_dice)
throw_button.grid(row=1, column=0)

quit_button = Button(root, text='QUIT', command=root.quit)
quit_button.grid(row=1, column=1)

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

throw_dice()

root.mainloop()
