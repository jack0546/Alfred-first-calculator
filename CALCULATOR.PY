import tkinter as tk
import math

root = tk.Tk()
root.title(": ALFRED SCIENTIFIC CALCULATOR:")
root.geometry("600x650")
root.configure(bg="#333")

display = tk.StringVar(value="0")
tk.Label(root, textvariable=display, bg="#111",
         fg="#0ff", font=("Arial", 20, "bold"),
         height=2).pack(fill="x", padx=10, pady=10)

def click(btn):
    current = display.get()
    if btn == "C": 
        display.set("0")
    elif btn == "del":
        display.set(current[:-1] if len(current) > 1 else "0")
    elif btn == "=":
        try: 
            display.set(str(eval(current)))
        except: 
            display.set("Error")
    elif btn == "sin":
        try:
            display.set(str(math.sin(math.radians(float(current)))))
        except:
            display.set("Error")
    elif btn == "cos":
        try:
            display.set(str(math.cos(math.radians(float(current)))))
        except:
            display.set("Error")
    else: 
        display.set(current + btn if current != "0" else btn)

buttons = [
    ["C", "sin", "cos", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    [".", "0", "del", "="]
]
        
for i, row in enumerate(buttons):
    frame = tk.Frame(root, bg="#000")
    frame.pack(fill="x", padx=10, pady=2)
    for j, btn in enumerate(row):
        color = "#050101" if btn in "+-*/=" else ("#176186" if btn == "C" else "#34495e")
        btn_widget = tk.Label(frame, text=btn, font=("Arial", 33, "bold"), bg=color, fg="white", width=5, height=2, relief="groove")
        btn_widget.bind("<Button-1>", lambda e, b=btn: click(b))
        btn_widget.pack(side="left", padx=2)

root.mainloop()
                            