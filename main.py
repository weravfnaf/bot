import discord
import random
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(1298657392916955258)  
    if channel is not None:
        await channel.send("Чем могу помочь?")

@bot.command()
async def Фотки_глобального_потепление(ctx):
    images = os.listdir('images')
    rand_image = random.choice(images)
    with open(f'images/{rand_image}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def фотки_глобального_потепление(ctx):
    images = os.listdir('images')
    rand_image = random.choice(images)
    with open(f'images/{rand_image}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
    await ctx.send(file=picture)

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

@bot.command()
async def О_чем_этот_бот(ctx):
    await ctx.send(f'Этот бот служит для разгаворов и глобального потепления')

@bot.command()
async def о_чем_этот_бот(ctx):
    await ctx.send(f'Этот бот служит для разгаворов и глобального потепления')

@bot.command()
async def Как_тебя_зовут(ctx):
    await ctx.send(f'{bot.user}!')

@bot.command()
async def как_тебя_зовут(ctx):
    await ctx.send(f'{bot.user}!')

@bot.command()
async def Кто_тебя_создал(ctx):
    await ctx.send(f'Секрет')

@bot.command()
async def кто_тебя_создал(ctx):
    await ctx.send(f'Секрет')

@bot.command()
async def Сколько_человек_тебя_создает(ctx):
    await ctx.send(f'3')

@bot.command()
async def сколько_человек_тебя_создает(ctx):
    await ctx.send(f'3')

@bot.command()
async def Во_что_можно_поиграть(ctx):
    await ctx.send(f'Rust ,CS2 ,Subnatica ,Among Us ,Deadlock ,Dota 2 ,Unturned ,Minecraft ,Roblox ,Stumble Guys ,Brawl Stars')

@bot.command()
async def во_что_можно_поиграть(ctx):
    await ctx.send(f'Rust ,CS2 ,Subnatica ,Among Us ,Deadlock ,Dota 2 ,Unturned ,Minecraft ,Roblox ,Stumble Guys ,Brawl Stars')

@bot.command()
async def info(ctx):
    await ctx.send(f'здравствуйте это info и в данный момент у нас есть команды: 1)Что-такое-глобальное-потепление 2)Что-сейчас-с-потеплением 3)фотки_глобального_потепление 4)Во-что-можно-поиграть. Да и вообще здесь есть много простых команд по типу: как-тебя-зовут или кто-тебя-создал')


@bot.command()
async def Info(ctx):
    await ctx.send(f'здравствуйте это info и в данный момент у нас есть команды: 1)Что-такое-глобальное-потепление 2)Что-сейчас-с-потеплением 3)фотки-глобальногопотепление 4)Во-что-можно-поиграть. Да и вообще здесь есть много простых команд по типу: как-тебя-зовут или кто-тебя-создал')

@bot.command()
async def secretinfo(ctx):
    await ctx.send(f'секретное инfo: есть мемасы(meme) и "аллея авторов"(avtor)')

@bot.command()
async def Secretinfo(ctx):
    await ctx.send(f'секретное инfo: есть мемасы(meme) и "аллея авторов"(avtor)')

#------------------------------Глобальное Потепление------------------------------#
@bot.command()
async def что_сейчас_с_потеплением(ctx):
    await ctx.send(f'Последствия глобального потепления включают повышение уровня моря, региональные изменения осадков, более частые экстремальные погодные явления, такие как жара и расширение пустынь.')

@bot.command()
async def Что_сейчас_с_потеплением(ctx):
    await ctx.send(f'Последствия глобального потепления включают повышение уровня моря, региональные изменения осадков, более частые экстремальные погодные явления, такие как жара и расширение пустынь.')

@bot.command()
async def Что_такое_глобальное_потепление(ctx):
    await ctx.send(f'Глоба́льное потепле́ние — долгосрочное повышение средней температуры климатической системы Земли, происходящее уже более века, основной причиной чего, по мнению подавляющего большинства учёных, является человеческая деятельность (антропогенный фактор)[⇨].Повышение температуры поверхности Земли с конца XIX века.Начиная с 1850 года, в десятилетнем масштабе температура воздуха в каждое десятилетие была выше, чем в любое предшествующее десятилетие. С 1750—1800 годов человек ответственен за повышение средней глобальной температуры на 0,8—1,2 °C. Вероятная величина дальнейшего роста температуры на протяжении XXI века на основе климатических моделей составляет 0,3—1,7 °C для минимального сценария эмиссии парниковых газов, 2,6—4,8 °C — для сценария максимальной эмиссии.Последствия глобального потепления включают повышение уровня моря, региональные изменения осадков, более частые экстремальные погодные явления[англ.], такие как жара и расширение пустынь[⇨]. Как указывается на сайте ООН, существуют тревожные свидетельства того, что превышение пороговых показателей, ведущее к необратимым изменениям в экосистемах и климатической системе нашей планеты, уже произошло.')

@bot.command()
async def что_такое_глобальное_потепление(ctx):
    await ctx.send(f'Глоба́льное потепле́ние — долгосрочное повышение средней температуры климатической системы Земли, происходящее уже более века, основной причиной чего, по мнению подавляющего большинства учёных, является человеческая деятельность (антропогенный фактор)[⇨].Повышение температуры поверхности Земли с конца XIX века.Начиная с 1850 года, в десятилетнем масштабе температура воздуха в каждое десятилетие была выше, чем в любое предшествующее десятилетие. С 1750—1800 годов человек ответственен за повышение средней глобальной температуры на 0,8—1,2 °C. Вероятная величина дальнейшего роста температуры на протяжении XXI века на основе климатических моделей составляет 0,3—1,7 °C для минимального сценария эмиссии парниковых газов, 2,6—4,8 °C — для сценария максимальной эмиссии.Последствия глобального потепления включают повышение уровня моря, региональные изменения осадков, более частые экстремальные погодные явления[англ.], такие как жара и расширение пустынь[⇨]. Как указывается на сайте ООН, существуют тревожные свидетельства того, что превышение пороговых показателей, ведущее к необратимым изменениям в экосистемах и климатической системе нашей планеты, уже произошло.')

@bot.command()
async def Надо_делать_f(ctx):
    images = os.listdir('image1')
    rand_image = random.choice(images)
    with open(f'image1/{rand_image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def надо_делать_f(ctx):
    images = os.listdir('image1')
    rand_image = random.choice(images)
    with open(f'image1/{rand_image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def Не_надо_делать_f(ctx):
    images = os.listdir('image2')
    rand_image = random.choice(images)
    with open(f'image2/{rand_image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
    
@bot.command()
async def не_надо_делать_f(ctx):
    images = os.listdir('image2')
    rand_image = random.choice(images)
    with open(f'image2/{rand_image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def meme(ctx):
    images = os.listdir('magesmem')
    rand_image = random.choice(images)
    with open(f'magesmem/{rand_image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def Meme(ctx):
    images = os.listdir('magesmem')
    rand_image = random.choice(images)
    with open(f'magesmem/{rand_image}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def Avtor(ctx):
    await ctx.send(f'авторы Артём или Artmag(artемаг,артемаг) занимался инфо и секретами , Джамал или Jm занимался базовыми командами, Семён или "какой-то чел" или spinatic. занимался командами и поиском инфы')

@bot.command()
async def avtor(ctx):
    await ctx.send(f'авторы Артём или Artmag(artемаг,артемаг) занимался инфо и секретами , Джамал или Jm занимался базовыми командами, Семён или "какой-то чел" или spinatic. занимался командами и поиском инфы')


@bot.command()
async def Посхалочка(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=dQw4w9WgXcQhttps://www.youtube.com/watch?v=dQw4w9WgXcQ')

@bot.command()
async def посхалочка(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=dQw4w9WgXcQhttps://www.youtube.com/watch?v=dQw4w9WgXcQ')

@bot.command()
async def откуда_инфа(ctx):
     WWW.WIKIPEDIA.COM, а чего вы ожидали что я отвечу?

@bot.command()
async def Откуда_инфа(ctx):
     WWW.WIKIPEDIA.COM, а чего вы ожидали что я отвечу?
