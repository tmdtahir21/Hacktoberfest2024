import tkinter as tk

def add_numbers():
    result = int(entry1.get()) + int(entry2.get())
    result_label.config(text=f"Result: {result}")

app = tk.Tk()
app.title("Simple Calculator")

# Create two input fields
entry1 = tk.Entry(app)
entry1.pack()

entry2 = tk.Entry(app)
entry2.pack()

# Create a button to add the numbers
add_button = tk.Button(app, text="Add", command=add_numbers)
add_button.pack()

# Label to display the result
result_label = tk.Label(app, text="Result: ")
result_label.pack()

app.mainloop()
