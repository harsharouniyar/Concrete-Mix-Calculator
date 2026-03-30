import tkinter as tk
from calculator import concrete_mix_calculator

def calculate():
    volume = float(entry_volume.get())

    cement, sand, agg, water, strength = concrete_mix_calculator(volume,1,2,3,0.5)

    result_label.config(text=f"""
Cement: {round(cement,2)} bags
Sand: {round(sand,2)} m3
Aggregate: {round(agg,2)} m3
Water: {round(water,2)} L
Strength: {round(strength,2)} MPa
""")

root = tk.Tk()
root.title("Concrete Mix Calculator")

tk.Label(root,text="Volume (m3)").grid(row=0)
entry_volume = tk.Entry(root)
entry_volume.grid(row=0,column=1)

tk.Button(root,text="Calculate",command=calculate).grid(row=1,column=1)

result_label = tk.Label(root,text="")
result_label.grid(row=2,column=1)

root.mainloop()