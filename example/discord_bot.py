from discord.ext import commands
from inworld_python import inworld_chat

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "!", intents=intents)

chat_app = inworld_chat.InWorldChat('inworld_key', 
                       'inworld_secret', 
                       'inworld_scene'
                      )

chat_app.setup()

@bot.command()
async def iw(ctx, *, query):
    out = chat_app.chat(query, str(ctx.author), str(ctx.channel.id), str(ctx.author.id))
    await ctx.reply(out)

@bot.event
async def on_ready():
    print('Bot is ready')

bot.run('your-bot-token')
