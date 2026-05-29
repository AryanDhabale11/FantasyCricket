from tkinter import *

# ================= MAIN WINDOW =================

root = Tk()

root.title("Fantasy Cricket League")
root.geometry("1150x650")
root.configure(bg="#0f172a")
root.resizable(False, False)

# ================= CARD FUNCTION =================

def create_card(parent, width, height, color):

    canvas = Canvas(
        parent,
        width=width,
        height=height,
        bg="#0f172a",
        highlightthickness=0
    )

    # Rounded effect
    canvas.create_rectangle(
        15,
        15,
        width-15,
        height-15,
        fill=color,
        outline=color
    )

    return canvas

# ================= TITLE =================

title = Label(
    root,
    text="🏏 Fantasy Cricket League",
    font=("Segoe UI", 28, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

title.pack(pady=20)

# ================= TEAM FRAME =================

team_frame = Frame(root, bg="#0f172a")
team_frame.pack()

team_label = Label(
    team_frame,
    text="Team Name:",
    font=("Segoe UI", 14, "bold"),
    bg="#0f172a",
    fg="white"
)

team_label.grid(row=0, column=0, padx=10)

team_entry = Entry(
    team_frame,
    width=25,
    font=("Segoe UI", 14),
    bg="#334155",
    fg="white",
    insertbackground="white",
    bd=0
)

team_entry.grid(row=0, column=1, padx=10)

# ================= MAIN CONTENT =================

main_frame = Frame(root, bg="#0f172a")
main_frame.pack(pady=25)

# ================= CATEGORY CARD =================

category_card = create_card(main_frame, 220, 430, "#1e293b")
category_card.grid(row=0, column=0, padx=20)

category_title = Label(
    category_card,
    text="Categories",
    font=("Segoe UI", 16, "bold"),
    bg="#1e293b",
    fg="#38bdf8"
)

category_card.create_window(110, 40, window=category_title)

categories = ["BAT", "BOW", "AR", "WK"]

y_position = 110

for category in categories:

    btn = Button(
        category_card,
        text=category,
        width=12,
        height=2,
        font=("Segoe UI", 11, "bold"),
        bg="#38bdf8",
        fg="black",
        activebackground="#0ea5e9",
        bd=0,
        cursor="hand2"
    )

    category_card.create_window(110, y_position, window=btn)

    y_position += 70

# ================= AVAILABLE PLAYERS CARD =================

available_card = create_card(main_frame, 340, 430, "#1e293b")
available_card.grid(row=0, column=1, padx=20)

available_title = Label(
    available_card,
    text="Available Players",
    font=("Segoe UI", 16, "bold"),
    bg="#1e293b",
    fg="#38bdf8"
)

available_card.create_window(170, 40, window=available_title)

available_list = Listbox(
    available_card,
    width=28,
    height=16,
    font=("Consolas", 12),
    bg="#334155",
    fg="white",
    bd=0,
    highlightthickness=0,
    selectbackground="#38bdf8"
)

available_card.create_window(170, 230, window=available_list)

# Demo Players
players = [
    "Virat Kohli",
    "Rohit Sharma",
    "Shubman Gill",
    "KL Rahul",
    "Suryakumar Yadav",
    "Hardik Pandya",
    "Ravindra Jadeja",
    "Axar Patel",
    "Rishabh Pant",
    "MS Dhoni",
    "Ishan Kishan",
    "Jasprit Bumrah",
    "Mohammed Shami",
    "Mohammed Siraj",
    "Bhuvneshwar Kumar",
    "Yuzvendra Chahal",
    "Kuldeep Yadav",
    "Ruturaj Gaikwad",
    "Sanju Samson",
    "Arshdeep Singh"
]

for player in players:
    available_list.insert(END, player)

# ================= SELECTED PLAYERS CARD =================

selected_card = create_card(main_frame, 340, 430, "#1e293b")
selected_card.grid(row=0, column=2, padx=20)

selected_title = Label(
    selected_card,
    text="Selected Players",
    font=("Segoe UI", 16, "bold"),
    bg="#1e293b",
    fg="#38bdf8"
)

selected_card.create_window(170, 40, window=selected_title)

selected_list = Listbox(
    selected_card,
    width=28,
    height=16,
    font=("Consolas", 12),
    bg="#334155",
    fg="white",
    bd=0,
    highlightthickness=0,
    selectbackground="#22c55e"
)

selected_card.create_window(170, 230, window=selected_list)

# ================= BOTTOM INFO =================

bottom_frame = Frame(root, bg="#0f172a")
bottom_frame.pack(pady=20)

points_label = Label(
    bottom_frame,
    text="💰 Points Available : 100",
    font=("Segoe UI", 13, "bold"),
    bg="#0f172a",
    fg="#22c55e"
)

points_label.grid(row=0, column=0, padx=25)

used_label = Label(
    bottom_frame,
    text="📊 Points Used : 0",
    font=("Segoe UI", 13, "bold"),
    bg="#0f172a",
    fg="#facc15"
)

used_label.grid(row=0, column=1, padx=25)

players_label = Label(
    bottom_frame,
    text="👥 Players Selected : 0",
    font=("Segoe UI", 13, "bold"),
    bg="#0f172a",
    fg="#f87171"
)

players_label.grid(row=0, column=2, padx=25)

# ================= RUN APP =================

root.mainloop()