import tkinter as tk

# create window
root = tk.Tk()

# creates a frame within our window
top_frame = tk.Frame(root)
top_frame.pack()

bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM)

first_buttom = tk.Button(top_frame, text='Login', fg='red')
second_buttom = tk.Button(top_frame, text='Forgot Username', fg='orange')

third_buttom = tk.Button(bottom_frame, text='Register', fg='blue')
fourth_buttom = tk.Button(bottom_frame, text='Forgot Password', fg='green')

first_buttom.pack(side=tk.LEFT)
second_buttom.pack(side=tk.RIGHT)
third_buttom.pack(side=tk.LEFT)
fourth_buttom.pack(side=tk.RIGHT)

# create some sample text to put on window
# sample_text = tk.Label(root, text='Sample Text')

# essentially runs a while loop so the program stays open forever
root.mainloop()
