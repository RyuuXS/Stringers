from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}

Selamat datang {}
Bot ini Bekerja Untuk Mendapatkan String Session Via Bot.
By @RYUUSHINNI
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/RYUUSHINNI")],
        [
            InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ ?", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/helpforRYUU")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot ini
/help - This Message
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - Membatalkan process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Pyrogram dan telethon string session by @RyuuString_bot

Group Support : [support](https://t.me/helpforRYUU)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @RYUUSHINNI
    """
