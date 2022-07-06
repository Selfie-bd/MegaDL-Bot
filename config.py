# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 1976680))
    API_HASH = os.environ.get("API_HASH", "9073255ce64a6072a59099803493f97d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5474681405:AAHbnU4Sx_ZtmuzgtGFMoXwLJXrpb-D20p8")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 1940030638))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001442783879"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)


class TEXT:
  ABOUT = """
🤖 **Name:** {bot_name}

📝 **Language:** [Python](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted On:** [Heroku](https://heroku.com)

🧑‍💻 **Developer:** [selfie-bd](https://t.me/selfiebd)

👥 **Support Group:** [Groupdc](https://t.me/groupdc)

📢 **Updates Channel:** [Groupdcbots](https://t.me/groupdcbots)
"""

  HELP_USER = """
This is **{bot_name}**

This Bot Can Download Files & Videos From Mega Links & Upload To Telegram. Just Send Any Mega.nz Link & See The Magic. You Can Also Add or Change Caption: Just Select An Uploaded File/ Video or Forward Me Any Telegram File & Then Write The Text You Want To Be Caption On The File As A Reply To That File & The Text You Wrote Will Be Attached As Caption 😁! 

**Made With ❤️ By @groupdcbots! 👑**
"""

  START_TEXT = """
👋🏻 **Hi** {user_mention},

I'm **{bot_name}**
I Can Download Files & Videos From Mega.nz Links & Upload To Telegram. Please Check Help To Learn More 😉!

**Maintained By: {bot_owner}**❤️!
"""
