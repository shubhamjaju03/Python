import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

tkinter.Label(text="Miles", font=("Arial", 12)).grid(column=2, row=0)
tkinter.Label(text="is equal to", font=("Arial", 12)).grid(column=0, row=1)
result_label = tkinter.Label(text="0", font=("Arial", 12))
result_label.grid(column=1, row=1)
tkinter.Label(text="Km", font=("Arial", 12)).grid(column=2, row=1)

def calculate_km():
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 2)
    result_label.config(text=str(km))
    miles_input.delete(0, tkinter.END)

tkinter.Button(text="Calculate", command=calculate_km).grid(column=1, row=2)

window.mainloop()
