import discord
from discord.ext import commands
import os
import giphy_client
from giphy_client.rest import ApiException
from discord import Activity, ActivityType
import keep_alive
import json
import random
import requests
import nekos

bot = commands.Bot(command_prefix="%",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Бот жив")
    await bot.change_presence(status=discord.Status.idle,activity=Activity(type=ActivityType.watching, name="в бездну"))

bot.remove_command('help')


@bot.event
async def on_member_join(member):
  embed = discord.Embed(title = f"**======== E N T I T Y ========\n====== Welcome Home ======**",description=f"Будь уверен, здесь тебе всегда рады!\nТакже не забудь прочитать [**правила**](https://discord.gg/cx3EPg7)." ,colour = 0x2b2d33)
  embed.set_image(url=f"https://cdn.discordapp.com/attachments/839218117691047946/841711460711268392/welcome_home_2.png")
  await member.send(embed = embed)


@bot.command()
async def welcum(ctx):
    embed = discord.Embed(color=0x2b2d33)
    embed.set_image(url=f"https://cdn.discordapp.com/attachments/839218117691047946/841711460711268392/welcome_home_2.png")
    await ctx.message.delete()
    await ctx.send(embed=embed)

@bot.command()
async def roles(ctx):
    embed = discord.Embed(color=0x2b2d33)
    embed.set_image(url=f"https://cdn.discordapp.com/attachments/721027138190442540/842708110527561758/kIUJvyKcmzDyERGFw9Gphm4O84vElCJv7MaWbMmwa4NJDJDnItQQlEVCyK-gHPGgdIr7lY3pLqGkCOo1U_X8Pg3D3D.png")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
async def rules(ctx):
    embed = discord.Embed(color=0x2b2d33)
    embed.set_image(url=f"https://cdn.discordapp.com/attachments/721027138190442540/842709764713742366/oUR_BZHMsG7P3jqAlVjOjpd4_iIYN_eZzrNljikWK5ZUp03sLeMj7-INs7RsReCzVDLM0d9nTD3uarOfhsRmkA3D3D.png")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
async def magaz(ctx):
    embed = discord.Embed(color=0x2b2d33)
    embed.set_image(url=f"https://cdn.discordapp.com/attachments/721027138190442540/842710033561288724/nuHqwZjhMhjVoULQQuz6Opd4_iIYN_eZzrNljikWK5YyeAl2fXalWp20NMeVx43twyyOT9ppAjBsmfd8uaD9tA3D3D.png")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
async def sponsors(ctx):
    embed = discord.Embed(color=0x2b2d33)
    embed.set_image(url=f"https://cdn.discordapp.com/attachments/721027138190442540/842710301362618378/o8vYmq8jlLG609u7VKAGgZd4_iIYN_eZzrNljikWK5Zebx_HsqxAx4waHgV3EIzfyF1nlWUYg85l9NV7qcZaUA3D3D.png")
    await ctx.message.delete()
    await ctx.send(embed=embed)

@bot.command() #автороли 2
@commands.has_permissions(manage_roles=True)
async def reactrole(ctx, emoji, role: discord.Role, *, msg: discord.Message=None):

    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {'role_name': role.name, 
        'role_id': role.id,
        'emoji': emoji,
        'message_id': msg.id}

        data.append(new_react_role)

    with open('reactrole.json', 'w') as f:
        json.dump(data, f, indent=4)
    await ctx.channel.send("Реакция поставлена")

@bot.event
async def on_raw_reaction_add(payload):

    if payload.member.bot:
        pass

    else:
        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(bot.get_guild(
                        payload.guild_id).roles, id=x['role_id'])

                    await payload.member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):

    with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for x in data:
            if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                role = discord.utils.get(bot.get_guild(
                    payload.guild_id).roles, id=x['role_id'])

                
                await bot.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)


@bot.command() #гифки
async def gif(ctx,*,q="random"):
 
    api_key="wpaaz96BkzEVav3qQ9Z78KFAxQBjOcy5" #надо получить API ключ на сайте https://developers.giphy.com/
    api_instance = giphy_client.DefaultApi()
 
    try: 
 
 
        api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)
 
        emb = discord.Embed(color = 0x2b2d33)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
 
        await ctx.channel.send(embed=emb)
        await ctx.message.delete()
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


@bot.command()
@commands.has_permissions(manage_messages = True)
async def sg(ctx,q="random",  *, text: str = 'Здесь мог быть ваш текст.'):
    api_key="wpaaz96BkzEVav3qQ9Z78KFAxQBjOcy5"
    api_instance = giphy_client.DefaultApi()
 
    try: 
 
 
        api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)
 
        emb = discord.Embed(description=text, color = 0x2b2d33)
        emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')
        await ctx.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


@bot.command()  # help
async def help(ctx, *args):
    embed = discord.Embed(title="Навигация по командам", colour=0xc582ff)
    embed.add_field(name="Модерация", value="clean", inline=False)
    embed.add_field(name="Развлечение", value="neko(nsfw), cat, kiss, roll\nflip, worth, hug, gif, feed, pat", inline=False)
    embed.add_field(name="Утилиты", value="inf, send, test, invite", inline=False)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)


