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
        return

    if client.user.mentioned_in(message):
        await message.channel.send("契約書だよ。そこに名前を書きな。")
        await asyncio.sleep(1)
        await message.channel.send(f"(あなたは契約書に`{message.author.display_name}`と書き込んだ。)")

        name = message.author.display_name
        await asyncio.sleep(2)
        length = len(name)
        if length == 1:
            hiragana = [chr(code) for code in range(0x3041, 0x3097)]
            katakana = [chr(code) for code in range(0x30A1, 0x30FA)]
            kana = hiragana + katakana
            new_name = "".join(random.choices(kana, k=12))
            await message.channel.send(f"フン。`{name}`というのかい。短い名前だねぇ。")
            await asyncio.sleep(2)
            await message.channel.send(f"短い名前は好きじゃないんだ。")
            await asyncio.sleep(2)
            await message.channel.send(f"今からお前の名前は`{new_name}`だ。")
            await asyncio.sleep(2)
            await message.channel.send(f"いいかい、`{new_name}`だよ。分かったら返事をするんだ、`{new_name}`!!")
        
        else:
            await message.channel.send(f"フン。`{name}`というのかい。贅沢な名だねぇ。")
            name_length = random.randint(1,10)
            new_name_listed = random.choices(name.replace(" ",""), k=name_length)
            new_name = "".join(new_name_listed)
            await asyncio.sleep(4)
            await message.channel.send(f"今からお前の名前は`{new_name}`だ。"
            f"いいかい、`{new_name}`だよ。分かったら返事をするんだ、`{new_name}`!!")

        await message.author.edit(nick=new_name)

        await message.channel.send(f"(あなたのニックネームは`{new_name}`になった。)")

client.run("YOUR_TOKEN_HERE")
