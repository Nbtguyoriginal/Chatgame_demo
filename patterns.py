patterns = {
    "turn": r"Turn: (\d+)",
    "time": r"Time: ([\w\s]+)",
    "day": r"Day: (\d+)",
    "weather": r"Weather: ([\w\s]+)",
    "health": r"Health: (\d+/\d+)",
    "xp": r"XP: (\d+)",
    "ac": r"AC: (\d+)",
    "level": r"Level: (\d+)",
    "location": r"Location: ([\w\s]+)",
    "gold": r"Gold: (\d+)",
    "silver": r"Silver: (\d+)",
    "bronze": r"Bronze: (\d+)",
    "wearing": r"Wearing: ([\w\s,]+)",
    "wielding": r"Wielding: ([\w\s,\(\)]+)",
    "status_effects": r"Status Effects: ([\w\s,\(\)]+)",
    "description": r"Description:\s*\n(.*?)(?:\n-{3,}|\Z)",
    "inventory": r"Inventory:\s*\n(.*?)(?:\n-{3,}|\Z)",
    "abilities": r"Abilities:\s*\n(.*?)(?:\n-{3,}|\Z)",
    "quest": r"Quest:\s*\n(.*?)(?:\n-{3,}|\Z)",
    "commands": r"Commands:\s*\n(.*?)(?:\n-{3,}|\Z)"
}

