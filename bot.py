import discord
from os import getenv

client = discord.Client()

async def get_server_count():
    all=online=0
    for member in client.get_all_members():
        if member.bot:
            continue
        else:
            all += 1
            if member.status != discord.Status.offline:
                online += 1
    return all,online

async def update_count(count):
    all, online = count
    await client.edit_channel(channel=client.get_channel(getenv(TOTAL)),
                        name= "total ꞉ " + str(all))
    await client.edit_channel(channel=client.get_channel(getenv(ONLINE)),
                        name= "online ꞉ " + str(online))

@client.event
async def on_member_join(member):
    await update_count(await get_server_count())

@client.event
async def on_member_remove(member):
    await update_count(await get_server_count())

@client.event
async def on_member_update(before, after):
    await update_count(await get_server_count())

@client.event
async def on_ready():
    await update_count(await get_server_count())

client.run(TOKEN)
