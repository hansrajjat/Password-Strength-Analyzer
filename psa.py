import re
import hashlib
import random
import string
from tkinter import *

def generate_password():
    characters = (
        string.ascii_letters +
        string.digits +
        "@#$%^&*!"
    )
    strong_password = "".join(
        random.choice(characters)
        for i in range(12)
    )
    return strong_password

def analyze_password():
    password = password_entry.get()
    score = 0
    result_text.delete(1.0, END)
    result_text.insert(END, "----- PASSWORD ANALYSIS -----\n\n")

    if len(password) >= 8:
        score += 1
        result_text.insert(END, "✔ Good Password Length\n")
    else:
        result_text.insert(END, "✘ Password Too Short\n")

    if re.search(r"[A-Z]", password):
        score += 1
        result_text.insert(END, "✔ Uppercase Letter Found\n")
    else:
        result_text.insert(END, "✘ No Uppercase Letter\n")

    if re.search(r"[a-z]", password):
        score += 1
        result_text.insert(END, "✔ Lowercase Letter Found\n")
    else:
        result_text.insert(END, "✘ No Lowercase Letter\n")

    if re.search(r"[0-9]", password):
        score += 1
        result_text.insert(END, "✔ Number Found\n")
    else:
        result_text.insert(END, "✘ No Number\n")

    if re.search(r"[@#$%^&*!]", password):
        score += 1
        result_text.insert(END, "✔ Special Character Found\n")
    else:
        result_text.insert(END, "✘ No Special Character\n")

    try:

        with open("common_passwords.txt", "r", encoding="utf-8") as file:
            common_passwords = file.read().splitlines()

        if password.lower() in common_passwords:
            result_text.insert(
                END,
                "⚠ WARNING: Common Password Detected\n"
            )
            score -= 1

    except FileNotFoundError:

        result_text.insert(
            END,
            "common_passwords.txt file not found\n"
        )

    result_text.insert(END, "\n----- RESULT -----\n\n")
    result_text.insert(
        END,
        f"Password Score: {score} / 5\n"
    )

    if score <= 2:
        result_text.insert(END, "WEAK PASSWORD\n")
        crack_time = "Few Seconds"

    elif score <= 4:
        result_text.insert(END, "MEDIUM PASSWORD\n")
        crack_time = "Few Days"

    else:
        result_text.insert(END, "STRONG PASSWORD\n")
        crack_time = "Hundreds of Years"

    result_text.insert(
        END,
        f"Estimated Crack Time: {crack_time}\n"
    )

    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()

    result_text.insert(
        END,
        f"\nSHA-256 HASH:\n{hashed_password}\n"
    )

    try:
        with open(
            "password_hashes.txt",
            "r",
            encoding="utf-8"
        ) as file:
            saved_hashes = file.read().splitlines()

    except FileNotFoundError:

        saved_hashes = []

    last_5_passwords = saved_hashes[-5:]
    if hashed_password in last_5_passwords:
        result_text.insert(
            END,
            "\n⚠ Cannot Use Last 5 Passwords Again\n"
        )

    else:
        with open(
            "password_hashes.txt",
            "a",
            encoding="utf-8"
        ) as file:
            file.write(hashed_password + "\n")

        result_text.insert(
            END,
            "\n✔ Password Hash Saved Successfully\n"
        )

    if score == 5:
        result_text.insert(
            END,
            "\n✔ Your Password is Already Strong\n"
        )

        result_text.insert(
            END,
            "No Suggestion Needed\n"
        )

    else:
        result_text.insert(
            END,
            f"\nSuggested Strong Password:\n{generate_password()}\n"
        )

def enter_key(event):
    analyze_password()
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide Password")

    else:
        password_entry.config(show="*")
        show_button.config(text="Show Password")

window = Tk()
window.title("Password Strength Analyzer")
window.geometry("650x650")
window.config(bg="#1e1e1e")

title_label = Label(
    window,
    text="Password Strength Analyzer",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title_label.pack(pady=20)
password_label = Label(
    window,
    text="Enter Password",
    font=("Arial", 12),
    bg="#1e1e1e",
    fg="white"
)

password_label.pack()
password_entry = Entry(
    window,
    width=35,
    font=("Arial", 14),
    show="*"
)

password_entry.pack(pady=10)
password_entry.bind("<Return>", enter_key)

show_button = Button(
    window,
    text="Show Password",
    command=toggle_password,
    bg="#2196F3",
    fg="white",
    font=("Arial", 10, "bold")
)

show_button.pack(pady=5)
analyze_button = Button(
    window,
    text="Analyze Password",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=analyze_password
)

analyze_button.pack(pady=15)

result_text = Text(
    window,
    width=75,
    height=22,
    font=("Arial", 10)
)

result_text.pack(pady=10)

window.mainloop()