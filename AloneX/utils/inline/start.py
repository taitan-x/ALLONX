from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(text="Cᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="Sᴏᴜʀᴄᴇ", user_id=OWNER),
        ],
        ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Aᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(text="Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL),
        [
               InlineKeyboardButton(text="Dᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER),
            )
        ],
    ]
    return buttons

close_key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]
            ]
        )
