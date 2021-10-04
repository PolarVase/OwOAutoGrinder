from discord.ext import commands
import discord
from os.path import isfile
import json
from requests import get
import time
from pypresence import Presence


bot = commands.Bot(">", self_bot = True)

dcToken = "NDcxNjMxNzczMzk1MzIwODM0.YUx1-A.IVTClU9Ip8kQpq1LbfR3otTf2dY" # YOUR DISCORD TOKEN HERE

version = "3"

channelToSendInID = ""
inOn = False

owoWait = 10
huntWait = 13
sellAllWait = 110
prayWait = 303
dailyWait = 86460

start_time_owo = 0
start_time_hunt = 0
start_time_daily = 0
start_time_pray = 0
start_time_sellall = 0

elapsed_time_owo = 0
elapsed_time_hunt = 0
elapsed_time_daily = 0
elapsed_time_pray = 0
elapsed_time_sellall = 0

firstTime = True

latestVersionPastebin = "https://pastebin.com/raw/MZ3PG9KB" 


def versionChecker(version):
    latestVersion = get("https://pastebin.com/raw/MZ3PG9KB").text

    latestVersion = int(latestVersion)

    if (version == latestVersion):
        print(f"Version is Up To Date!\nYour program version: {version}\nLatest Version: {latestVersion}")
    if (version < latestVersion):
        print(f"Version is OUTDATED! Please Update The Program!\nYour program version: {version}\nLatest Version: {latestVersion}")
    if (version > latestVersion):
        print(f"You are using Beta Version Of The Program! Please Report Any bugs!\nYour program version: {version}\nLatest Version: {latestVersion}")



@bot.event
async def on_ready():
    print("OwOAutoGrinder is ON! Prefix is >")
    print("\nPlease! For the love of the god! Don't use it in dms. I am not putting safety shit here.")
    print("I will never do it. Use it as intended. This program isn't Dumb-Proof.")

    versionChecker(int(version))




RPC = Presence('890305556357734412', pipe=0)
RPC.connect()

@bot.command()
async def rpc(ctx, option):
    await ctx.message.delete()

    option = str(option)

    if (option == "start"):
        print(RPC.update(state = "You Can Get It For Free!", 
        details = "Grinding OwO | https://github.com/xakeplusplus/OwOAutoGrinder", 
        small_image = "smallimg", small_text = "Brought to you by xakeplusplus, Unseens", 
        large_image = "largeimg", large_text = "Automatic OwO Grinder", 
        buttons = [{"label": "Download", "url": "https://github.com/xakeplusplus/OwOAutoGrinder"}]))
    if (option == "stop"):
        RPC.clear()
    
    
@bot.command()
async def setchannel(ctx):
    await ctx.message.delete()

    global channelToSendInID

    channelToSendInID = ctx.channel.id
    
    f = open("owogrinder.json", "w")
    channelToSendInID = int(channelToSendInID)
    
    tempPyJson = {
        "token": dcToken,
        "channelId": channelToSendInID
    }

    json.dump(tempPyJson, f)
    f.close()

    print(f"Channel Set To: {channelToSendInID}")

    
@bot.command()
async def start(ctx):
    await ctx.message.delete()

    if (isfile("owogrinder.json") == True):
        f = open("owogrinder.json", "r")
        
        loaded = json.load(f)

        try:
            if (loaded["channelId"] != None):
                global channelId
                global isOn

                tempChannelIdVar = loaded["channelId"]
                tempChannelIdVar = int(tempChannelIdVar)

                channelId = tempChannelIdVar
                channelId = int(channelId)
                
                isOn = True
                await grinder()
        except Exception as e:
            print("Error Occured: " + e)

    elif (channelToSendInID == None):
        print("You didn't specify the channel to start the grinder in! Type >setchannel")
    else:
        isOn = True

        await grinder()


breakerVar = False
async def grinder():
    while (isOn == True):
        channelToSendIn = bot.get_channel(channelToSendInID)

        global start_time_owo
        global start_time_hunt
        global start_time_daily
        global start_time_pray
        global start_time_sellall

        global elapsed_time_owo
        global elapsed_time_hunt
        global elapsed_time_daily
        global elapsed_time_pray
        global elapsed_time_sellall

        global firstTime

        if (firstTime):
            time.sleep(2.937)
            await channelToSendIn.send("owo hunt")
            time.sleep(1.830)
            await channelToSendIn.send("owo")
            time.sleep(2.341)
            await channelToSendIn.send("owo daily")
            time.sleep(1.542)
            await channelToSendIn.send("owo pray")
            time.sleep(6.31)
            await channelToSendIn.send("owo sell all")
            time.sleep(3.238)
            
            firstTime = False

            start_time_owo = time.time()
            start_time_hunt = time.time()
            start_time_daily = time.time()
            start_time_pray = time.time()
            start_time_sellall = time.time()

        if (not firstTime):
            elapsed_time_hunt = time.time() - start_time_owo
            elapsed_time_hunt = time.time() - start_time_hunt
            elapsed_time_daily = time.time() - start_time_daily
            elapsed_time_pray = time.time() - start_time_pray
            elapsed_time_sellall = time.time() - start_time_sellall

            if (elapsed_time_hunt > huntWait):
                time.sleep(2)
                await channelToSendIn.send("owo hunt")
                start_time_hunt = time.time()
            if (elapsed_time_owo > owoWait):
                time.sleep(2)
                await channelToSendIn.send("owo")
                start_time_owo = time.time()
            if (elapsed_time_daily > dailyWait):
                time.sleep(2)
                await channelToSendIn.send("owo daily")
                start_time_daily = time.time()
            if (elapsed_time_pray > prayWait):
                time.sleep(2)
                await channelToSendIn.send("owo pray")
                start_time_pray = time.time()
            if (elapsed_time_sellall > sellAllWait):
                time.sleep(2)
                await channelToSendIn.send("owo sell all")
                start_time_sellall = time.time()

        @bot.event
        async def on_message(message: discord.Message):
            if message.guild is None and message.author.bot is True:
                if (str(message.author) == "OwO#8456"):
                    raise KeyboardInterrupt
                
            await bot.process_commands(message)

bot.run(dcToken, bot=False)