@bot.command()
async def test(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=discord.Embed(description=("**Все прекрасно!**"), color=0xc582ff))


@bot.command()
async def inf(ctx, member: discord.Member):
    emb = discord.Embed(title='Информация о пользователе', color=0xc582ff)
    emb.add_field(name="Когда присоединился:", value=member.joined_at, inline=False)
    emb.add_field(name='Имя:', value=member.display_name, inline=False)
    emb.add_field(name='Айди:', value=member.id, inline=False)
    emb.add_field(name="Аккаунт был создан:", value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),
                  inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Вызвано:{ctx.message.author}", icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
    await ctx.message.delete()
    await ctx.send(embed=emb)


@bot.command()           # очистка сообщений
@commands.has_permissions(manage_messages=True)
async def clean(ctx, amount=None):
    await ctx.channel.purge(limit=int(amount) + 1)
    await ctx.send(embed=discord.Embed(description=(f'**Очищено {amount} сообщений!**'), color=0xc582ff))


@bot.event  # voice 
async def on_voice_state_update(member, before, after):
    if after.channel.id == 789601886281138206:  # entity ивенты
        maincategory = discord.utils.get(member.guild.categories, id=789601583578087454)
        channel3 = await member.guild.create_voice_channel(name=f'Ивентная комната', category=maincategory)
        await member.move_to(channel3)
        await channel3.set_permissions(member, connect=True,  move_members=True, manage_channels=True)

        def check(a, b, c):
            return len(channel3.members) == 0

        await bot.wait_for('voice_state_update', check=check)
        await channel3.delete()
        
    if after.channel.id == 757642643386925217:  # entity х4
            maincategory = discord.utils.get(member.guild.categories, id=823692983957454868)
            channel4 = await member.guild.create_voice_channel(name=f'Комната для 4', user_limit=4, category=maincategory)
            await member.move_to(channel4)

            def check(x, y, z):
                return len(channel4.members) == 0

            await bot.wait_for('voice_state_update', check=check)
            await channel4.delete()
           
    if after.channel.id == 757642886513819779:  # entity х5
        maincategory = discord.utils.get(member.guild.categories, id=823692983957454868)
        channel5 = await member.guild.create_voice_channel(name=f'Комната для 5', user_limit=5, category=maincategory)
        await member.move_to(channel5)

        def check(x, y, z):
            return len(channel5.members) == 0

        await bot.wait_for('voice_state_update', check=check)
        await channel5.delete()
        
    if after.channel.id == 777598798604009473:  # entity х6
        maincategory = discord.utils.get(member.guild.categories, id=823692983957454868)
        channel6 = await member.guild.create_voice_channel(name=f'Комната для 6', user_limit=6, category=maincategory)
        await member.move_to(channel6)

        def check(x, y, z):
            return len(channel6.members) == 0

        await bot.wait_for('voice_state_update', check=check)
        await channel6.delete()
        
    if after.channel.id == 777598785840873542:  # entity х10
        maincategory = discord.utils.get(member.guild.categories, id=823692983957454868)
        channel7 = await member.guild.create_voice_channel(name=f'Комната для 10', user_limit=10, category=maincategory)
        await member.move_to(channel7)

        def check(x, y, z):
            return len(channel7.members) == 0

        await bot.wait_for('voice_state_update', check=check)
        await channel7.delete()
    if after.channel.id == 831896788398243912:  # entity х3
        maincategory = discord.utils.get(member.guild.categories, id=823692983957454868)
        channel8 = await member.guild.create_voice_channel(name=f'Комната для 3', user_limit=3, category=maincategory)
        await member.move_to(channel8)

        def check(x, y, z):
            return len(channel8.members) == 0

        await bot.wait_for('voice_state_update', check=check)
        await channel8.delete()


@bot.command()  # ссылка на инвайт бота
async def invite(ctx):
    await ctx.message.delete()
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=821594015589466173&permissions=8&scope=bot")


