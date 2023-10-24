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

# Example formats for missing game data
example_formats = {
    "turn": "Turn: 1",
    "time": "Time: Morning",
    "day": "Day: 1",
    "weather": "Weather: Sunny",
    "health": "Health: 100/100",
    "xp": "XP: 0",
    "ac": "AC: 10",
    "level": "Level: 1",
    "location": "Location: Village Center",
    "gold": "Gold: 10",
    "silver": "Silver: 50",
    "bronze": "Bronze: 100",
    "wearing": "Wearing: Simple Tunic, Leather Boots",
    "wielding": "Wielding: Iron Sword",
    "status_effects": "Status Effects: None",
    "description": "Description: A quiet village square.",
    "inventory": "Inventory: [List items]",
    "abilities": "Abilities: Strength (10), Intelligence (8)",
    "quest": "Quest: Seek the elder.",
    "commands": "Commands: 1. Walk around, 2. Talk to villagers"
}


