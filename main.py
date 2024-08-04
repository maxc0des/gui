from customtkinter import *
import random

app = CTk()
app.geometry("500x400")

# Initialize end and number
end = 100
number = "unknown"

def get_number():
    global number
    number = random.randint(0, end)
    output.configure(text=f"Your number is {number}")

def update_slider(value):
    global end
    end = int(float(value))  # Convert the value to an integer
    btn.configure(text=f"Get a random number between 0 and {end}")

# Create the button
btn = CTkButton(master=app, text=f"Get a random number between 0 and {end}", command=get_number)
btn.pack(pady=20)

# Create the slider
slider = CTkSlider(master=app, from_=0, to=100, number_of_steps=100, command=update_slider)
slider.set(end)  # Initialize slider to match the end value
slider.pack(pady=20)

# Create the output label
output = CTkLabel(master=app, text=f"Your number is {number}")
output.pack(pady=20)

app.mainloop()