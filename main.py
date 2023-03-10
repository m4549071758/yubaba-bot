import discord
import random
import asyncio

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f"{client.user.name}としてログインしました")
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return #自分自身のアクションは無視
    
    if client.user.mentioned_in(message): #メンションされたら
        old_name = message.author.display_name #ユーザー名の取得

        await message.channel.send("契約書だよ。そこに名前を書きな。")
        await asyncio.sleep(1)
        await message.channel.send(f"あなたは契約書に`{old_name}`と書き込んだ。")

        await asyncio.sleep(1)
        await message.channel.send(f"フン。`{old_name}`というのかい。贅沢な名だね。")

        name_length = random.randint(1,15) #名前の長さをrandintで決定 1~15文字
        new_name_listed = random.choices(name.replace(" ",""), k=name_length) #空白は潰し、randomでchoice
        new_name = "".join(new_name_listed) #リストから文字列へ

        await asyncio.sleep(3)
        await message.channel.send(f"今からお前の名前は`{new_name}`だ。"
        f"いいかい、`{new_name}`だよ。分かったら返事をするんだ、`{new_name}`!!")

        await message.author.edit(nick=new_name) #ニックネームを変更

        await message.channel.send(f"あなたのニックネームは`{new_name}`になった。")

client.run("YOUR_TOKEN_HERE")
