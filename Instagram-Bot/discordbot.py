import discord
from discord.ext import commands, tasks
from credentials import *
from config import *
from instabot import *
from datetime import *

today_date = datetime.today().strftime('Date: %d-%m-%Y')
discord_client = discord.Client()
TOKEN = "discord_token"

def send_to_discord(total_time,start_time,end_time):
    global today
    today = today_date +\
            "\nFrom: " + start_time +  "  -  Until: "  + end_time +\
            "\nTime: " + total_time

    @discord_client.event
    async def on_ready():
        if execution == "test":
            overall = "discord_id_test"
            channel  = discord_client.get_channel(overall)
        else:
            channel  = discord_client.get_channel(clients[client.user_i][2])
        response = client.user_likes
        response = (str(response).replace(',', '').replace('(', '').replace(')', '').replace("'",""))
        if client.succesfull > 0:
            embedVar = discord.Embed(title = "RESULTS", description = today, color = 0x00ff00)
        else:
            embedVar = discord.Embed(title = "RESULTS", description = today, color = 0xea2e2e)
        embedVar.add_field(name  = "Likes", value = response,)
        embedVar.add_field(name  = "Followed", value = client.followed,)
        #embedVar.add_field(name  = "Unfollowed", value = client.unfollowed[i],)
        embedVar.add_field(name  = "Account stats", value = client.statistics,  inline = False)
        if execution == "test":
                embedVar.add_field(name  = "Account name", value = (clients[client.user_i][0]))
        await channel.send(embed = embedVar)

        with open("txt files/Results.txt") as Results:
            lines = []
            for line in Results:
                lines.append(line)
        if len(lines) >= number_of_accounts:
            overall = "discord_id"
            if execution == "test":
                overall = "discord_id_test"
            channel  = discord_client.get_channel(overall)
            with open("txt files/Results.txt", "rb") as file:
                await channel.send("Results", file=discord.File(file, "Results.txt"))
            open('txt files/Results.txt', 'w').close()

        await discord_client.close()


    discord_client.run(TOKEN)
