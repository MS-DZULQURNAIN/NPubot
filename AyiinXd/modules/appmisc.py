# imported from github.com/ravana69/PornHub to userbot by @heyworld
# please don't nuke my credits 😓
import asyncio
import logging
import os
import time
from datetime import datetime
from urllib.parse import quote

import bs4
import requests
from justwatch import JustWatch
from telethon import *
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.types import (
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]


logger = logging.getLogger(__name__)
thumb_image_path = TEMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"
name = "Profile Photos"


@ayiin_cmd(pattern="remove(?: |$)(.*)", allow_sudo=False)
async def _(event):
    if event.fwd_from:
        return
    if event.is_private:
        return False
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not (chat.admin_rights or chat.creator):
            await eor(event, get_string("no_admn"))
            return False
    p = 0
    b = 0
    c = 0
    d = 0
    e = []
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    xx = await eor(event, get_string("com_2"))
    async for i in event.client.iter_participants(event.chat_id):
        p += 1
        #
        # Note that it's "reversed". You must set to ``True`` the permissions
        # you want to REMOVE, and leave as ``None`` those you want to KEEP.
        rights = ChatBannedRights(until_date=None, view_messages=True)
        if isinstance(i.status, UserStatusEmpty):
            y += 1
            if "y" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await eod(xx, get_string("hk_admn")
                              )
                    e.append(str(e))
                    break
                c += 1
        if isinstance(i.status, UserStatusLastMonth):
            m += 1
            if "m" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await eod(
                        xx,
                        "**Saya memerlukan hak admin untuk melakukan tindakan ini!**",
                    )
                    e.append(str(e))
                    break
                c += 1
        if isinstance(i.status, UserStatusLastWeek):
            w += 1
            if "w" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await eod(xx, get_string("hk_admn")
                              )
                    e.append(str(e))
                    break
                c += 1
        if isinstance(i.status, UserStatusOffline):
            o += 1
            if "o" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await eod(xx, get_string("hk_admn")
                                      )
                    e.append(str(e))
                    break
                c += 1
        if isinstance(i.status, UserStatusOnline):
            q += 1
            if "q" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await eor(event, get_string("hk_admn")
                              )
                    e.append(str(e))
                    break
                c += 1
        if isinstance(i.status, UserStatusRecently):
            r += 1
            if "r" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await eod(xx, get_string("hk_admn")
                              )
                    e.append(str(e))
                    break
                c += 1
        if i.bot:
            b += 1
            if "b" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await eod(xx, get_string("hk_admn")
                              )
                    e.append(str(e))
                    break
                c += 1
        elif i.deleted:
            d += 1
            if "d" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await eod(xx, get_string("hk_admn")
                              )
                    e.append(str(e))
                else:
                    c += 1
        elif i.status is None:
            n += 1
    if input_str:
        required_string = """Kicked {} / {} users
Deleted Accounts: {}
UserStatusEmpty: {}
UserStatusLastMonth: {}
UserStatusLastWeek: {}
UserStatusOffline: {}
UserStatusOnline: {}
UserStatusRecently: {}
Bots: {}
None: {}"""
        await xx.edit(required_string.format(c, p, d, y, m, w, o, q, r, b, n))
        await asyncio.sleep(5)
    await event.edit(
        """Total= {} users
Number Of Deleted Accounts= {}
Status: Empty= {}
      : Last Month= {}
      : Last Week= {}
      : Offline= {}
      : Online= {}
      : Recently= {}
Number Of Bots= {}
Unidentified= {}""".format(
            p, d, y, m, w, o, q, r, b, n
        )
    )


async def ban_user(chat_id, i, rights):
    try:
        await client(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)


