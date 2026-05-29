import sqlite3

conn = sqlite3.connect("database/fantasy_cricket.db")
cur = conn.cursor()

# Create Tables
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

# Sample Players
players = [
    ("Virat Kohli", 250, 12000, 43, 62, 10.0, "BAT"),
    ("Rohit Sharma", 240, 9800, 29, 48, 9.5, "BAT"),
    ("KL Rahul", 120, 4200, 5, 32, 8.5, "BAT"),
    ("Hardik Pandya", 130, 2200, 0, 10, 9.0, "AR"),
    ("Ravindra Jadeja", 170, 2500, 0, 15, 8.5, "AR"),
    ("MS Dhoni", 350, 10700, 10, 73, 8.0, "WK"),
    ("Rishabh Pant", 90, 2400, 2, 11, 8.5, "WK"),
    ("Jasprit Bumrah", 110, 150, 0, 0, 8.5, "BOW"),
    ("Mohammed Shami", 95, 120, 0, 0, 8.0, "BOW"),
    ("Bhuvneshwar Kumar", 130, 300, 0, 0, 7.5, "BOW")
]

# Insert Players
for player in players:
    try:
        cur.execute(
            "INSERT INTO stats VALUES (?, ?, ?, ?, ?, ?, ?)",
            player
        )
    except:
        pass

conn.commit()

print("Player data inserted successfully!")

conn.close()