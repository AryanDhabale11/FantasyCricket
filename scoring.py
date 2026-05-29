# ================= FANTASY POINTS CALCULATOR =================

def calculate_points(
        runs,
        fours,
        sixes,
        wickets,
        catches
):

    points = 0

    # Batting Points
    points += runs * 1
    points += fours * 1
    points += sixes * 2

    # Bowling Points
    points += wickets * 10

    # Fielding Points
    points += catches * 4

    return points