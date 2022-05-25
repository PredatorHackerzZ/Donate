# Developed By : Abhishek Kumar (https://telegram.me/TheTeleRoid) 

import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import *


Bot = Client(
    "Donate",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TEXT = """Hey! {}
☞ Very Happy to Know that You are Donating Us.

Thanks For Using [Our Bots](https://t.me/+KYLCdC4XfcdmNGVl).

Made with love For [You](tg://settings)"""

DONATE_BUTTONS = [
    InlineKeyboardButton(text='Donate 💸', callback_data='donateme'
    )
]

DONATE_TEXT = """Hey! {}
You Can Donate Us Using UPI. 

PayTm/PhonePe/GooglePay - `sk7062563@okhdfcbank`

Or Contact Us :- [Abhishek Kumar](https://telegram.me/HelpLessBoi). """

BUTTON_TEXT = """ Click the Below Buttons To Donate Us. """

UPI_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" Back", callback_data="back"),
            InlineKeyboardButton(" PayPal ", url="https://paypal.me/AbhishekKumarIN47")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

PAY_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" UPI ", callback_data="upidata"),
            InlineKeyboardButton(" PayPal ", url="https://paypal.me/AbhishekKumarIN47")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([DONATE_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["donate"]))
async def filter(bot, update):
    await update.reply_text(
        text="Click the Following Button to Donate Us.",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="UPI", callback_data="upidata"),
                 InlineKeyboardButton(text="PayPal", url="https://paypal.me/AbhishekKumarIN47")]
            ],
            [
                [InlineKeyboardButton(text="😥 Close", callback_data="close")]
            ]
        ),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "donateme":
        await update.message.edit_text(
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "upidata":
        await update.message.edit_text(
            text=DONATE_TEXT.format(update.from_user.mention),
            reply_markup=UPI_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "back":
        await update.message.edit_text(
            text=BUTTON_TEXT,
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

Bot.run()
