import tkinter as tk
from tkinter import messagebox
import re

# =========================
# COLORS
# =========================
BG = "#1e1f26"
CARD = "#2b2d3a"
ENTRY_BG = "#f4f4f4"

PRIMARY = "#7c5cff"
PRIMARY_HOVER = "#9277ff"

TEXT = "#ffffff"
PLACE = "#777777"

# =========================
# ROOT
# =========================
root = tk.Tk()
root.title("Registration Form")
root.geometry("420x520")
root.resizable(False, False)
root.configure(bg=BG)

# Center Screen
x = (root.winfo_screenwidth() // 2) - (420 // 2)
y = (root.winfo_screenheight() // 2) - (520 // 2)
root.geometry(f"420x520+{x}+{y}")

# =========================
# MAIN CARD
# =========================
main = tk.Frame(root, bg=CARD)
main.place(relx=0.5, rely=0.5, anchor="center",
           width=320, height=400)

# =========================
# TITLE
# =========================
title = tk.Label(
    main,
    text="REGISTER",
    font=("Arial", 22, "bold"),
    bg=CARD,
    fg=TEXT
)
title.pack(pady=(25, 20))

# =========================
# FIELD CREATOR
# =========================
entries = {}

def create_field(icon, placeholder, is_password=False):

    container = tk.Frame(main, bg=CARD)
    container.pack(pady=10)

    field = tk.Frame(
        container,
        bg=ENTRY_BG,
        width=250,
        height=42
    )
    field.pack()

    field.pack_propagate(False)

    icon_label = tk.Label(
        field,
        text=icon,
        font=("Arial", 13),
        bg=ENTRY_BG,
        fg=PRIMARY
    )
    icon_label.pack(side="left", padx=10)

    entry = tk.Entry(
        field,
        bd=0,
        font=("Arial", 11),
        fg=PLACE,
        bg=ENTRY_BG,
        insertbackground="#000000"
    )

    entry.insert(0, placeholder)
    entry.pack(side="left", fill="both", expand=True)

    # ---------------------
    # Placeholder Logic
    # ---------------------
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="#000000")

            if is_password:
                entry.config(show="*")

        field.config(bg="#ffffff")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg=PLACE)

            if is_password:
                entry.config(show="")

        field.config(bg=ENTRY_BG)

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

    # ---------------------
    # Password Toggle
    # ---------------------
    if is_password:

        def toggle():
            if entry.get() == placeholder:
                return

            if entry.cget("show") == "":
                entry.config(show="*")
                eye_btn.config(text="👁")
            else:
                entry.config(show="")
                eye_btn.config(text="🙈")

        eye_btn = tk.Button(
            field,
            text="👁",
            bd=0,
            bg=ENTRY_BG,
            activebackground=ENTRY_BG,
            cursor="hand2",
            command=toggle
        )
        eye_btn.pack(side="right", padx=10)

    entries[placeholder] = entry

# =========================
# INPUTS
# =========================
create_field("👤", "Name")
create_field("✉", "Email")
create_field("📞", "Phone")
create_field("🔒", "Password", True)

# =========================
# EMAIL CHECK
# =========================
def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# =========================
# REGISTER
# =========================
def register():

    name = entries["Name"].get()
    email = entries["Email"].get()
    phone = entries["Phone"].get()
    password = entries["Password"].get()

    # Validation
    if name == "Name":
        messagebox.showerror("Error", "Enter your name")
        return

    if not valid_email(email):
        messagebox.showerror("Error", "Invalid email")
        return

    if not phone.isdigit():
        messagebox.showerror("Error", "Phone must be numeric")
        return

    if len(password) < 8 or password == "Password":
        messagebox.showerror(
            "Error",
            "Password must be at least 8 characters"
        )
        return

    messagebox.showinfo(
        "Success",
        "Registration Completed Successfully!"
    )

# =========================
# BUTTON
# =========================
register_btn = tk.Button(
    main,
    text="REGISTER",
    font=("Arial", 14, "bold"),
    bg=PRIMARY,
    fg="white",
    activebackground=PRIMARY_HOVER,
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    command=register,
    height=2 
)

register_btn.pack(
    pady=15,
    ipadx=70
)

# Hover Effect
def on_enter(e):
    register_btn.config(bg=PRIMARY_HOVER)

def on_leave(e):
    register_btn.config(bg=PRIMARY)

register_btn.bind("<Enter>", on_enter)
register_btn.bind("<Leave>", on_leave)

# =========================
# START
# =========================
root.mainloop()