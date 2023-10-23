import json

class GameMaster:
    def __init__(self):
        self.turn = None
        self.time = None
        self.day = None
        self.weather = None
        self.health = None
        self.xp = None
        self.ac = None
        self.level = None
        self.location = None
        self.gold = None
        self.silver = None
        self.bronze = None
        self.wearing = None
        self.wielding = None
        self.status_effects = None
        self.description = None
        self.inventory = None
        self.abilities = None
        self.quest = None
        self.commands = None
        self.action_summary = []

    def update_game_state(self, game_state):
        for key, value in game_state.items():
            setattr(self, key, value)

    def save_to_json(self, file_name="game_state.json"):
        game_state = {attr: getattr(self, attr) for attr in vars(self) if not callable(getattr(self, attr))}
        with open(file_name, 'w') as file:
            json.dump(game_state, file, indent=4)

    def load_from_json(self, file_name="game_state.json"):
        with open(file_name, 'r') as file:
            game_state = json.load(file)
            self.update_game_state(game_state)

    def is_info_missing(self):
        essential_info = ['turn', 'time', 'day', 'weather', 'health', 'xp', 'ac', 'level', 
                          'location', 'gold', 'silver', 'bronze', 'wearing', 'wielding', 
                          'status_effects', 'description', 'inventory', 'abilities', 'quest', 
                          'commands']
        missing_info = [info for info in essential_info if getattr(self, info, None) is None]
        return missing_info

    def construct_request_for_missing_info(self):
        missing_info = self.is_info_missing()
        if missing_info:
            request = f"GameMaster, we are missing information on the following: {', '.join(missing_info)}. " \
                      f"Can you provide the details?"
            return request
        return "All essential information is available."

# Example usage
if __name__ == "__main__":
    game_master = GameMaster()
    game_master.weather = None  # Simulating missing information
    game_master.wielding = None  # Simulating missing information
    print(game_master.construct_request_for_missing_info())  # It should construct a request for missing info
