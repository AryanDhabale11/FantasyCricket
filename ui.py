from tkinter import *
from tkinter import messagebox
from database import (
    fetch_players,
    save_team,
    get_saved_teams,
    get_leaderboard,
    delete_team,
    search_team
)

from scoring import calculate_points

# ================= MAIN WINDOW =================

root = Tk()

root.title("Fantasy Cricket League")
root.geometry("1280x920")
root.configure(bg="#0f172a")
root.resizable(False, False)

# ================= VARIABLES =================

total_points = 100
used_points = 0
selected_count = 0

selected_players = []

# ================= CARD FUNCTION =================

def create_card(parent, width, height, color):

    canvas = Canvas(
        parent,
        width=width,
        height=height,
        bg="#0f172a",
        highlightthickness=0
    )

    canvas.create_rectangle(
        15,
        15,
        width - 15,
        height - 15,
        fill=color,
        outline=color
    )

    return canvas

# ================= UPDATE LABELS =================

def update_labels():

    points_label.config(
        text=f"💰 Points Available : {total_points - used_points}"
    )

    used_label.config(
        text=f"📊 Points Used : {used_points}"
    )

    players_label.config(
        text=f"👥 Players Selected : {selected_count}"
    )

# ================= SHOW PLAYERS =================

def show_players(category):

    available_list.delete(0, END)

    players = fetch_players(category)

    for player in players:
        available_list.insert(END, player[0])

# ================= ADD PLAYER =================

def add_player(event):

    global used_points
    global selected_count

    selected = available_list.curselection()

    if not selected:
        return

    player = available_list.get(selected)

    if player in selected_players:
        messagebox.showwarning(
            "Duplicate Player",
            "Player already selected!"
        )
        return

    if selected_count >= 11:
        messagebox.showwarning(
            "Team Full",
            "You can select only 11 players!"
        )
        return

    selected_players.append(player)

    selected_list.insert(END, player)

    available_list.delete(selected)

    used_points += 10
    selected_count += 1

    update_labels()

# ================= REMOVE PLAYER =================

def remove_player(event):

    global used_points
    global selected_count

    selected = selected_list.curselection()

    if not selected:
        return

    player = selected_list.get(selected)

    selected_players.remove(player)

    selected_list.delete(selected)

    available_list.insert(END, player)

    used_points -= 10
    selected_count -= 1

    update_labels()

# ================= SAVE TEAM =================

def save_team_data():

    team_name = team_entry.get()

    if team_name == "":
        messagebox.showwarning(
            "Missing Team Name",
            "Please enter a team name!"
        )
        return

    if selected_count != 11:
        messagebox.showwarning(
            "Incomplete Team",
            "Select exactly 11 players!"
        )
        return

    save_team(
        team_name,
        selected_players,
        used_points
    )

    messagebox.showinfo(
        "Success",
        "Team saved successfully!"
    )

# ================= VIEW SAVED TEAMS =================

def view_teams():

    teams = get_saved_teams()

    team_window = Toplevel(root)

    team_window.title("Saved Teams")
    team_window.geometry("700x500")
    team_window.configure(bg="#0f172a")

    title = Label(
        team_window,
        text="📋 Saved Fantasy Teams",
        font=("Segoe UI", 22, "bold"),
        bg="#0f172a",
        fg="#38bdf8"
    )

    title.pack(pady=20)

    team_listbox = Listbox(
        team_window,
        width=80,
        height=20,
        font=("Consolas", 11),
        bg="#1e293b",
        fg="white",
        selectbackground="#38bdf8",
        bd=0
    )

    team_listbox.pack(pady=20)

    for team in teams:

        team_name = team[0]
        players = team[1]
        value = team[2]

        display_text = (
            f"Team: {team_name} | "
            f"Points Used: {value} | "
            f"Players: {players}"
        )

        team_listbox.insert(END, display_text)

# ================= SCORE CALCULATOR =================

