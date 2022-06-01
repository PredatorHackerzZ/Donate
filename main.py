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


START_TEXT = """Hᴇʏ! {}

☞ Vᴇʀʏ Hᴀᴘᴘʏ ᴛᴏ Kɴᴏᴡ Tʜᴀᴛ Yᴏᴜ ᴀʀᴇ Dᴏɴᴀᴛɪɴɢ Uꜱ.

Tʜᴀɴᴋꜱ Fᴏʀ Uꜱɪɴɢ [Oᴜʀ Bᴏᴛꜱ](https://t.me/+KYLCdC4XfcdmNGVl).

Mᴀᴅᴇ Wɪᴛʜ Lᴏᴠᴇ Fᴏʀ [Yᴏᴜ](tg://settings)"""

DONATE_BUTTONS = [
    InlineKeyboardButton(
        text='Dᴏɴᴀᴛᴇ 💳',
        callback_data='donateme'
    )
]

DONATE_TEXT = """Hᴇʏ! {}
Yᴏᴜ Cᴀɴ Dᴏɴᴀᴛᴇ Uꜱ Uꜱɪɴɢ UPI.

PayTm/PhonePe/GooglePay - `sk7062563@okhdfcbank`

Oʀ Cᴏɴᴛᴀcᴛ Uꜱ :- [ツAʙʜɪsʜᴇᴋ Kᴜᴍᴀʀ 🇮🇳](https://telegram.me/HelpLessBoi). """

BUTTON_TEXT = """ Click the Below Buttons To Donate Us. """

UPI_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" Back ", callback_data="back"),
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
async def donate(bot, update):
    await update.reply_text(
        text="Click the Following Button to Donate Us.",
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_message(filters.private & filters.command(["bots"]))
async def bots(bot, update):
    await update.reply_text(
        text="https://t.me/+t1ko_FOJxhFiOThl",
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_inline_query()
async def answerX(bot, update):

    answers = list()
    incoming = update.query

    if incoming == "":
        answer.append(InlineQueryResultArticle(title="This is My Donation Or Payment Bot", description="You Can Donate Us Using Inline.",
        input_message_content=InputTextMessageContent(message_text="Please Donate Us Any Amount You Like, to Support the Service."),
        reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton("", url="https://p.paytm.me/xCTH/n6kio0sk") ] ] ),
        thumb_url="https://telegra.ph/file/330bd070950b8ef775ca9.jpg") )
    else:
        answer.append(InlineQueryResultArticle(title="This is My Donation Or Payment Bot", description="You Can Donate Us Using Inline.",
        input_message_content=InputTextMessageContent(message_text="Please Donate Us Any Amount You Like, to Support the Service."),
        reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton("", url="https://p.paytm.me/xCTH/n6kio0sk") ] ] ),
        thumb_url="https://telegra.ph/file/330bd070950b8ef775ca9.jpg") )

    try:
        await event.answer(results=answers, cache_time=0)
    except QueryIdInvalid:
        pass

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
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

Bot.run()
