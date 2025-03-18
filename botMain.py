
import discord
import os
from discord.ext import commands
import pyautogui
import time

DPGRun = (0)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def KeyPress(button):
    if DPGRun == 1:
        if button == "up":
            pyautogui.press('up')
        elif button == "down":
            pyautogui.press('down')
        elif button == "left":
            pyautogui.press('left')
        elif button == "right":
            pyautogui.press('right')
        elif button == "a":
            pyautogui.press('x')
        elif button == "b":
            pyautogui.press('z')
        elif button == "start":
            pyautogui.press('0')
        elif button == "select":
            pyautogui.press('1')
        else:
            exit("KEYPRESSFAILURE")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def bintro(ctx):
    await ctx.send('Welcome to Discord Plays Games!')
    await ctx.send('This bot has been created by Orbernator Studios')
    await ctx.send('To use this bot please message Orbernator')

@bot.command()
@commands.is_owner
async def botstart(ctx):
    if DPGRun == 0:
        await ctx.send('DPG NOW ENABLED')
        DPGRun = 1
    elif DPGRun == 1:
        await ctx.send('Bot already started')
    else:
        await ctx.send('CRITICAL ERROR. RESTART BOT. (DPG run val)')

@bot.command()
async def stop(ctx):
    if DPGRun == 0:
        await ctx.send('Bot already disabled')
    elif DPGRun == 1:
        await ctx.send('DPG DISABLED')
    else:
        await ctx.send('CRITICAL ERROR. RESTART BOT. (DPG run val)')

# UP COMMANDS HERE
@bot.command()
async def up(ctx):
    KeyPress("up")

@bot.command()
async def u(ctx):
    KeyPress("up")

# DOWN COMMANDS HERE
@bot.command()
async def down(ctx):
    KeyPress("down")

@bot.command()
async def d(ctx):
    KeyPress("down")

# LEFT COMMANDS HERE
@bot.command()
async def left(ctx):
    KeyPress("left")

@bot.command()
async def l(ctx):
    KeyPress("left")

# RIGHT COMMANDS HERE
@bot.command()
async def right(ctx):
    KeyPress("right")

@bot.command()
async def r(ctx):
    KeyPress("right")

# A AND B COMMANDS
@bot.command()
async def a(ctx):
    KeyPress("a")

@bot.command()
async def b(ctx):
    KeyPress("b")

#START AND SELECT COMMANDS
@bot.command()
async def start(ctx):
    KeyPress("start")

@bot.command()
async def select(ctx):
    KeyPress("select")



bot.run(os.getenv('TOKEN'))
