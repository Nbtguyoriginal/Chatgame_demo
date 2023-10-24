import json
from collections import deque, OrderedDict
from patterns import example_formats  # Importing the formats

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
        self.missing_info_queue = deque()

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

    def check_and_add_to_queue(self, missing_info):
        for info in missing_info:
            if info not in self.missing_info_queue:
                self.missing_info_queue.append(info)

    def group_missing_info(self):
        grouping = [
            ['turn', 'time', 'day', 'weather'],
            ['health', 'xp', 'ac', 'level'],
            ['location', 'gold', 'silver', 'bronze'],
            ['wearing', 'wielding', 'status_effects'],
            ['description', 'inventory', 'abilities', 'quest', 'commands']
        ]
        for group in grouping:
            if all(item in self.missing_info_queue for item in group):
                for item in group:
                    self.missing_info_queue.remove(item)
                return group
        return [self.missing_info_queue.popleft()]

    def construct_request_for_missing_info(self):
        missing_info = self.is_info_missing()
        self.check_and_add_to_queue(missing_info)
        if not self.missing_info_queue:
            return "All essential information is available."

        current_group = self.group_missing_info()
        examples = [example_formats[item] for item in current_group]
        request = f"GameMaster, we need details in the format of: {', '.join(examples)}."
        return request

if __name__ == "__main__":
    game_master = GameMaster()
    game_master.weather = None  # Simulating missing information
    game_master.wielding = None  # Simulating missing information
    print(game_master.construct_request_for_missing_info())  # It should construct a request for missing info
