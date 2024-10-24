from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹ ʙᴀʙʏ-ᴍᴜsɪᴄ™ ˼ ʙᴏᴛ ✪
 
 ❍ • ʙsᴅᴋ ʀᴇᴘᴏ ʟᴇɢᴀ ◉‿◉ •
 
 ❍ • ᴘᴇʜʟᴇ istkhar ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ •
 
 ❍ • ᴄʜᴜᴘ ᴄʜᴜᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ •
 
 ❍ • ʀᴇᴘᴏs ᴛᴏ ɴᴀʜɪ ᴍɪʟᴇɢᴀ ʙᴇᴛᴀ ⊂◉‿◉ •
 
 ❍ • ᴀɢʀ ᴄʜᴀʜɪʏᴇ ᴛᴏ istkhar ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ •
 
 ❍ • 𝚃𝙴𝚁𝙸 𝙼𝙰𝙰 𝙺𝙸 𝙲𝙷𝚄𝚃  •
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("•ᴀᴅᴅ ᴍᴇ•", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("•sᴜᴘᴘᴏʀᴛ•", url="https://t.me/+9ZDy2Q5zdGgwMGNl"),
          InlineKeyboardButton("•ᴏᴡɴᴇʀ•", url="https://t.me/II_ISTKHAR_II"),
          ],
               [
                InlineKeyboardButton("•ᴜᴘᴅᴀᴛᴇs•", url="https://t.me/PURVI_SUPPORT"),

],
[
              InlineKeyboardButton("•ʙᴀɴᴀʟʟ•", url=f"https://t.me/SATYABANALL_ROBOT"),
              InlineKeyboardButton("︎•queen-ᴍᴜsɪᴄ•", url=f"https://t.me/Queenmusic_robot"),
              ],
              [
              InlineKeyboardButton("•SONALI MUSIC•", url=f"https://t.me/SonaliMusicRobot"),
InlineKeyboardButton("•ᴄʜᴀᴛ ʙᴏᴛ•", url=f"https://t.me/Purvi_Chat_Bot"),
],
[
InlineKeyboardButton("•sᴛʀɪɴɢ-ɢᴇɴ•", url=f"https://t.me/KING_STRING_SESSION_BOT"),
InlineKeyboardButton("•ᴍᴀɴᴀɢᴍᴇɴᴛ•", url=f"https://t.me/SATYA_HELP97_BOT"),
],
[
              InlineKeyboardButton("•sᴘᴀᴍ-ʙᴏᴛ•", url=f"https://t.me/AlPha_SPam_BOTS"),
              InlineKeyboardButton("•ᴀᴘɴᴀ-ᴍᴜsɪᴄ•︎", url=f"https://t.me/DCxMUSICxBOT"),
              ],
              [
              InlineKeyboardButton("•sᴛʀɪɴɢ ʜᴀᴄᴋ•", url=f"https://t.me/BABYSTRINGROBOT"),
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/62e2e9fc93cd51219264f.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/BABY-MUSIC/BABYTUNE/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[•ʙᴏᴛ-ᴏᴡɴᴇʀ•](https://t.me/II_ISTKHAR_II) | [•ᴜᴘᴅᴀᴛᴇs•](https://t.me/PURVI_SUPPORT)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
