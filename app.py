import tkinter as tk
from tkinter import scrolledtext, simpledialog
import openai
import json
import os
from collections import OrderedDict
import config
import random

# OpenAI API Key
openai.api_key = config.OPENAI_API_KEY

# Read the content of gamemaster.txt
with open("gamemaster.txt", "r") as file:
    game_prompt = file.read()

# LRU Cache
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: str) -> str:
        if key not in self.cache:
            return ""
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: str, value: str) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

cache = LRUCache(100)
turn_counter = 0
game_state = "start"

# Create directories if they don't exist
directories = [config.PLAYER_DIR, config.ENEMY_DIR, config.NPC_DIR, config.LOCATION_DIR, config.QUEST_DIR, config.SPELL_DIR, config.GAME_STATE_DIR]
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to save data to JSON
def save_to_json(data, directory, filename):
    with open(os.path.join(directory, filename), 'w') as file:
        json.dump(data, file)

# Function to load data from JSON
def load_from_json(directory, filename):
    with open(os.path.join(directory, filename), 'r') as file:
        return json.load(file)

# Create the main window
root = tk.Tk()
root.title("Grimblood's Adventure")
root.geometry("400x500")

# Create the chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=45, height=25, font=("Arial", 10))
chat_window.pack(pady=10)
chat_window.configure(state=tk.DISABLED)

# Create the entry box for user input
entry_box = tk.Text(root, wrap=tk.WORD, width=45, height=5, font=("Arial", 10))
entry_box.pack(pady=10)

# Function to handle sending a message
def send():
    global turn_counter, game_state
    msg = entry_box.get("1.0", 'end-1c').strip()
    entry_box.delete("1.0", tk.END)
    
    if msg:
        chat_window.configure(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {msg}\n")
        chat_window.configure(state=tk.DISABLED)

        cache_key = f"{game_state}_{msg}"
        cached_response = cache.get(cache_key)

        if cached_response:
            bot_response = cached_response
        else:
            # Integrate combat and NPC interactions here
            if "attack" in msg:
                # Placeholder for combat logic
                damage = random.randint(5, 20)  # Example damage calculation
                bot_response = f"You attacked and dealt {damage} damage."
            elif "talk to" in msg:
                # Placeholder for NPC interaction logic
                bot_response = "The NPC shares some valuable information with you."
            else:
                response = openai.Completion.create(
                    model="gpt-3.5-turbo",
                    prompt=f"{game_prompt}\n\nUser: {msg}\nGrimblood:",
                    max_tokens=150
                )
                bot_response = response.choices[0].text.strip()
            cache.set(cache_key, bot_response)

        chat_window.configure(state=tk.NORMAL)
        chat_window.insert(tk.END, f"Grimblood: {bot_response}\n")
        chat_window.configure(state=tk.DISABLED)
        chat_window.see(tk.END)

        turn_counter += 1
        if turn_counter > 10:
            game_state = "next_phase"
            chat_window.insert(tk.END, f"Hint: Try doing something different.\n")

# Create the send button
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send)
send_button.pack(pady=10)

# Starting the Tkinter main loop
root.mainloop()
