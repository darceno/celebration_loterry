import tkinter as tk

root = tk.Tk()
root.title("Celebration Lottery")

# basics attributes of the window
window_width = 600
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# frame for the main page
main_page = tk.Frame(root)
main_page.pack(side="left", fill="both", expand=True)

# frame for the lottery page
second_page = tk.Frame(root)
second_page.pack(side="left", fill="both", expand=True)
second_page.pack_forget()

# frame for the result page
third_page = tk.Frame(root)
third_page.pack(side="left", fill="both", expand=True)
third_page.pack_forget()

# functions to change pages
def go_second_page():
    main_page.pack_forget()
    second_page.pack(side="left", fill="both", expand=True)

def go_back():
    main_page.pack(side="left", fill="both", expand=True)
    second_page.pack_forget(), third_page.pack_forget()

# elements in the main page
welcome = tk.Label(main_page, text="Welcome to the Celebration Lottery!", font="Arial 18 bold")
welcome.place(relx=0.5, rely=0.1, anchor="n")

question = tk.Label(main_page, text="Have you accomplished something you're proud of? \n Use your ticket for a chance to celebrate", font="Arial 16 italic")
question.place(relx=0.5, rely=0.22, anchor="n")


go_lottery_button = tk.Button(main_page, text="Use ticket", font="Arial 18 bold", height=2, width=15, command=go_second_page)
go_lottery_button.place(relx=0.5, rely=0.5, anchor="n")

# elements in the second page (lottery page)
number_selection = tk.Frame(second_page, pady=130)
number_selection.place(relx=0.5, rely=0.5, anchor="center")

instruction_2 = tk.Label(second_page, text="Try to guess the secret number! \n You can only celebrate if you get it right", font="Arial 14 bold")
instruction_2.place(relx=0.5, rely=0.1, anchor="n")

instruction_3 = tk.Label(number_selection, text="Choose your number", font="Arial 12")
button1 = tk.Button(number_selection, text="1", font="Arial 16", height=1, width=2)
button2 = tk.Button(number_selection, text="2", font="Arial 16", height=1, width=2)
button3 = tk.Button(number_selection, text="3", font="Arial 16", height=1, width=2)
instruction_3.grid(row=0, columnspan=5, pady=5)
button1.grid(row=1, column=0, padx=1)
button2.grid(row=1, column=1, padx=1)
button3.grid(row=1, column=2, padx=1)

go_back_button = tk.Button(second_page, text="Back", font="Arial 12", command=go_back)
go_back_button.place(relx=0.5, rely=0.95, anchor="s")

# elements in the third page (result page):
result_title = tk.Label(third_page, text="The secret number is...", font="Arial 18 bold")
result_title.place(relx=0.5, rely=0.1, anchor="n")
result_frame = tk.LabelFrame(third_page, background="white", border=0)
result_frame.place(relx=0.5, rely=0.4, anchor="center")
result_screen = tk.Label(result_frame, text="42", height=3, width=10, font= "Arial 24 bold", background="white")
result_screen.pack(anchor="center")
result_reveal = tk.Label(third_page, text="Congratulations, you got it! \n Celebrate your accomplishment!", font="Arial 24 bold")
result_reveal.place(relx=0.5, rely=0.8, anchor="s")


root.mainloop()