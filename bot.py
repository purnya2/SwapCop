# bot.py
import aiohttp, wget
import asyncio, aiofiles
import os, random, re
import urllib.request
import beat
import discord
from dotenv import load_dotenv
import exorzhumor
import ameno
import tts
import earthboundify
import suavekubo

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()


def Find(string):
	url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
	return url

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} has connected to Discord!\n'
        f'{guild.name}(id: {guild.id})'
        )
        

@client.event
async def on_message(message):
    global prevurl
    if message.author == client.user:
        return
    att = message.attachments
   
    message_in = str(message.content).lower()
    message_list = message_in.split()
    print(message_list)

    if message.attachments:
        prevurl = message.attachments[0].url

    findmessage = ""
    if len(Find(message_in))>0:
        findmessage = Find(message_in)[0]
        if findmessage.endswith(".png") or findmessage.endswith(".jpg") or findmessage.endswith(".jpeg"):
            prevurl = findmessage
            print(prevurl)


    blockedList = []
    if len(message_in)>0:
        if message_in[0][0]=='-' and (message.author.id in blockedList):
            await message.channel.send("shut the fuck up <@"+str(message.author.id)+">, get NaeNaed")
            message_in=""
        else:
            if message_in == "i'm stuff" or message_in == "im stuff":
                await message.channel.send("https://i.imgur.com/tCh0zLi.jpg")
                print("sent!")
        #
            if message_in == "-gondola":
                await message.channel.send(file=discord.File("gondola\\"+random.choice(os.listdir("gondola"))))
                print("sent!")

            if message_in == "-suavekubo" or message_in == "-kubo":
                temp = suavekubo.init('c')
                print("downloading?")
                wget.download(temp[0])
                print("downloaded!")
                await message.channel.send(file=discord.File(temp[1]))
                os.remove(temp[1])
                print("sent!")

            if message_list[0] == "-4chan" and len(message_list)>1:
                print("mhhh")
                if len(message_list)>0:
                    print("mhhh")
                    temp = suavekubo.init(message_list[1])
                    print("downloading?")
                    wget.download(temp[0])
                    print("downloaded!")
                    await message.channel.send(file=discord.File(temp[1]))
                    os.remove(temp[1])

                print("sent!")

            if message_in == "-boomerhumor" or message_in == "-exorzhumor":
                await message.channel.send(exorzhumor.randomExorz())
                print("sent!")

            if message_list[0] == "-swapfuck" and len(message_list)>0:
                if len(message_list)>1 and message.attachments:
                    if int(message_list[1])<0:
                        await message.channel.send("why the fuck would you use a negative number")
                    else:
                        await message.channel.send("---")
                        att = message.attachments
                        inputorder="1111"
                        if len(message_list)>2:
                            if beat.ordercheck(message_list[2]):
                                inputorder = message_list[2]
                                print("order -- " + inputorder + " -- detected")
                        
                        if att[0].filename.endswith(".mp3"):
                            await message.channel.send("mp3 file detected")
                            await message.channel.send("---")
                            #urllib.request.urlretrieve(url,'\downloads')
                            async with aiohttp.ClientSession() as session:
                                url = att[0].url
                                async with session.get(url) as resp:
                                    if resp.status == 200:
                                        f = await aiofiles.open('downloads\source.mp3', mode='wb')
                                        await f.write(await resp.read())
                                        await f.close()
                            await message.channel.send("gonna take a longass time, please wait") 
                            beat.swapthisshit('downloads\source.mp3',"out.mp3",int(message_list[1]),inputorder)
                            
                            await message.channel.send(file=discord.File('out.mp3'))
                        else:
                            await message.channel.send("error, the file is not mp3, fucking dumbass")
                            await message.channel.send("---")
                else:
                    await message.channel.send("Usage: ```-swapfuck <lenght in ms of the chunks to swap> *<order of the beats>``` \n you must attach an mp3 file only, over 8 megabytes files are not supported (commands marked with * are not obligatory)\n\ndescription: This command takes in input an mp3 song, and it divides it in various milliseconds, and then it swaps the various pieces each other according to the order that is inputted\n the order has to look like \"1234\" and must not have numbers that are not 1 2 3 or 4\n examples:\n    ```-swapfuck 2000```\n    ```-swapfuck 500 1242```")
            if message_list[0] == "-dorime":
                if len(prevurl)>0:
                    await message.channel.send("---")
                    if prevurl.lower().endswith(".png") or prevurl.lower().endswith(".jpg") or prevurl.lower().endswith(".jpeg"):
                        await message.channel.send("image file detected")
                        await message.channel.send("---")
                        async with aiohttp.ClientSession() as session:
                            url = prevurl
                            async with session.get(url) as resp:
                                if resp.status == 200:
                                    f = await aiofiles.open('dorime\images\dummy.png', mode='wb')
                                    await f.write(await resp.read())
                                    await f.close()
                        await message.channel.send("gonna take a longass time, please wait") 
                        ameno.start()
                        print(os.getcwd())
                        await message.channel.send(file=discord.File('dorime\outwithaudio.mp4'))
                    else:
                        await message.channel.send("error, the file extension is not valid, fucking dumbass")
                        await message.channel.send("---")
                else:
                    await message.channel.send("Usage: just write -dorime, and have the image sent with it fuckass")
            
            if message_list[0] == "-tts":
                if len(message_list)>1:
                    ttsstr = ""
                    for i in range(1,len(message_list)):
                        ttsstr = ttsstr + " " + message_list[i]
                    tts.init(ttsstr)
                    await message.channel.send(file=discord.File('tts\out.wav'))
                else:
                    await message.channel.send("Usage: -tts <string>\n if you want to know how to sing, please check out <https://www.youtube.com/watch?v=nu_Pp3ptxTY> \n tonal table: <http://gyazo.com/fe2d44c8c3817e612e94adcc168b99e5.png>")
            

            if message_list[0] == "-earthboundify":
                if len(prevurl)>0:
                    await message.channel.send("---")
                    
                    
                    if prevurl.lower().endswith(".png") or prevurl.lower().endswith(".jpg") or prevurl.lower().endswith(".jpeg"):
                        await message.channel.send("image file detected")
                        await message.channel.send("---")
                        async with aiohttp.ClientSession() as session:
                            url = prevurl
                            async with session.get(url) as resp:
                                if resp.status == 200:
                                    f = await aiofiles.open('earthboundify\images\dummy.png', mode='wb')
                                    await f.write(await resp.read())
                                    await f.close()
                        await message.channel.send("gonna take a longass time, please wait")
                        if len(message_list)>1:
                            text = ""
                            for i in range(len(message_list)-1):
                                text += str(message_list[i+1]) + " "
                            earthboundify.start(text)
                        else:
                            earthboundify.start()
                        await message.channel.send(file=discord.File('earthboundify\outwithaudio.mp4'))
            
            if message_list[0] == "-close":
                if message.author.id == 492310805639987210:
                    await message.channel.send("oh :(")
                    await message.channel.send("shutting down...")
                    exit()
                else:
                    await message.channel.send("https://i.ytimg.com/vi/_Xlyiru8Lls/mqdefault.jpg")

client.run(TOKEN)
