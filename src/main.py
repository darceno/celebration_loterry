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

root.mainloop()