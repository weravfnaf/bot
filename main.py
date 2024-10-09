import discord
import random
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)
#привествия--------------------------------------------------------------
@bot.command()
async def Hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def Hi(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def hi(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def Привет(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def привет(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def Как_дела(ctx):
    await ctx.send(f'Хорошо !')

@bot.command()
async def как_дела(ctx):
    await ctx.send(f'Хорошо !')

@bot.command()
async def Как_жизнь(ctx):
    await ctx.send(f'Прекрасно !')

@bot.command()
async def как_жизинь(ctx):
    await ctx.send(f'Прекрасно !')

@bot.command()
async def Что_делаешь(ctx):
    await ctx.send(f'Вам помогаю !')

@bot.command()
async def что_делаешь(ctx):
    await ctx.send(f'Вам помогаю !')
#-------------------------------------------------------------------------

@bot.command()
async def Help(ctx):
    await ctx.send(f'В этом боте есть базовые команды к примеру привет но необычные команды написоны в команде Info')



bot.run("MTIyNzIyNjk2MjMyNjcxNjUxNg.GwzbZy.NE1z7AKSbbBrjTtV1V_XsS8b5c0IAAl7Ca1_Oc")
