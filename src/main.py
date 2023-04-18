from discord.ext import commands
import discord
from music_commands import music_commands
from fighting_commands import fighting_commands
from game_commands import game_commands
from utility_commands import utility_commands

import os

TOKEN = "MTAzNzM4ODcwMTE3NDU5NTY2NQ.GWKvji.jXYz-hECk-p5SuZTuJh9gWwLueR6XXzDCOs1M0" #os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="-", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} on ready')

bot.add_cog(music_commands(bot))
bot.add_cog(fighting_commands(bot))
bot.add_cog(game_commands(bot))
bot.add_cog(utility_commands(bot))

bot.run(TOKEN)
