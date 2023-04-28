from tkinter import *


def convert_miles_to_km(miles):
    km = miles * 1.60934
    return km


def on_button_press():
    miles = float(entry.get())
    km = convert_miles_to_km(miles)
    result.config(text=f"{round(km,1)}")


if __name__ == "__main__":
    # Define the application area
    window = Tk()
    window.title("Mile to Km Converter")
    window.minsize(width=300, height=100)
    window.config(padx=10, pady=10)

    # Label
    equal_to = Label(text="Is equal to", font=("Arial", 12, "bold"))
    equal_to.grid(column=1, row=1)
    equal_to.config(padx=10, pady=10)

    # Label
    result = Label(text="0", font=("Arial", 12, "bold"))
    result.grid(column=3, row=1)
    result.config(padx=10, pady=10)

    # Label
    u_miles = Label(text="Miles", font=("Arial", 12, "bold"))
    u_miles.grid(column=4, row=0)
    u_miles.config(padx=10, pady=10)

    # Label
    u_km = Label(text="Km", font=("Arial", 12, "bold"))
    u_km.grid(column=4, row=1)
    u_km.config(padx=10, pady=10)

    # Entry
    entry = Entry(width=10)
    entry.grid(column=3, row=0)

    # Button
    button = Button(text="Calculate", command=on_button_press)
    button.grid(column=3, row=2)

    window.mainloop()
