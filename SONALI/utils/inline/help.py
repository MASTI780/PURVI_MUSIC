from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from SONALI import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text="• ʙᴀᴄᴋ •",
            callback_data=f"settingsback_helper",
        ),
       
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="H_B_1",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="H_B_2",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="H_B_3",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="H_B_4",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="H_B_5",
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text="H_B_6",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="H_B_7",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="H_B_8",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="H_B_9",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="H_B_10",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="H_B_11",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="H_B_12",
                    callback_data="help_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="H_B_13",
                    callback_data="help_callback hb13",
                ),
                InlineKeyboardButton(
                    text="H_B_14",
                    callback_data="help_callback hb14",
                ),
                InlineKeyboardButton(
                    text="H_B_15",
                    callback_data="help_callback hb15",
                ),
            ], 
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="• ʙᴀᴄᴋ •",
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data=f"close"),
            ],
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="• ᴏᴘᴇɴ ɪɴ ᴘʀɪᴠɪᴛᴇ •", url=f"https://t.me/{app.username}?start=help"
            ),
        ],
    ]
    return buttons
