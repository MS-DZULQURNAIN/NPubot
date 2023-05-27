# Copyright (C) 2020  sandeep.n(π.$)
# button post makker for catuserbot thanks to uniborg for the base
# by @sandy1709 (@mrconfused)

import os
import re

from telethon import Button

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, tgbot
from AyiinXd.ayiin import ayiin_cmd, edit_delete, reply_id

# regex obtained from:
# https://github.com/PaulSonOfLars/tgbot/blob/master/tg_bot/modules/helper_funcs/string_handling.py#L23
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")


@ayiin_cmd(pattern="cbutton(?:\\s|$)([\\s\\S]*)")
async def _(event):
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(
            event, "**Teks apa yang harus saya gunakan di pesan button?**"
        )
    prev = 0
    note_data = ""
    buttons = []
    for match in BTN_URL_REGEX.finditer(markdown_note):
        n_escapes = 0
        to_check = match.start(1) - 1
        while to_check > 0 and markdown_note[to_check] == "\\":
            n_escapes += 1
            to_check -= 1
        if n_escapes % 2 == 0:
            buttons.append((match.group(2), match.group(3), bool(match.group(4))))
            note_data += markdown_note[prev : match.start(1)]
            prev = match.end(1)
        elif n_escapes % 2 == 1:
            note_data += markdown_note[prev:to_check]
            prev = match.start(1) - 1
        else:
            break
    else:
        note_data += markdown_note[prev:]
    message_text = note_data.strip() or None
    tl_ib_buttons = build_keyboard(buttons)
    tgbot_reply_message = None
    if reply_message and reply_message.media:
        tgbot_reply_message = await event.client.download_media(reply_message.media)
    if tl_ib_buttons == []:
        tl_ib_buttons = None
    await tgbot.send_message(
        entity=event.chat_id,
        message=message_text,
        parse_mode="html",
        file=tgbot_reply_message,
        link_preview=False,
        buttons=tl_ib_buttons,
    )
    await event.delete()
    if tgbot_reply_message:
        os.remove(tgbot_reply_message)


@ayiin_cmd(pattern="ibutton(?:\\s|$)([\\s\\S]*)")
async def _(event):
    reply_to_id = await reply_id(event)
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(
            event, "**Teks apa yang harus saya gunakan di pesan button?**"
        )
    catinput = "Inline buttons " + markdown_note
    AyiinUBOT = await tgbot.get_me()
    BOT_USERNAME = AyiinUBOT.username
    results = await event.client.inline_query(BOT_USERNAME, catinput)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


def build_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


CMD_HELP.update(
    {
        "button": """
𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏💎        

👤ᴘᴇʀɪɴᴛᴀʜ ʙᴜᴛᴛᴏɴ :         

ᴄᴍᴅ:         
  ├⋟ .cbutton <ᴛᴇxᴛ> [ɴᴀᴍᴀ]<buttonurl:ʟɪɴᴋ ᴇʟᴜ>
  └⋟ ʙᴜᴀᴛ ᴘᴇsᴀɴ ʙᴜᴛᴛᴏɴ ᴅɪ ᴄʜ (ᴛᴀᴍʙᴀʜᴋᴀɴ @DZuserbot sʙɢ ᴀᴅᴍɪɴ ᴅɪ ᴄʜ ʟᴜ)

ᴄᴍᴅ:         
  ├⋟ .ibutton <ᴛᴇxᴛ> [ɴᴀᴍᴀ]<buttonurl:ʟɪɴᴋ ᴇʟᴜ>
  └⋟ ʙᴜᴀᴛ ᴘᴇsᴀɴ ʙᴜᴛᴛᴏɴᴜʀʟ ᴅɪ ᴘᴇʀsᴏɴᴀʟ/ᴅɪᴄʜᴀᴛ

ɴᴏᴛᴇ :         
      ᴘᴀᴋᴇ ᴛɪᴛɪᴋ ᴅɪ ᴀᴡᴀʟ ᴘᴇʀɪɴᴛᴀʜ ʏᴀ ᴀɴJ🗿         
      ᴋʟᴏ ɢᴘʜᴍ ᴘᴄ ᴏᴡɴᴇʀ : @MSDZULQRNN
    """
    }
)
