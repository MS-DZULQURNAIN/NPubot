# Taken from
# https://github.com/AvinashReddy3108/PaperplaneRemix/blob/master/userbot/plugins/memes.py

# TG-UserBot - A modular Telegram UserBot script for Python.
# Copyright (C) 2019 Kandarp <https://github.com/kandnub>
#
# TG-UserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TG-UserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TG-UserBot.  If not, see <https://www.gnu.org/licenses/>.

import requests

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="shibe$")
async def shibe(event):
    xx = await edit_or_reply(event, "`otw nyari anj...`")
    response = requests.get("https://shibe.online/api/shibes").json()
    if not response:
        await event.edit("**kaga nemu Anjing.**")
        return
    await event.client.send_message(entity=event.chat_id, file=response[0])
    await xx.delete()


@ayiin_cmd(pattern="cat$")
async def cats(event):
    xx = await edit_or_reply(event, "`otw nyari kucing...`")
    response = requests.get("https://shibe.online/api/cats").json()
    if not response:
        await event.edit("**kaga nemu kucing.**")
        return
    await event.client.send_message(entity=event.chat_id, file=response[0])
    await xx.delete()


CMD_HELP.update(
    {
        "animals": """
𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏💎        

👤ᴘᴇʀɪɴᴛᴀʜ ᴀɴɪᴍᴀʟs:         

ᴄᴍᴅ:         
  ├⋟ .cat
  └⋟ ᴜɴᴛᴜᴋ Mᴇɴɢɪʀɪᴍ ɢᴀᴍʙᴀʀ ᴋᴜᴄɪɴɢ sᴇᴄᴀʀᴀ ʀᴀɴᴅᴏᴍ

ᴄᴍᴅ:         
  ├⋟ .shibe
  └⋟ ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ɢᴀᴍʙᴀʀ ʀᴀɴᴅᴏᴍ ᴅᴀʀɪ ᴀɴJɪɴɢ Jᴇɴɪs sʜɪʙᴀ

ɴᴏᴛᴇ :         
      ᴘᴀᴋᴇ ᴛɪᴛɪᴋ ᴅɪ ᴀᴡᴀʟ ᴘᴇʀɪɴᴛᴀʜ ʏᴀ ᴀɴJ🗿         
      ᴋʟᴏ ɢᴘʜᴍ ᴘᴄ ᴏᴡɴᴇʀ : @MSDZULQRNN
    """
    }
)
