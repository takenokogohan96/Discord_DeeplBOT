# coding: UTF-8

import discord
from discord.ext import commands
import configparser
import datetime
import requests

#config.ini読み出し
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
discord_bot_token = config_ini.get('TOKEN', 'discord_bot_token')
deepl_api_token = config_ini.get('TOKEN', 'deepl_api_token')
JP_to_EN = config_ini.get('TRIGGEREMOJI', 'JP_to_EN')
EN_to_JP = config_ini.get('TRIGGEREMOJI', 'EN_to_JP')

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

dt_now = datetime.datetime.now()
bot = commands.Bot(command_prefix='!!!',intents=intents)
bot.remove_command('help')

#起動部
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f"JP/EN"))
    print(dt_now.strftime('[%m/%d %H:%M] ') + bot.user.name + 'name:' + bot.user.name)
    print(dt_now.strftime('[%m/%d %H:%M] ') + bot.user.name + 'ID:' + str(bot.user.id))
    print(dt_now.strftime('[%m/%d %H:%M] ') + bot.user.name + 'Logged in as\n')

#翻訳機能部
@bot.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == (JP_to_EN):
        channel = bot.get_channel(payload.channel_id)
        msg = await channel.fetch_message(payload.message_id)
        user = bot.get_user(payload.user_id)
        params = {
            "auth_key": deepl_api_token,
            "text": msg.content,
            "target_lang": 'JA'
        }
        request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
        result = request.json()
        translated_get_text = result["translations"][0]["text"]
        translated_post_text = msg.content
        embed=discord.Embed(color=0x042b48)
        embed.set_thumbnail(url="https://i.imgur.com/eUiRdY4.jpg")
        embed.add_field(name="日本語(Japanese)", value=translated_get_text, inline=False)
        embed.add_field(name="原文(Original)", value=translated_post_text, inline=True)
        embed.set_footer(text= "(" + msg.author.display_name + ")")
        await user.send(embed=embed)
        await msg.remove_reaction(JP_to_EN, user)
    elif payload.emoji.name == (EN_to_JP):
        channel = bot.get_channel(payload.channel_id)
        msg = await channel.fetch_message(payload.message_id)
        user = bot.get_user(payload.user_id)
        params = {
            "auth_key": deepl_api_token,
            "text": msg.content,
            "target_lang": 'EN-US'
        }
        request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
        result = request.json()
        translated_get_text = result["translations"][0]["text"]
        translated_post_text = msg.content
        embed=discord.Embed(color=0x042b48)
        embed.set_thumbnail(url="https://i.imgur.com/eUiRdY4.jpg")
        embed.add_field(name="英語(English)", value=translated_get_text, inline=False)
        embed.add_field(name="原文(Original)", value=translated_post_text, inline=True)
        embed.set_footer(text= "(" + msg.author.display_name + ")")
        await user.send(embed=embed)
        await msg.remove_reaction(EN_to_JP, user)

bot.run(discord_bot_token)
