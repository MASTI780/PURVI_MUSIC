import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

OWNERS = "7531575025"
from SONALI import app
from SONALI.utils.database import add_served_chat, get_assistant

# Multiple accounts ke string sessions
STRING_SESSIONS = [
    "your_string_session_1"BQCZzqEANcXRMpPHezT-8J1LnVgBl-IafUjsfSiiSoU6ktSlDchcdhtjPj_9JvDpAD-YSdg3qumlehE-zlU_OrHVrOcYauBIMX_Rutje-NwfAXe5fZV9mDST8bAf2wsLckYbJUqV9sXArRy_O4A1lymIYIi-xaB08dYhBK9YWUcd6acWU_Cv2vTKxCr23wkUrahpj8tlobiMSkpTpDiK4MCDscPVgaPE97ocs427KKWdtMz2oIwei67gm5RqrqVVgBsymOod9APSVoG07bukxVrP9ynNtF4DDmENArWi7oc4c6xeyXmS4hM336XxKRf7C5HR8sg0AwbvQxPVGPEcvyvtblXwSAAAAAGCXgzzAA",
    "your_string_session_2"BQD7IGgAZF_fpNe93DWjyl9kORo7ooBE7LGkxr8E3VzZjJEQlKF22FdlNEM7fwFz-fA4YJWZGyBnTLDpJCb5Doay8Bz1x30N9pH1_J35qaiVjMVZ43uXXb1zHYM-QpPnHdsfpc8CHeevVSkvdsnyuVr-IFCRmL4Wf4qGc4ZQzDL4ldDknjPzkrGDpEXlzVuTFSqR6hxW1Q9ODgZte5ejlgkYK_0mpuble4c6OcSyvoXasEmlRX4hwYZn6BBHX8lIO2ZMOv_Z1kgDP2OnEHL0BT4RlTqrUzqSTCDApuIQ_tnGeZMDFuQRVgofdlRqTdjWr7jySwyacOYKlkiWSTcOlogAAipwVAAAAAGF4OEZAA",
    "your_string_session_3"BQCZzqEAwD3nCMUVUMhYydxmRLiA5MroDtuCb6caD_Ho4wRpaHOGV5utuAADBYo9E1bDLTvZ9OVrTHYupQ3ciT9NWn18HQlg-BVmC7hZZxkNWFRErKw3HnelfjTq1qVOTvQv2xg9H-L_oiZdo6DINXZ24B-t_UQIFBhzk_Udl9Ylrpv96fhwKdScx-l8zX_S5MoY1wlC-OS7UAcDoAAvPhzgDEQot3wLGIvbErnjMsinYbNfvOHF_wLWFS2W4KJgfGVRCZBtezSBY3y-C_vuXiaMZpjFm2u_3jZ-4bM7Pqzwzu3wnJnbV5Q77aiWsIeoZtRRlC9g0kXYOaUeXiwc6160VrIACwAAAAHJuXfnAA",
    "your_string_session_4"BQFUvHQAii4GwqkpuCzUOAxvGPQOIaRzfyK9cLWkUe9M_K6e1e072m_0yxWtS6CyW90fdX6M_ruPQQkyB_beLD2gHumODmCqEFI4BpiOAqqeHLEBX3Vs_71wYOUV8zHGLrAGHpUkSJyRQZf55E7JXHP7F5OH969CFNLaJfVpZXDLbK-hJWPyHKr_ZvhVx0YUrdiymH2s28j5uTqhvHstOf7K1_g47e52VN90CScF35NLFWm1fx_slZ8KmHDMYMDIL6uT5M9n8J633PuF9uujvGI9tFFOXPlyfyIGuqN7dYtbsKM-S49wMUgIPbRAv0I4NXo_CCY6Mvf2BBECnqhjk9cZcjqUDQAAAAHU2h2CAA",
    "your_string_session_5"BQCZzqEAibMQRwDzEUelCnX0LVELKwqzBgGDAIetRl9TqqOi8ME-X3YU3Pt4NYUh1RRHtR1p4h1vD0t1dg7EBpvduO-vYZzufC7sPsHh_MPMUG6i6S90Agpppdh_10wizrR4RjC_9KWj6J8JrnUXKuNuDM8cXeWTw2mpmsHgQix78iNCiBRL9FlHJRT-us42Spip_akRnzhEOtelU3U3qPcyJeejTbdWotKk5y4yKfZaNEOGQE6GxO-8wrra2SOUdU_8NxZIBaxBUW3naC5dS2FwOAFizANaWdpO4OiUZ-SFdVj_JzjpogkwGuhXCLiZ-ja2EXlSFG-k6oh6DlfEm7A-SibE3AAAAAFk3eywAA",
]

@app.on_message(filters.command("gadd") & filters.user(int(OWNERS)))
async def add_allbot(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply(
            "**❍ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ. ᴘʟᴇᴀsᴇ ᴜsᴇ ʟɪᴋᴇ » `/gadd @BOT_USERNAME`**"
        )
        return

    bot_username = command_parts[1]
    
    done = 0
    failed = 0
    all_clients = []

    # Har string session ke liye client initialize karna
    for session in STRING_SESSIONS:
        client_instance = Client(session)
        await client_instance.start()
        all_clients.append(client_instance)

    try:
        bot = await app.get_users(bot_username)
        app_id = bot.id
        notification_message = await message.reply("❍ **ᴀᴅᴅɪɴɢ ɢɪᴠᴇɴ ʙᴏᴛ ɪɴ ᴀʟʟ ᴄʜᴀᴛs!**")

        for userbot in all_clients:
            await userbot.send_message(bot_username, f"/start")
            async for dialog in userbot.get_dialogs():
                if dialog.chat.id == -1002011723196:
                    continue
                try:
                    await userbot.add_chat_members(dialog.chat.id, app_id)
                    done += 1
                except Exception as e:
                    failed += 1

                await notification_message.edit(
                    f"**❍ ᴀᴅᴅɪɴɢ {bot_username}**\n\n"
                    f"**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✔**\n"
                    f"**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ✘**\n\n"
                    f"**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
                )
                await asyncio.sleep(3)  # Rate limit ke liye sleep

        await notification_message.edit(
            f"**❍ {bot_username} ʙᴏᴛ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🎉**\n\n"
            f"**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n"
            f"**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ✘**\n\n"
            f"**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
    finally:
        # Sabhi clients ko stop karna
        for client_instance in all_clients:
            await client_instance.stop()
