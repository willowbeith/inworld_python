import discord
from discord.ext import commands
from inworld_python import inworld_chat

# Create a new Intents object with default settings
# These settings include tracking of messages, reactions, etc.
intents = discord.Intents.default()
# Enable tracking of message content
intents.message_content = True

# Initialize the Bot object with the "!" command prefix
# and the specified intents
bot = commands.Bot(command_prefix="!annabella", intents=intents)

# Create an InWorldChat object with the specified key, secret, and scene
chat_app = inworld_chat.InWorldChat('FiOSdrLV1taDFxAQOZ68V9uHFjAtjaPPjNakUINKKapJcTGCTaznjw9eojNGp8ND', 'xaSYoJOltnzJNLfpcnUky0Z909aQMKRz', 'workspaces/default-pi_sllrv-upltj902robew/characters/annabella')

# Set up the InWorldChat object
chat_app.setup()

@bot.command()
async def iw(ctx, *, query):
    """
    This function defines the 'iw' command for the bot.
    When the 'iw' command is used, the bot sends a chat message using the InWorldChat object.
    The message content is then sent as a reply in Discord.

    :param ctx: context object provided by discord.py, contains message details
    :param query: message content to send as chat
    """
    # Send a chat message using the InWorldChat object
    # The message content, author name, channel ID, and author ID are provided as arguments
    out = chat_app.chat(query, str(ctx.author), str(ctx.channel.id), str(ctx.author.id))
    # Reply in Discord with the chat output
    await ctx.reply(out)

@bot.event
async def on_ready():
    """
    This function is run when the bot has connected to Discord and is ready.
    """
    print('Bot is ready')

# Run the bot with the specified token
bot.run('MTExODI3MzkyODA1NDQ0ODM1MA.GcF-i2.0N51Hug97o1e0Ba7AM-ur0oe1JmntLsywyp2Yw')
