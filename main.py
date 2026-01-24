import random
import time

import discord

from constants import MATRIX_PATH, TOKEN_PATH, COOLDOWN_SECONDS
from matrix import load_matrix
from generator import generate_sentence


matrix = load_matrix(MATRIX_PATH)
all_SOL = [key for key in matrix.keys() if key[0] == '[SOL]'] # all starting words

# discord stuff
with open(TOKEN_PATH, 'r', encoding='utf8') as f:
    token = f.read()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

last_response_time = 0

@client.event
async def on_ready():
    print(f'logged in as {client.user}')

@client.event
async def on_message(message):
    global last_response_time

    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        current_time = time.time()

        if current_time - last_response_time < COOLDOWN_SECONDS:
            return

        starting_words = all_SOL[random.randint(0, len(all_SOL) - 1)]
        output = generate_sentence(matrix, starting_words, temperature=10)

        await message.reply(output)

client.run(token)