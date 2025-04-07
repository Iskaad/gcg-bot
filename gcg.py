import discord
from discord.ext import commands
import os

# Récupérer le token depuis la variable d'environnement
TOKEN = os.getenv("DISCORD_TOKEN")

# Paramètres du bot
TARGET_CHANNEL_ID = 888954801877057546  # Canal où notre bot enverra un message
ALLOWED_BOTS = ["Charlemagne"]  # Liste des bots à écouter (par leur nom)
LISTEN_CHANNEL_ID = 1010989803342401588  # ID du canal où le bot écoute les messages

# Initialisation des intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Nécessaire pour lire le contenu des messages
intents.presences = False
intents.typing = False

# Création du bot avec les intents définis
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")


@bot.event
async def on_message(message):
    # Vérifie que le message provient d'un bot autorisé et n'est pas dans le canal cible
    if message.author.bot and message.author.name in ALLOWED_BOTS and message.channel.id != TARGET_CHANNEL_ID:
        target_channel = bot.get_channel(TARGET_CHANNEL_ID)
        if target_channel:
            await target_channel.send(
                f"Un nouveau ticket a été créé dans {message.channel.mention} !"
            )

    # Tester si le bot reçoit le mot 'Oscar' (insensible à la casse)
    if message.channel.id == LISTEN_CHANNEL_ID and message.content.lower(
    ) == "oscar":
        await message.channel.send("Operationnel")

    # Assurer que le bot peut traiter les commandes
    await bot.process_commands(message)


# Lancer le bot avec le token récupéré
bot.run(TOKEN)