def open_score_calculator():

    calc_window = Toplevel(root)

    calc_window.title("Fantasy Points Calculator")
    calc_window.geometry("500x600")
    calc_window.configure(bg="#0f172a")

    title = Label(
        calc_window,
        text="🏏 Fantasy Points Calculator",
        font=("Segoe UI", 20, "bold"),
        bg="#0f172a",
        fg="#38bdf8"
    )

    title.pack(pady=20)

    # Runs
    Label(
        calc_window,
        text="Runs:",
        font=("Segoe UI", 12),
        bg="#0f172a",
        fg="white"
    ).pack()

    runs_entry = Entry(calc_window, font=("Segoe UI", 12))
    runs_entry.pack(pady=5)

    # Fours
    Label(
        calc_window,
        text="Fours:",
        font=("Segoe UI", 12),
        bg="#0f172a",
        fg="white"
    ).pack()

    fours_entry = Entry(calc_window, font=("Segoe UI", 12))
    fours_entry.pack(pady=5)

    # Sixes
    Label(
        calc_window,
        text="Sixes:",
        font=("Segoe UI", 12),
        bg="#0f172a",
        fg="white"
    ).pack()

    sixes_entry = Entry(calc_window, font=("Segoe UI", 12))
    sixes_entry.pack(pady=5)

    # Wickets
    Label(
        calc_window,
        text="Wickets:",
        font=("Segoe UI", 12),
        bg="#0f172a",
        fg="white"
    ).pack()

    wickets_entry = Entry(calc_window, font=("Segoe UI", 12))
    wickets_entry.pack(pady=5)

    # Catches
    Label(
        calc_window,
        text="Catches:",
        font=("Segoe UI", 12),
        bg="#0f172a",
        fg="white"
    ).pack()

    catches_entry = Entry(calc_window, font=("Segoe UI", 12))
    catches_entry.pack(pady=5)

    result_label = Label(
        calc_window,
        text="Total Points: 0",
        font=("Segoe UI", 16, "bold"),
        bg="#0f172a",
        fg="#22c55e"
    )

    result_label.pack(pady=20)

    def calculate():

        try:

            runs = int(runs_entry.get())
            fours = int(fours_entry.get())
            sixes = int(sixes_entry.get())
            wickets = int(wickets_entry.get())
            catches = int(catches_entry.get())

            total = calculate_points(
                runs,
                fours,
                sixes,
                wickets,
                catches
            )

            result_label.config(
                text=f"Total Points: {total}"
            )

        except:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numbers!"
            )

    calculate_btn = Button(
        calc_window,
        text="Calculate Points",
        font=("Segoe UI", 12, "bold"),
        bg="#22c55e",
        fg="white",
        bd=0,
        padx=20,
        pady=10,
        cursor="hand2",
        command=calculate
    )

    calculate_btn.pack(pady=10)

# ================= LEADERBOARD WINDOW =================

def open_leaderboard():

    leaderboard_data = get_leaderboard()

    board_window = Toplevel(root)

    board_window.title("Fantasy Leaderboard")
    board_window.geometry("650x500")
    board_window.configure(bg="#0f172a")

    title = Label(
        board_window,
        text="🏆 Fantasy Leaderboard",
        font=("Segoe UI", 24, "bold"),
        bg="#0f172a",
        fg="#facc15"
    )

    title.pack(pady=20)

    leaderboard_list = Listbox(
        board_window,
        width=60,
        height=18,
        font=("Consolas", 13),
        bg="#1e293b",
        fg="white",
        selectbackground="#38bdf8",
        bd=0
    )

    leaderboard_list.pack(pady=20)

    rank = 1

    for team in leaderboard_data:

        team_name = team[0]
        score = team[1]

        line = (
            f"#{rank}   "
            f"{team_name}   "
            f"Score: {score}"
        )

        leaderboard_list.insert(END, line)

        rank += 1
# ================= TEAM MANAGER =================

