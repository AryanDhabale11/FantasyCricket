import sqlite3

DB_PATH = "database/fantasy_cricket.db"

# Connect Database
def connect_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

# Create Tables
def create_tables():

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS stats(
        player TEXT PRIMARY KEY,
        matches INTEGER,
        runs INTEGER,
        hundreds INTEGER,
        fifties INTEGER,
        value REAL,
        ctg TEXT
    )
    """)

    conn.commit()
    conn.close()

# Insert Sample Players
def insert_players():

    conn = connect_db()
    cur = conn.cursor()

    players = [
        ("Virat Kohli", 250, 12000, 43, 62, 10.0, "BAT"),
        ("Rohit Sharma", 240, 9800, 29, 48, 9.5, "BAT"),
        ("Shubman Gill", 75, 2800, 6, 15, 8.5, "BAT"),
        ("KL Rahul", 120, 4200, 5, 32, 8.5, "BAT"),

        ("Hardik Pandya", 130, 2200, 0, 10, 9.0, "AR"),
        ("Ravindra Jadeja", 170, 2500, 0, 15, 8.5, "AR"),
        ("Axar Patel", 80, 1100, 0, 5, 8.0, "AR"),

        ("MS Dhoni", 350, 10700, 10, 73, 8.0, "WK"),
        ("Rishabh Pant", 90, 2400, 2, 11, 8.5, "WK"),
        ("Ishan Kishan", 60, 1800, 1, 9, 7.5, "WK"),

        ("Jasprit Bumrah", 110, 150, 0, 0, 8.5, "BOW"),
        ("Mohammed Shami", 95, 120, 0, 0, 8.0, "BOW"),
        ("Mohammed Siraj", 70, 90, 0, 0, 7.5, "BOW"),
        ("Kuldeep Yadav", 85, 200, 0, 0, 7.5, "BOW"),
        ("Yuzvendra Chahal", 100, 250, 0, 0, 8.0, "BOW")
    ]

    for player in players:
        try:
            cur.execute(
                "INSERT INTO stats VALUES (?, ?, ?, ?, ?, ?, ?)",
                player
            )
        except:
            pass

    conn.commit()
    conn.close()

# Fetch Players by Category
def fetch_players(category):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT player FROM stats WHERE ctg=?",
        (category,)
    )

    players = cur.fetchall()

    conn.close()

    return players

# Run File
create_tables()
insert_players()

print("Database Ready!")

# Save Team
def save_team(team_name, players, value):

    conn = connect_db()
    cur = conn.cursor()

    players_string = ",".join(players)

    cur.execute(
        "INSERT INTO teams VALUES (?, ?, ?)",
        (team_name, players_string, value)
    )

    conn.commit()
    conn.close()

    # Fetch Saved Teams
def get_saved_teams():

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM teams")

    teams = cur.fetchall()

    conn.close()

    return teams

# ================= LEADERBOARD =================

def get_leaderboard():

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT team_name, value
        FROM teams
        ORDER BY value DESC
    """)

    leaderboard = cur.fetchall()

    conn.close()

    return leaderboard