@ayiin_cmd(pattern="rnupload(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    thumb = thumb_image_path if os.path.exists(thumb_image_path) else None
    xx = await eor(event, get_string("com_1"))
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        end = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        to_download_directory = TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await event.client.download_media(
            reply_message,
            downloaded_file_name,
        )
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            time.time()
            await event.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=True,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await xx.edit(get_string("appmis_2").format(ms_one, ms_two)
                          )
        else:
            await eod(xx, get_string("error_3").format(input_str))
    else:
        await eod(xx, "Syntax // .rnupload filename.extension <reply ke media>")


@ayiin_cmd(pattern="grab(?: |$)(.*)")
async def potocmd(event):
    id = "".join(event.raw_text.split(maxsplit=2)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    xx = await eor(event, get_string("com_1"))
    if user:
        photos = await event.client.get_profile_photos(user.sender)
    else:
        photos = await event.client.get_profile_photos(chat)
    if id.strip() == "":
        try:
            await event.client.send_file(event.chat_id, photos)
        except a:
            photo = await event.client.download_profile_photo(chat)
            await event.client.send_file(event.chat_id, photo)
    else:
        try:
            id = int(id)
            if id <= 0:
                return await eod(xx, get_string("failed1")
                                 )
        except BaseException:
            return await eod(xx, "**Lmao**")
        if int(id) <= (len(photos)):
            send_photos = await event.client.download_media(photos[id - 1])
            await event.client.send_file(event.chat_id, send_photos)
            await xx.delete()
        else:
            return await eod(xx, get_string("failed2"))


@ayiin_cmd(pattern="res(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        return await eod(event, "**Mohon Balas Ke Link.**", time=20)
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        return await eod(event, "**Mohon Balas Ke Link.**", time=20)
    chat = "@CheckRestrictionsBot"
    xx = await eor(event, get_string("com_1"))
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=894227130)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            await event.client.forward_messages(chat, reply_message)
            response = await response
        if response.text.startswith(""):
            await eod(event, get_string("error_2"))
        else:
            await xx.delete()
            await event.client.send_message(event.chat_id, response.message)
            await event.client.delete_message(chat, event.chat_id, response.message)


def get_stream_data(query):
    stream_data = {}

    # Compatibility for Current Userge Users
    try:
        country = Config.WATCH_COUNTRY
    except Exception:
        country = "IN"

    # Cooking Data
    just_watch = JustWatch(country=country)
    results = just_watch.search_for_item(query=query)
    movie = results["items"][0]
    stream_data["title"] = movie["title"]
    stream_data["movie_thumb"] = (
        "https://images.justwatch.com"
        + movie["poster"].replace("{profile}", "")
        + "s592"
    )
    stream_data["release_year"] = movie["original_release_year"]
    try:
        print(movie["cinema_release_date"])
        stream_data["release_date"] = movie["cinema_release_date"]
    except KeyError:
        try:
            stream_data["release_date"] = movie["localized_release_date"]
        except KeyError:
            stream_data["release_date"] = None

    stream_data["type"] = movie["object_type"]

    available_streams = {}
    for provider in movie["offers"]:
        provider_ = get_provider(provider["urls"]["standard_web"])
        available_streams[provider_] = provider["urls"]["standard_web"]

    stream_data["providers"] = available_streams

    scoring = {}
    for scorer in movie["scoring"]:
        if scorer["provider_type"] == "tmdb:score":
            scoring["tmdb"] = scorer["value"]

        if scorer["provider_type"] == "imdb:score":
            scoring["imdb"] = scorer["value"]
    stream_data["score"] = scoring
    return stream_data


# Helper Functions


def pretty(name):
    if name == "play":
        name = "Google Play Movies"
    return name[0].upper() + name[1:]


def get_provider(url):
    url = url.replace("https://www.", "")
    url = url.replace("https://", "")
    url = url.replace("http://www.", "")
    url = url.replace("http://", "")
    url = url.split(".")[0]
    return url


@ayiin_cmd(pattern="watch(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    xx = await eor(event, get_string("com_1"))
    streams = get_stream_data(query)
    title = streams["title"]
    thumb_link = streams["movie_thumb"]
    release_year = streams["release_year"]
    release_date = streams["release_date"]
    scores = streams["score"]
    try:
        imdb_score = scores["imdb"]
    except KeyError:
        imdb_score = None
    try:
        tmdb_score = scores["tmdb"]
    except KeyError:
        tmdb_score = None
    stream_providers = streams["providers"]
    if release_date is None:
        release_date = release_year
    output_ = f"**Movie:**\n`{title}`\n**Release Date:**\n`{release_date}`"
    if imdb_score:
        output_ = output_ + f"\n**IMDB: **{imdb_score}"
    if tmdb_score:
        output_ = output_ + f"\n**TMDB: **{tmdb_score}"
    output_ = output_ + "\n\n**Available on:**\n"
    for provider, link in stream_providers.items():
        if "sonyliv" in link:
            link = link.replace(" ", "%20")
        output_ += f"[{pretty(provider)}]({link})\n"
    await event.client.send_file(
        event.chat_id,
        caption=output_,
        file=thumb_link,
        force_document=False,
        allow_cache=False,
        silent=True,
    )
    await xx.delete()


# credits:
# Ported from Saitama Bot.
# By :- @PhycoNinja13b
# Modified by :- @kirito6969,@deleteduser420


@ayiin_cmd(pattern="weeb(?: |$)(.*)")
async def weebify(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit(get_string("appmis_3"))
        return
    string = " ".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)


boldfont = [
    "𝗮",
    "𝗯",
    "𝗰",
    "𝗱",
    "𝗲",
    "𝗳",
    "𝗴",
    "𝗵",
    "𝗶",
    "𝗷",
    "𝗸",
    "𝗹",
    "𝗺",
    "𝗻",
    "𝗼",
    "𝗽",
    "𝗾",
    "𝗿",
    "𝘀",
    "𝘁",
    "𝘂",
    "𝘃",
    "𝘄",
    "𝘅",
    "𝘆",
    "𝘇",
]


@ayiin_cmd(pattern="bold(?: |$)(.*)")
async def thicc(bolded):
    args = bolded.pattern_match.group(1)
    if not args:
        get = await bolded.get_reply_message()
        args = get.text
    if not args:
        return await eod(bolded, get_string("appmis_4"))
    xx = await eor(bolded, get_string("com_1"))
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            boldcharacter = boldfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, boldcharacter)
    await xx.edit(string)


medievalbold = [
    "𝖆",
    "𝖇",
    "𝖈",
    "𝖉",
    "𝖊",
    "𝖋",
    "𝖌",
    "𝖍",
    "𝖎",
    "𝖏",
    "𝖐",
    "𝖑",
    "𝖒",
    "𝖓",
    "𝖔",
    "𝖕",
    "𝖖",
    "𝖗",
    "𝖘",
    "𝖙",
    "𝖚",
    "𝖛",
    "𝖜",
    "𝖝",
    "𝖞",
    "𝖟",
]


@ayiin_cmd(pattern="medibold(?: |$)(.*)")
async def mediv(medievalx):
    args = medievalx.pattern_match.group(1)
    if not args:
        get = await medievalx.get_reply_message()
        args = get.text
    if not args:
        return await eod(
            medievalx, get_string("appmis_5")
        )
    xx = await eor(medievalx, get_string("com_1"))
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            medievalcharacter = medievalbold[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, medievalcharacter)
    await xx.edit(string)


doublestruckt = [
    "𝕒",
    "𝕓",
    "𝕔",
    "𝕕",
    "𝕖",
    "𝕗",
    "𝕘",
    "𝕙",
    "𝕚",
    "𝕛",
    "𝕜",
    "𝕝",
    "𝕞",
    "𝕟",
    "𝕠",
    "𝕡",
    "𝕢",
    "𝕣",
    "𝕤",
    "𝕥",
    "𝕦",
    "𝕧",
    "𝕨",
    "𝕩",
    "𝕪",
    "𝕫",
]


@ayiin_cmd(pattern="doublestruck(?: |$)(.*)")
async def doublex(doublestrucktx):
    args = doublestrucktx.pattern_match.group(1)
    if not args:
        get = await doublestrucktx.get_reply_message()
        args = get.text
    if not args:
        return await eod(
            doublestrucktx, get_string("appmis_6")
        )
    xx = await eor(doublestrucktx, get_string("com_1"))
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            strucktcharacter = doublestruckt[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, strucktcharacter)
    await xx.edit(string)


cursiveboldx = [
    "𝓪",
    "𝓫",
    "𝓬",
    "𝓭",
    "𝓮",
    "𝓯",
    "𝓰",
    "𝓱",
    "𝓲",
    "𝓳",
    "𝓴",
    "𝓵",
    "𝓶",
    "𝓷",
    "𝓸",
    "𝓹",
    "𝓺",
    "𝓻",
    "𝓼",
    "𝓽",
    "𝓾",
    "𝓿",
    "𝔀",
    "𝔁",
    "𝔂",
    "𝔃",
]


@ayiin_cmd(pattern="curbold(?: |$)(.*)")
async def cursive2(cursivebolded):
    args = cursivebolded.pattern_match.group(1)
    if not args:
        get = await cursivebolded.get_reply_message()
        args = get.text
    if not args:
        await eod(
            cursivebolded, get_string("appmis_7")
        )
        return
    xx = await eor(cursivebolded, get_string("com_1"))
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursiveboldcharacter = cursiveboldx[normiefont.index(
                normiecharacter)]
            string = string.replace(normiecharacter, cursiveboldcharacter)
    await xx.edit(string)


medival2 = [
    "𝔞",
    "𝔟",
    "𝔠",
    "𝔡",
    "𝔢",
    "𝔣",
    "𝔤",
    "𝔥",
    "𝔦",
    "𝔧",
    "𝔨",
    "𝔩",
    "𝔪",
    "𝔫",
    "𝔬",
    "𝔭",
    "𝔮",
    "𝔯",
    "𝔰",
    "𝔱",
    "𝔲",
    "𝔳",
    "𝔴",
    "𝔵",
    "𝔶",
    "𝔷",
]


@ayiin_cmd(pattern="medi(?: |$)(.*)")
async def medival22(medivallite):
    args = medivallite.pattern_match.group(1)
    if not args:
        get = await medivallite.get_reply_message()
        args = get.text
    if not args:
        await eod(medivallite, get_string("appmis_8"))
        return
    xx = await eor(medivallite, get_string("com_1"))
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            medivalxxcharacter = medival2[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, medivalxxcharacter)
    await xx.edit(string)


cursive = [
    "𝒶",
    "𝒷",
    "𝒸",
    "𝒹",
    "𝑒",
    "𝒻",
    "𝑔",
    "𝒽",
    "𝒾",
    "𝒿",
    "𝓀",
    "𝓁",
    "𝓂",
    "𝓃",
    "𝑜",
    "𝓅",
    "𝓆",
    "𝓇",
    "𝓈",
    "𝓉",
    "𝓊",
    "𝓋",
    "𝓌",
    "𝓍",
    "𝓎",
    "𝓏",
]


@ayiin_cmd(pattern="cur(?: |$)(.*)")
async def xcursive(cursivelite):
    args = cursivelite.pattern_match.group(1)
    if not args:
        get = await cursivelite.get_reply_message()
        args = get.text
    if not args:
        await eod(cursivelite, get_string("appmis_9"))
        return
    xx = await eor(cursivelite, get_string("com_1"))
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursivecharacter = cursive[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, cursivecharacter)
    await xx.edit(string)


CMD_HELP.update(
    {
        "watch": """
𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏💎        

👤ᴘᴇʀɪɴᴛᴀʜ ᴡᴀᴛᴄʜ :         

ᴄᴍᴅ:         
    ├⋟ .watch <ɴᴀᴍᴀ ᴍᴏᴠɪᴇ/ᴛᴠ>
    └⋟ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴅᴇᴛᴀɪʟ ᴛᴇɴᴛᴀɴɢ ғɪʟᴍ

ɴᴏᴛᴇ :         
      ᴘᴀᴋᴇ ᴛɪᴛɪᴋ ᴅɪ ᴀᴡᴀʟ ᴘᴇʀɪɴᴛᴀʜ ʏᴀ ᴀɴJ🗿         
      ᴋʟᴏ ɢᴘʜᴍ ᴘᴄ ᴏᴡɴᴇʀ : @MSDZULQRNN
    """
    }
)

CMD_HELP.update(
    {
        "glitch": """
𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏💎        

👤ᴘᴇʀɪɴᴛᴀʜ ɢʟɪᴛᴄʜ :         

ᴄᴍᴅ:         
    ├⋟ .glitch <ʀᴇᴘʟʏ ғᴏᴛᴏ>
    └⋟ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢɪғ ɢʟɪᴛᴄʜ ᴅᴀʀɪ ғᴏᴛᴏ

ɴᴏᴛᴇ :         
      ᴘᴀᴋᴇ ᴛɪᴛɪᴋ ᴅɪ ᴀᴡᴀʟ ᴘᴇʀɪɴᴛᴀʜ ʏᴀ ᴀɴJ🗿         
      ᴋʟᴏ ɢᴘʜᴍ ᴘᴄ ᴏᴡɴᴇʀ : @MSDZULQRNN
    """
    }
)

CMD_HELP.update(
    {
        "grab": """
𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏💎        

👤ᴘᴇʀɪɴᴛᴀʜ ɢʀᴀʙ :         

ᴄᴍᴅ:         
    ├⋟ .grab 
    └⋟ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ғᴏᴛᴏ ᴘʀᴏғɪʟ ᴅᴀʀɪ ᴘᴇɴɢɢᴜɴᴀ

ɴᴏᴛᴇ :         
      ᴘᴀᴋᴇ ᴛɪᴛɪᴋ ᴅɪ ᴀᴡᴀʟ ᴘᴇʀɪɴᴛᴀʜ ʏᴀ ᴀɴJ🗿         
      ᴋʟᴏ ɢᴘʜᴍ ᴘᴄ ᴏᴡɴᴇʀ : @MSDZULQRNN
    """
    }
)

CMD_HELP.update(
    {
        "bannedall": """
𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏💎        

👤ᴘᴇʀɪɴᴛᴀʜ ʙᴀɴɴᴇᴅᴀʟʟ :         

ᴄᴍᴅ:         
  ├⋟ .remove
  └⋟ ᴜɴᴛᴜᴋ Mᴇɴɢᴀɴᴀʟɪsᴀ ᴜsᴇʀ ᴅᴀʀɪ ɢʀᴜᴘ sᴇᴄᴀʀᴀ sᴘᴇsɪғɪᴋ

ᴄᴍᴅ:         
  ├⋟ .remove <ᴋᴇʏᴡᴏʀᴅ>
  ├⋟ ᴋᴇʏᴡᴏʀᴅ : d
  ├⋟ ʙᴜᴀᴛ ᴋɪᴄᴋ ᴜsᴇʀ ᴅᴀʀɪ ɢᴄ sᴇᴄᴀʀᴀ sᴘᴇsɪғɪᴋ
  ├⋟ ᴋᴇʏᴡᴏʀᴅ : y
  ├⋟ ʙᴜᴀᴛ ɴɢᴇʙᴀɴ ᴀᴋᴜɴ ʏɢ ᴛᴇʀᴀᴋʜɪʀ ᴅɪʟɪʜᴀᴛ sᴇᴛᴀʜᴜɴ ʏɢ ʟᴀʟᴜ
  ├⋟ ᴋᴇʏᴡᴏʀᴅ : m
  ├⋟ ʙᴜᴀᴛ ɴɢᴇʙᴀɴ ᴀᴋᴜɴ ʏɢ ᴛᴇʀᴀᴋʜɪʀ ᴅɪʟɪʜᴀᴛ sᴇʙᴜʟᴀɴ ʏɢ ʟᴀʟᴜ
  ├⋟ ᴋᴇʏᴡᴏʀᴅ : o
  ├⋟ ʙᴜᴀᴛ ɴɢᴇʙᴀɴ ᴀᴋᴜɴ ʏɢ sᴇᴅᴀɴɢ ᴏғғʟɪɴᴇ
  ├⋟ ᴋᴇʏᴡᴏʀᴅ : q
  ├⋟ ʙᴜᴀᴛ ɴɢᴇʙᴀɴ ᴀᴋᴜɴ ʏɢ sᴇᴅᴀɴɢ ᴏɴʟɪɴᴇ
  ├⋟ ᴋᴇʏᴡᴏʀᴅ : r
  ├⋟ ʙᴜᴀᴛ ɴɢᴇʙᴀɴ ᴀᴋᴜɴ ʏɢ ᴛᴇʀᴀᴋʜɪʀ ᴅɪʟɪʜᴀᴛ
  ├⋟ ᴋᴇʏᴡᴏʀᴅ : b
  ├⋟ ʙᴜᴀᴛ ɴɢᴇʙᴀɴ ʙᴏᴛ ʏɢ ᴀᴅᴀ ᴅɪ ɢᴄ     
  ├⋟ ᴋᴇʏᴡᴏʀᴅ : n
  └⋟ ʙᴜᴀᴛ ɴɢᴇʙᴀɴ ᴀᴋᴜɴ ʏɢ Lᴀsᴛ Sᴇᴇɴ A Lᴏɴɢ Tɪᴍᴇ Aɢᴏ

ɴᴏᴛᴇ :         
      ᴘᴀᴋᴇ ᴛɪᴛɪᴋ ᴅɪ ᴀᴡᴀʟ ᴘᴇʀɪɴᴛᴀʜ ʏᴀ ᴀɴJ🗿         
      ᴋʟᴏ ɢᴘʜᴍ ᴘᴄ ᴏᴡɴᴇʀ : @MSDZULQRNN
    """
    }
)

CMD_HELP.update(
    {
        "rnupload": """
𝘿𝙕-𝙐𝙎𝙀𝙍𝘽𝙊𝙏💎        

👤ᴘᴇʀɪɴᴛᴀʜ ʀɴᴜᴘʟᴏᴀᴅ :         

ᴄᴍᴅ:         
    ├⋟ .rnupload 
    └⋟ ʙᴜᴀᴛ ʀᴇɴᴀᴍᴇ ᴅᴀɴ ᴜᴘʟᴏᴀᴅ, ʀᴇᴘʟʏ ᴋᴇ ᴍᴇᴅɪᴀ & ᴋᴇᴛɪᴋ .rnupload xʏᴢ.Jᴘɢ

ɴᴏᴛᴇ :         
      ᴘᴀᴋᴇ ᴛɪᴛɪᴋ ᴅɪ ᴀᴡᴀʟ ᴘᴇʀɪɴᴛᴀʜ ʏᴀ ᴀɴJ🗿         
      ᴋʟᴏ ɢᴘʜᴍ ᴘᴄ ᴏᴡɴᴇʀ : @MSDZULQRNN
    """
    }
)