@bot.listen("on_command_error")
async def cooldown_message(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.message.delete()

@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command()
async def hug(ctx, member: discord.Member):
    embed = discord.Embed(description = f'{member.mention}, тебя обнимает {ctx.message.author.mention}', color=0xc582ff )
    embed.set_image(url=nekos.img('hug'))
    await ctx.message.delete()
    await ctx.send(embed=embed)

@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command()
async def feed(ctx, member: discord.Member):
    embed = discord.Embed(description = f'{member.mention}, тебя кормит {ctx.message.author.mention}', color=0xc582ff )
    embed.set_image(url=nekos.img('feed'))
    await ctx.message.delete()
    await ctx.send(embed=embed)
    

@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command()
async def pat(ctx, member: discord.Member):
    embed = discord.Embed(description = f'{member.mention}, тебя гладит {ctx.message.author.mention}', color=0xc582ff )
    embed.set_image(url=nekos.img('pat'))
    await ctx.message.delete()
    await ctx.send(embed=embed)

  
@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command()
async def kiss(ctx, member: discord.Member):
    embed = discord.Embed(description = f'{member.mention}, тебя целует {ctx.message.author.mention}', color=0xc582ff )
    embed.set_image(url=nekos.img('kiss'))
    await ctx.message.delete()
    await ctx.send(embed=embed)


@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command()
async def punch(ctx, member: discord.Member):
    embed = discord.Embed(description = f'{member.mention}, тебя стукнул(а) {ctx.message.author.mention}', color=0xc582ff )
    embed.set_image(url=nekos.img('slap'))
    await ctx.message.delete()
    await ctx.send(embed=embed)


@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command()
async def tickle(ctx, member: discord.Member):
    embed = discord.Embed(description = f'{member.mention}, тебя щекочет {ctx.message.author.mention}', color=0xc582ff )
    embed.set_image(url=nekos.img('tickle'))
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
async def flip(ctx):
    name = ('Вам выпал орёл', 'Вам выпала решка')
    await ctx.message.delete()
    await ctx.send(embed=discord.Embed(description=(f'{ctx.message.author.mention}, **{random.choice(name)}**'), color=0xc582ff))


@bot.command()
async def worth(ctx):
    embed = discord.Embed(description = f'{ctx.message.author.mention},', color=0xc582ff )
    embed.set_image(url=nekos.img('8ball'))
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)
    embed = discord.Embed(color=0xc582ff, title='Случайный котик')
    embed.set_image(url=json_data['link'])
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_messages = True)
async def send(ctx,  *, text: str = 'Здесь мог быть ваш текст.'):
    embed = discord.Embed(color=0x2b2d33, description=text)
    await ctx.message.delete()
    await ctx.send(embed=embed)


Arguments = "feet, yuri, trap, futanari, hololewd, lewdkemo, solog, feetg, cum, erokemo, les, wallpaper, lewdk, ngif, tickle, lewd, feed, gecg, eroyuri, eron, cum_jpg, bj, nsfw_neko_gif, solo, kemonomimi, nsfw_avatar, gasm, poke, anal, slap, hentai, avatar, erofeet, holo, keta, blowjob, pussy, tits, holoero, lizard, pussy_jpg, pwankg,classic, kuni, waifu, pat, 8ball, kiss, femdom, neko, spank, cuddle, erok, fox_girl, boobs, random_hentai_gif, smallboobs, hug, ero, smug, goose, baka, woof"


def is_nsfw():
    async def predicate(ctx):
        return ctx.channel.is_nsfw()

    return commands.check(predicate)


@bot.command()
@is_nsfw()
async def neko(ctx, get=None):
    if get is None:
        await ctx.message.delete()
        await ctx.send(
            embed=discord.Embed(color=0xc582ff, title='Выбери одно',
                                description=f'{Arguments}'))
    emb = discord.Embed(color=0xc582ff)
    emb.set_image(url=nekos.img(get))
    await ctx.message.delete()
    await ctx.send(embed=emb)

@commands.cooldown(1, 120, commands.BucketType.user)
@is_nsfw()
@bot.command()
async def spank(ctx, member: discord.Member):
    embed = discord.Embed(description = f'{member.mention}, тебя отшлёпал {ctx.message.author.mention}', color=0xc582ff )
    embed.set_image(url=nekos.img('spank'))
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command() #выдать пацанскую роль
@commands.has_permissions(view_audit_log = True)
async def boy(ctx, member:discord.Member):
  role = discord.utils.get(member.guild.roles, id=827323597755514941)
  girl = discord.utils.get(member.guild.roles, id=736933395292225539)
  await member.remove_roles(girl)
  await member.add_roles(role)
  await ctx.message.delete()
  emb = discord.Embed(title=f'Выдана роль {role}', color=0x2b2d33)
  emb.add_field(name="Участнику", value=member.name, inline=False)
  emb.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)  
  await ctx.send(embed=emb)


@bot.command() #выдать бабскую роль
@commands.has_permissions(view_audit_log = True)
async def girl(ctx, member:discord.Member):
  role = discord.utils.get(member.guild.roles, id=736933395292225539)
  boy = discord.utils.get(member.guild.roles, id=827323597755514941)
  await member.remove_roles(boy)
  await member.add_roles(role)
  await ctx.message.delete()
  emb = discord.Embed(title=f'Выдана роль {role}', color=0x2b2d33)
  emb.add_field(name="Участнику", value=member.name, inline=False)
  emb.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)  
  await ctx.send(embed=emb)


@bot.command() #дать потрогать NSFW 
@commands.has_permissions(view_audit_log = True)
async def old(ctx, member:discord.Member):
  role = discord.utils.get(member.guild.roles, id=736731230309187584)
  await member.add_roles(role)
  await ctx.message.delete()
  emb = discord.Embed(title=f'Выдана роль {role}', color=0x2b2d33)
  emb.add_field(name="Участнику", value=member.name, inline=False)
  emb.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)  
  await ctx.send(embed=emb)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            embed=discord.Embed(description=f'** {ctx.author.name}, данной команды не существует.**', color=0x2b2d33))


my_secret = os.environ['Bot_secret']
keep_alive.keep_alive()
bot.run(my_secret)