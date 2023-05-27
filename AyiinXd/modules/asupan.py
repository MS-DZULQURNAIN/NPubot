# 🍀 © @tofik_dn
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
# ⚠️ Do not remove credits

from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice

from AyiinXd import BLACKLIST_CHAT
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, edit_or_reply


@ayiin_cmd(pattern="asupan$")
async def _(event):
    xx = await edit_or_reply(event, "`Sabar anj...`")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@tedeasupancache", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(asupannya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Kaga ada anj, tobat napa**")


@ayiin_cmd(pattern="moan$")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(
            event, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    xx = await edit_or_reply(event, "`Sabar anj...`")
    try:
        moannya = [
            moan
            async for desah in event.client.iter_messages(
                "@cachemoan", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(moannya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Kaga ada anj, tobat napa**")


CMD_HELP.update(
    {
        "asupan": """
𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏💎        

👤ᴘᴇʀɪɴᴛᴀʜ ᴀsᴜᴘᴀɴ:         

ᴄᴍᴅ:         
  ├⋟ .asupan
  └⋟ ʙᴜᴀᴛ ɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ᴀsᴜᴘᴀɴ sᴇᴄᴀʀᴀ ʀᴀɴᴅᴏᴍ

ᴄᴍᴅ:         
  ├⋟ .moan
  └⋟ ʙᴜᴀᴛ ɴɢɪʀɪᴍ ᴀsᴜᴘᴀɴ ᴍᴏᴀɴ/ᴅᴇsᴀʜ sᴇᴄᴀʀᴀ ʀᴀɴᴅᴏᴍ

ɴᴏᴛᴇ :         
      ᴘᴀᴋᴇ ᴛɪᴛɪᴋ ᴅɪ ᴀᴡᴀʟ ᴘᴇʀɪɴᴛᴀʜ ʏᴀ ᴀɴJ🗿         
      ᴋʟᴏ ɢᴘʜᴍ ᴘᴄ ᴏᴡɴᴇʀ : @MSDZULQRNN
    """
    }
)
