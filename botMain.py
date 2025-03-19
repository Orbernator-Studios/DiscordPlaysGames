
import discord
import os
from discord.ext import commands
import time

import mGBA

dpg_run = 0
emulator = ("0")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def bot_on():
    global dpg_run
    dpg_run = 1

def bot_off():
    global dpg_run
    dpg_run = 0
def KeyPress(button):
    if dpg_run == 1:
        time.sleep(0.2)
        if button == "up":
            if emulator == "mGBA":
                mGBA.UP()
        elif button == "down":
            if emulator == 'mGBA':
                mGBA.DOWN()
        elif button == "left":
            if emulator == "mGBA":
                mGBA.LEFT()
        elif button == "right":
            if emulator == "mGBA":
                mGBA.RIGHT()
        elif button == "a":
            if emulator == "mGBA":
                mGBA.A()
        elif button == "b":
            if emulator == "mGBA":
                mGBA.B()
        elif button == "start":
            if emulator == "mGBA":
                mGBA.START()
        elif button == "select":
            if emulator == "mGBA":
                mGBA.SELECT()
        else:
            exit("KEYPRESSFAILURE")



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
@commands.is_owner()
async def setemu(ctx, arg):
    global emulator
    if dpg_run == 1:
        await ctx.send("Please disable the bot first.")
    elif dpg_run == 0:
        await ctx.send('Searching for emulator '+ arg +'...')
        if arg == ("mGBA"):
            emulator = ("mGBA")
            import mGBA
            await ctx.send('mGBA configs enabled')
        else:
            await ctx.send('Emulator not found. Please try again.')
    else:
        await ctx.send('CRITICAL FAILURE. RESTART BOT. (DPGRun val error)')

@bot.command()
async def bintro(ctx):
    await ctx.send('Welcome to Discord Plays Games!')
    await ctx.send('This bot has been created by Orbernator Studios')
    await ctx.send('To use this bot please message the bot hoster')





@bot.command()
async def botstart(ctx):
    if dpg_run == 0:
        await ctx.send('DPG NOW ENABLED')
        bot_on()
    elif dpg_run == 1:
        await ctx.send('Bot already started')
    else:
        await ctx.send('CRITICAL ERROR. RESTART BOT. (DPG run val)')

@bot.command()
async def stop(ctx):
    if dpg_run == 0:
        await ctx.send('Bot already disabled')
    elif dpg_run == 1:
        await ctx.send('DPG DISABLED')
        bot_off()
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



bot.run('PUT_TOKEN_HERE')
