import discord
from colorama import Fore
from discord.ext import commands

w = Fore.WHITE
r = Fore.RED
b = Fore.LIGHTBLACK_EX
g = Fore.LIGHTGREEN_EX
c = Fore.CYAN
m = Fore.LIGHTMAGENTA_EX
ll = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
fr = Fore.RESET
ly = Fore.LIGHTYELLOW_EX

intents = discord.Intents.all()
intents.members = True
token = input(f"{lr}Input your token : {b}")
print(f"""{b}Your prefix is {lr}.{b}

    .msgall <msg>
    .msgid  <userid>

""")

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def msgid(ctx, target: discord.User, *, message):
    try:
        await target.send(message)
        await ctx.send(f'Message sent to user {target.mention} with ID {target.id}')
    except Exception as e:
        await ctx.send(f'Failed to send message to user {target.mention}: {e}')

@bot.command()
async def msgall(ctx, *, message):
    failed_users = []
    for member in ctx.guild.members:
        if member.bot:
            continue
        try:
            await member.send(message)
            await ctx.send(f"Message sent to user {member.mention} with ID {member.id}")
        except discord.Forbidden:
            failed_users.append(member)
        except Exception as e:
            print(f"An error occurred while messaging {member}: {e}")
            continue
    if failed_users:
        failed_users_str = ', '.join(str(member) for member in failed_users)
        await ctx.send(f"Failed to send message to: {failed_users_str}")

bot.run(token)