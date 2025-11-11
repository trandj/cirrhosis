from tkinter import *
from tkinter import filedialog

# ---------- Window Setup ----------
root = Tk()
root.title("VizLab")
root.geometry("1920x1200")
root.configure(bg="#a9c8f5")  # blue border background

# ---------- Outer Frame (Blue Border) ----------
outer_frame = Frame(root, bg="#a9c8f5", padx=40, pady=40)
outer_frame.pack(fill="both", expand=True)

# ---------- Main UI Container ----------
main_frame = Frame(outer_frame, bg="#e6e8f4")
main_frame.pack(fill="both", expand=True)

# ---------- Header Bar ----------
header = Frame(main_frame, bg="#2e2c9e", height=80)
header.pack(fill="x")

# "VizLab" as a clickable tab (Home)
home_btn = Button(
    header,
    text="VizLab",
    fg="white",
    bg="#2e2c9e",
    font=("Helvetica", 45, "bold"),
    bd=0,
    relief="flat",
    activebackground="#2e2c9e",
    activeforeground="white",
    cursor="hand2",
)
home_btn.pack(side="left", padx=30, pady=10)

# ---------- Navigation Bar ----------
nav = Frame(main_frame, bg="#c8cbe3", height=60, pady=10)
nav.pack(fill="x")

def create_nav_button(parent, text, active=False):
    font_weight = "bold" if active else "normal"
    font_style = ("Helvetica", 25, font_weight, "underline")
    return Button(
        parent,
        text=text,
        relief="flat",
        bg="#c8cbe3",
        fg="black",
        font=font_style,
        padx=45,
        pady=8,
        bd=0,
        cursor="hand2",
        activebackground="#b3b3b3",
        highlightthickness=0
    )

# Tabs including the new “Records”
tabs = ["Import", "Cleaning", "Visualization", "Mining", "Records"]
for t in tabs:
    btn = create_nav_button(nav, t)
    btn.pack(side="left", padx=70, pady=5)

# ---------- Main Content Area ----------
content = Frame(main_frame, bg="#e6e8f4", padx=60, pady=60)
content.pack(fill="both", expand=True)

# ---------- Flow-Like Layout ----------
flow = Frame(content, bg="#e6e8f4")
flow.pack(fill="both", expand=True)

# Responsive columns
flow.grid_columnconfigure(0, weight=1)
flow.grid_columnconfigure(1, weight=1)

main_title = Label(
    content,
    text="Patient Records",
    font=("Helvetica", 26, "bold"),
    bg="#e6e8f4",
    fg="black",
)
main_title.pack(pady=20)



# ---------- Run App ----------
root.mainloop()