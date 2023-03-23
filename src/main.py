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

# elements in the main page:

welcome = tk.Label(main_page, text="Welcome to the Celebration Lottery!", font="Arial 18 bold")
welcome.place(relx=0.5, rely=0.1, anchor="n")

question = tk.Label(main_page, text="Have you accomplished something you're proud of? \n Use your ticket for a chance to celebrate", font="Arial 16 italic")
question.place(relx=0.5, rely=0.22, anchor="n")


go_lottery_button = tk.Button(main_page, text="Use ticket", font="Arial 18 bold", height=2, width=15, command=go_second_page)
go_lottery_button.place(relx=0.5, rely=0.5, anchor="n")


root.mainloop()