def open_team_manager():

    manager = Toplevel(root)

    manager.title("Team Manager")
    manager.geometry("750x550")
    manager.configure(bg="#0f172a")

    title = Label(
        manager,
        text="⚙️ Team Manager",
        font=("Segoe UI", 24, "bold"),
        bg="#0f172a",
        fg="#38bdf8"
    )

    title.pack(pady=15)

    # Search Box
    search_entry = Entry(
        manager,
        width=30,
        font=("Segoe UI", 13),
        bg="#334155",
        fg="white",
        insertbackground="white",
        bd=0
    )

    search_entry.pack(pady=10)

    # Team List
    team_listbox = Listbox(
        manager,
        width=80,
        height=18,
        font=("Consolas", 11),
        bg="#1e293b",
        fg="white",
        selectbackground="#38bdf8",
        bd=0
    )

    team_listbox.pack(pady=20)

    # Load Teams
    def load_teams(data):

        team_listbox.delete(0, END)

        for team in data:

            team_name = team[0]
            players = team[1]
            points = team[2]

            line = (
                f"{team_name} | "
                f"Points: {points} | "
                f"{players}"
            )

            team_listbox.insert(END, line)

    # Initial Load
    load_teams(get_saved_teams())

    # Search Function
    def search():

        keyword = search_entry.get()

        result = search_team(keyword)

        load_teams(result)

    # Delete Function
    def delete_selected():

        selected = team_listbox.curselection()

        if not selected:
            return

        line = team_listbox.get(selected)

        team_name = line.split("|")[0].strip()

        delete_team(team_name)

        messagebox.showinfo(
            "Deleted",
            "Team deleted successfully!"
        )

        load_teams(get_saved_teams())

    # Buttons
    search_btn = Button(
        manager,
        text="🔍 Search",
        font=("Segoe UI", 11, "bold"),
        bg="#38bdf8",
        fg="black",
        bd=0,
        padx=15,
        pady=8,
        command=search
    )

    search_btn.pack(pady=5)

    delete_btn = Button(
        manager,
        text="🗑 Delete Team",
        font=("Segoe UI", 11, "bold"),
        bg="#ef4444",
        fg="white",
        bd=0,
        padx=15,
        pady=8,
        command=delete_selected
    )

    delete_btn.pack(pady=5)

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
main_frame.pack(pady=5)

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
        cursor="hand2",
        command=lambda c=category: show_players(c)
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

available_list.bind("<Double-Button-1>", add_player)

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

selected_list.bind("<Double-Button-1>", remove_player)

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

# ================= BUTTON FRAME =================

button_frame = Frame(root, bg="#0f172a")
button_frame.pack(pady=15)

# ================= SAVE BUTTON =================

save_button = Button(
    button_frame,
    text="💾 Save Team",
    font=("Segoe UI", 12, "bold"),
    bg="#B70E0E",
    fg="white",
    bd=0,
    padx=18,
    pady=10,
    cursor="hand2",
    command=save_team_data
)

save_button.grid(row=0, column=0, padx=10)

# ================= VIEW TEAMS BUTTON =================

view_button = Button(
    button_frame,
    text="📋 View Teams",
    font=("Segoe UI", 12, "bold"),
    bg="#f4f4f4",
    fg="black",
    bd=0,
    padx=18,
    pady=10,
    cursor="hand2",
    command=view_teams
)

view_button.grid(row=0, column=1, padx=10)

# ================= CALCULATOR BUTTON =================

calculator_button = Button(
    button_frame,
    text="🧮 Calculator",
    font=("Segoe UI", 12, "bold"),
    bg="#facc15",
    fg="black",
    bd=0,
    padx=18,
    pady=10,
    cursor="hand2",
    command=open_score_calculator
)

calculator_button.grid(row=0, column=2, padx=10)

# ================= LEADERBOARD BUTTON =================

leaderboard_button = Button(
    button_frame,
    text="🏆 Leaderboard",
    font=("Segoe UI", 12, "bold"),
    bg="#f97316",
    fg="white",
    bd=0,
    padx=18,
    pady=10,
    cursor="hand2",
    command=open_leaderboard
)

leaderboard_button.grid(row=0, column=3, padx=10)

# ================= TEAM MANAGER BUTTON =================

manager_button = Button(
    button_frame,
    text="⚙️ Team Manager",
    font=("Segoe UI", 12, "bold"),
    bg="#8b5cf6",
    fg="white",
    bd=0,
    padx=18,
    pady=10,
    cursor="hand2",
    command=open_team_manager
)

manager_button.grid(row=0, column=4, padx=10)


# ================= RUN APP =================

root.mainloop()