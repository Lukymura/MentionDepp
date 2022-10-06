#Copyright ©️ 2022 Lukymura. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [Depp Mention bot by Lukymura] (https://github.com/Lukymura/MentionDepp)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/PingAllBot-teletips/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.types import Message
import os
import asyncio
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait

teletips=Client(
    "MentionDepp",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

chatQueue = []

stopProcess = False

@teletips.on_message(filters.command(["ping","all"]))
async def everyone(client, message):
  global stopProcess
  try: 
    try:
      sender = await teletips.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      if len(chatQueue) > 5:
        await message.reply("⛔️ | ɢᴜᴇ ᴜᴅᴀʜ ɴɢᴇʀᴊᴀɪɴ sᴀᴍᴘᴇ ᴍᴀᴋsɪᴍᴀʟ 5 ᴏʙʀᴏʟᴀɴ ɢᴜᴇ,ʟᴏ ᴄᴏʙᴀ ᴋᴀᴘᴀɴ ᴋᴀᴘᴀɴ ᴅᴀʜʜ.")
      else:  
        if message.chat.id in chatQueue:
          await message.reply("🚫 | ᴜᴅᴀʜ ᴀᴅᴀ ᴘʀᴏsᴇs ʏᴀɴɢ sᴇᴅᴀɴɢ ʙᴇʀʟᴀɴɢsᴜɴɢ ᴅᴀʟᴀᴍ ᴏʙʀᴏʟᴀɴ ɪɴɪ, ᴛᴏʟᴏɴɢ /stop ʙᴜᴀᴛ ᴍᴜʟᴀɪ ʏᴀɴɢ ʙᴀʀᴜ.")
        else:  
          chatQueue.append(message.chat.id)
          if len(message.command) > 1:
            inputText = message.command[1]
          elif len(message.command) == 1:
            inputText = ""    
          membersList = []
          async for member in teletips.get_chat_members(message.chat.id):
            if member.user.is_bot == True:
              pass
            elif member.user.is_deleted == True:
              pass
            else:
              membersList.append(member.user)
          i = 0
          lenMembersList = len(membersList)
          if stopProcess: stopProcess = False
          while len(membersList) > 0 and not stopProcess :
            j = 0
            text1 = f"{inputText}\n\n"
            try:    
              while j < 10:
                user = membersList.pop(0)
                if user.username == None:
                  text1 += f"{user.mention} "
                  j+=1
                else:
                  text1 += f"@{user.username} "
                  j+=1
              try:     
                await teletips.send_message(message.chat.id, text1)
              except Exception:
                pass  
              await asyncio.sleep(10) 
              i+=10
            except IndexError:
              try:
                await teletips.send_message(message.chat.id, text1)  
              except Exception:
                pass  
              i = i+j
          if i == lenMembersList:    
            await message.reply(f"✅ | ᴜᴅᴀʜ ɢᴜᴇ ᴍᴇɴᴛɪᴏɴ ʏᴀ **ᴛᴏᴛᴀʟ {i} ᴍᴇᴍʙᴇʀ**.\n❌ | ʙᴏᴛ sᴀᴍᴀ ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs ɢᴀ ɢᴜᴇ ᴍᴇɴᴛɪᴏɴ ɴɢᴀᴘᴀɪɴ ᴊᴜɢᴀ ᴄᴀᴘᴇ ᴄᴀᴘᴇ.") 
          else:
            await message.reply(f"✅ | ᴜᴅᴀʜ ɢᴜᴇ ᴍᴇɴᴛɪᴏɴ ʏᴀ **{i} ᴍᴇᴍʙᴇʀ.**\n❌ | ʙᴏᴛ sᴀᴍᴀ ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs ɢᴀ ɢᴜᴇ ᴍᴇɴᴛɪᴏɴ ɴɢᴀᴘᴀɪɴ ᴊᴜɢᴀ ᴄᴀᴘᴇ ᴄᴀᴘᴇ.")    
          chatQueue.remove(message.chat.id)
    else:
      await message.reply("👮🏻 | ᴛᴏʟᴏʟʟ, **ᴄᴜᴍᴀ ᴀᴅᴍɪɴ** ʏᴀɴɢ ʙɪsᴀ ᴘᴀᴋᴇ ɢᴜᴇ ʙᴇɢᴏᴏ")  
  except FloodWait as e:
    await asyncio.sleep(e.value) 

@teletips.on_message(filters.command(["remove","clean"]))
async def remove(client, message):
  global stopProcess
  try: 
    try:
      sender = await teletips.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      bot = await teletips.get_chat_member(message.chat.id, "self")
      if bot.status == ChatMemberStatus.MEMBER:
        await message.reply("🕹 | ʟᴏ ʙᴇʟᴜᴍ ᴊᴀᴅɪ ᴀᴅᴍɪɴ ʙᴇɢᴏ ʙᴜᴀᴛ ʜᴀᴘᴜs ᴛᴏʟᴏʟ ᴀᴍᴀᴛ sɪʜ.")  
      else:  
        if len(chatQueue) > 5 :
          await message.reply("⛔️ | ɢᴜᴇ ᴜᴅᴀʜ ɴɢᴇʀᴊᴀɪɴ sᴀᴍᴘᴇ ᴍᴀᴋsɪᴍᴀʟ 5 ᴏʙʀᴏʟᴀɴ ɢᴜᴇ,ʟᴏ ᴄᴏʙᴀ ᴋᴀᴘᴀɴ ᴋᴀᴘᴀɴ ᴅᴀʜʜ.")
        else:  
          if message.chat.id in chatQueue:
            await message.reply("🚫 | ᴜᴅᴀʜ ᴀᴅᴀ ᴘʀᴏsᴇs ʏᴀɴɢ sᴇᴅᴀɴɢ ʙᴇʀʟᴀɴɢsᴜɴɢ ᴅᴀʟᴀᴍ ᴏʙʀᴏʟᴀɴ ɪɴɪ, ᴛᴏʟᴏɴɢ /stop ʙᴜᴀᴛ ᴍᴜʟᴀɪ ʏᴀɴɢ ʙᴀʀᴜ.")
          else:  
            chatQueue.append(message.chat.id)  
            deletedList = []
            async for member in teletips.get_chat_members(message.chat.id):
              if member.user.is_deleted == True:
                deletedList.append(member.user)
              else:
                pass
            lenDeletedList = len(deletedList)  
            if lenDeletedList == 0:
              await message.reply("👻 | ᴋᴀɢᴀ ᴀᴅᴀ ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs ᴍᴇᴍᴇᴋ.")
              chatQueue.remove(message.chat.id)
            else:
              k = 0
              processTime = lenDeletedList*10
              temp = await teletips.send_message(message.chat.id, f"🚨 | Total {lenDeletedList} ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs ᴜᴅᴀʜ ɢᴜᴇ ᴅᴇᴛᴇᴋsɪ.\n⏳ | ᴇsᴛɪᴍᴀsɪ ᴡᴀᴋᴛᴜ: {processTime} ᴅᴇᴛɪᴋ ᴅᴀʀɪ sᴇᴋᴀʀᴀɴɢ.")
              if stopProcess: stopProcess = False
              while len(deletedList) > 0 and not stopProcess:   
                deletedAccount = deletedList.pop(0)
                try:
                  await teletips.ban_chat_member(message.chat.id, deletedAccount.id)
                except Exception:
                  pass  
                k+=1
                await asyncio.sleep(10)
              if k == lenDeletedList:  
                await message.reply(f"✅ | ᴅᴀʜ ɢᴜᴇ ʙᴀɴᴛᴀɪ ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs ᴅɪ ɢᴄ ʟᴏ ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ʙɪʟᴀɴɢ ᴍᴀᴋᴀsɪ sᴀᴍᴀ ᴅᴇᴘᴘ ʏᴀɴᴠ ᴘᴀʟɪɴɢ ɢᴀɴᴛᴇɴɢ.")  
                await temp.delete()
              else:
                await message.reply(f"✅ | ᴅᴀʜ ɢᴜᴇ ʙᴀɴᴛᴀɪ {k} ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs ᴅɪ ɢᴄ ʟᴏ ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ʙɪʟᴀɴɢ ᴍᴀᴋᴀsɪ sᴀᴍᴀ ᴅᴇᴘᴘ ʏᴀɴɢ ᴘᴀʟɪɴɢ ɢᴀɴᴛᴇɴɢ.")  
                await temp.delete()  
              chatQueue.remove(message.chat.id)
    else:
      await message.reply("👮🏻 | ᴛᴏʟᴏʟ, **ᴄᴜᴍᴀ ᴀᴅᴍɪɴ** ʏᴀɴɢ ʙɪsᴀ ᴘᴀᴋᴇ ɢᴜᴇ ʙᴇɢᴏ.")  
  except FloodWait as e:
    await asyncio.sleep(e.value)                               
        
@teletips.on_message(filters.command(["stop","cancel"]))
async def stop(client, message):
  global stopProcess
  try:
    try:
      sender = await teletips.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      if not message.chat.id in chatQueue:
        await message.reply("ʟᴏ ᴍᴀᴜ ʙᴇʀʜᴇɴᴛɪɪɴ ᴀᴘᴀᴀɴ ᴍᴇᴍᴇᴋ ᴏʀᴀɴɢ ᴋᴀɢᴀ ᴛᴀɢ ᴀʟʟ.")
      else:
        stopProcess = True
        await message.reply("ᴅᴀʀɪ ᴛᴀᴅɪ ᴅᴏɴɢ ɢᴜᴇ ᴅᴀʜ ᴄᴀᴘᴇ.")
    else:
      await message.reply("ᴛᴏʟᴏʟ, **ᴄᴜᴍᴀ ᴀᴅᴍɪɴ** ʏᴀɴɢ ʙɪsᴀ ᴘᴀᴋᴇ ɢᴜᴇ ʙᴇɢᴏ.")
  except FloodWait as e:
    await asyncio.sleep(e.value)

@teletips.on_message(filters.command(["admins","staff"]))
async def admins(client, message):
  try: 
    adminList = []
    ownerList = []
    async for admin in teletips.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
      if admin.privileges.is_anonymous == False:
        if admin.user.is_bot == True:
          pass
        elif admin.status == ChatMemberStatus.OWNER:
          ownerList.append(admin.user)
        else:  
          adminList.append(admin.user)
      else:
        pass   
    lenAdminList= len(ownerList) + len(adminList)  
    text2 = f"**GROUP STAFF - {message.chat.title}**\n\n"
    try:
      owner = ownerList[0]
      if owner.username == None:
        text2 += f"👑 ᴏᴡɴᴇʀ\n└ {owner.mention}\n\n👮🏻 ᴀᴅᴍɪɴs\n"
      else:
        text2 += f"👑 ᴏᴡɴᴇʀ\n└ @{owner.username}\n\n👮🏻 ᴀᴅᴍɪɴs\n"
    except:
      text2 += f"👑 ᴏᴡɴᴇʀ\n└ <i>Hidden</i>\n\n👮🏻 ᴀᴅᴍɪɴs\n"
    if len(adminList) == 0:
      text2 += "└ <i>Admins are hidden</i>"  
      await teletips.send_message(message.chat.id, text2)   
    else:  
      while len(adminList) > 1:
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"├ {admin.mention}\n"
        else:
          text2 += f"├ @{admin.username}\n"    
      else:    
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"└ {admin.mention}\n\n"
        else:
          text2 += f"└ @{admin.username}\n\n"
      text2 += f"**ᴊᴜᴍʟᴀʜ ᴛᴏᴛᴀʟ ᴀᴅᴍɪɴ**: {lenAdminList}\n❌ | ʙᴏᴛ sᴀᴍᴀ ᴀᴅᴋɪɴ ᴛᴇʀsᴇᴍʙᴜɴʏɪ ᴅɪᴛᴏʟᴀᴋ."  
      await teletips.send_message(message.chat.id, text2)           
  except FloodWait as e:
    await asyncio.sleep(e.value)       

@teletips.on_message(filters.command("bots"))
async def bots(client, message):  
  try:    
    botList = []
    async for bot in teletips.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
      botList.append(bot.user)
    lenBotList = len(botList) 
    text3  = f"**ʙᴏᴛ ʟɪsᴛ - {message.chat.title}**\n\n🤖 ʙᴏᴛ\n"
    while len(botList) > 1:
      bot = botList.pop(0)
      text3 += f"├ @{bot.username}\n"    
    else:    
      bot = botList.pop(0)
      text3 += f"└ @{bot.username}\n\n"
      text3 += f"**ᴊᴜᴍʟᴀʜ ᴛᴏᴛᴀʟ ʙᴏᴛ**: {lenBotList}"  
      await teletips.send_message(message.chat.id, text3)
  except FloodWait as e:
    await asyncio.sleep(e.value)

@teletips.on_message(filters.command("start") & filters.private)
async def start(client, message):
  text = f'''
ʜᴀʟᴏ ᴀɴᴀᴋ ᴋᴏɴᴛᴏʟ ʏᴀɪᴛᴜ {message.from_user.mention},
ᴋᴇɴᴀʟɪɴ ɴᴀᴀ ɢᴜᴇ **MentionDepp**. ɢᴜᴇ ʙɪsᴀ ʙᴀɴᴛᴜɪɴ ʟᴏ ʙᴜᴀᴛ ɴɢᴇᴛᴀɢ ᴀɴᴀᴋ ᴀɴᴀᴋ ɴɢᴇɴᴛᴏᴅ sᴜᴘᴀʏᴀ ᴍᴜɴᴄᴜʟ.

ʟᴏ ᴋᴀɢᴀ ᴊᴏɪɴ ᴄʜ ɢᴜᴇ, ɢᴜᴇ sᴜᴍᴘᴀʜɪɴ ᴍᴇᴍᴇᴋ sᴀᴍᴀ ᴋᴏɴᴛᴏʟ ʟᴏ ʙᴜsᴜᴋ[ᴄʜᴀɴɴᴇʟ](http://t.me/kyyomasaa)

ᴋᴀʟᴏ ʟᴏ ʙᴇɢᴏ ᴋᴇᴛɪᴋ /help ʙɪᴀʀ ʟᴏ ᴛᴀᴜ.
'''
  await teletips.send_message(message.chat.id, text, disable_web_page_preview=True)


@teletips.on_message(filters.command("help"))
async def help(client, message):
  text = '''
ɴᴀʜʜ ʟᴏ ɪᴋᴜᴛɪɴ ʏᴀɴɢ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ʙᴛᴡ ɢᴜᴇ ᴍᴀᴜ ᴘᴀᴋᴇ ʙᴀʜᴀsᴀ ᴇɴɢɢʀᴇs ʙɪᴀʀ ᴋᴀʏᴀᴋ ᴏʀᴀɴɢ ᴘʀᴏғᴇsɪᴏɴᴀʟ ᴀɴᴊᴀʏʏ

**Commands**:
- /ping "input": <i>Mention all members.</i>
- /remove: <i>Remove all deleted accounts.</i>
- /admins: <i>Mention all admins.</i>
- /bots: <i>Get the full bot list.</i>
- /stop: <i>Stop an on going process.</i>

'''
  await teletips.send_message(message.chat.id, text, disable_web_page_preview=True)

print("sᴀᴀᴛɴʏᴀ ᴋᴇʀᴊᴀ!")  
teletips.run()
 
#Copyright ©️ 2021 Lukymura. All Rights Reserved 
