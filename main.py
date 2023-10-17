# Developed By : Abhishek Kumar (https://telegram.me/MrAbhi2k3) 

import os
import requests
from pyrogram import Client, filters
from requests.utils import requote_uri
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InputTextMessageContent
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)


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
Yᴏᴜ Cᴀɴ Dᴏɴᴀᴛᴇ Uꜱ Uꜱɪɴɢ UPI [India].

GooglePay - `sk7062563@okhdfcbank`

PayTM / PhonePe - `MrAbhi2k3@apl`

Oʀ Cᴏɴᴛᴀcᴛ Uꜱ :- [ツAʙʜɪsʜᴇᴋ Kᴜᴍᴀʀ 🇮🇳](https://telegram.me/HelpLessBoi). """

BUTTON_TEXT = """ Click the Below Buttons To Donate Us. """

UPI_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔙 Back ", callback_data="back"),
            InlineKeyboardButton("💰 PayPal ", url="https://paypal.me/AbhishekKumarIN47")
        ],
        [
            InlineKeyboardButton("🍵 Ko-Fi", url="https://ko-fi.com/Abhishekkumarin47"),
            InlineKeyboardButton("🔒 Close", callback_data="close")
        ]
    ]
)

PAY_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("₹ UPI ", callback_data="upidata"),
            InlineKeyboardButton("💰 PayPal ", url="https://paypal.me/AbhishekKumarIN47")
        ],
        [

            InlineKeyboardButton('🔒 Close', callback_data='close')

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


@Bot.on_message(filters.command(["donate"]))
async def donate_command(bot, update):
    await update.reply_text(
        text=BUTTON_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_message(filters.command(["bots"]))
async def bots_list(bot, update):
    await update.reply_text(
        text="https://t.me/+t1ko_FOJxhFiOThl",
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_inline_query()
async def answer(client, inline_query):
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="UPI ₹10",
                input_message_content=InputTextMessageContent(
                    "You Can Donate Us ₹10 for this Free Service"
                ),
                url="https://github.com/PredatorHackerzZ",
                description="Donate Us Some Amount as per your wish.",
                thumb_url="https://graph.org/file/92de75471809eb6645991.jpg",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Donate ₹10",
                            url="https://upayi.ml/sk7062563@okhdfcbank/10"
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="UPI ₹25",
                input_message_content=InputTextMessageContent(
                    "You Can Donate Us ₹25 for this Free Service"
                ),
                url="https://github.com/PredatorHackerzZ",
                description="Donate Us Some Amount as per your wish.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Donate ₹25",
                            url="https://upayi.ml/sk7062563@okhdfcbank/25"
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="UPI ₹50",
                input_message_content=InputTextMessageContent(
                    "You Can Donate Us ₹50 for this Free Service"
                ),
                url="https://github.com/PredatorHackerzZ",
                description="Donate Us Some Amount as per your wish.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Donate ₹50",
                            url="https://upayi.ml/sk7062563@okhdfcbank/50"
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="UPI ₹100",
                input_message_content=InputTextMessageContent(
                    "You Can Donate Us ₹100 for this Free Service"
                ),
                url="https://github.com/PredatorHackerzZ",
                description="Donate Us Some Amount as per your wish.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Donate ₹100",
                            url="https://upayi.ml/sk7062563@okhdfcbank/100"
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="UPI ₹500",
                input_message_content=InputTextMessageContent(
                    "You Can Donate Us ₹500 for this Free Service"
                ),
                url="https://github.com/PredatorHackerzZ",
                description="Donate Us Some Amount as per your wish.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Donate ₹500",
                            url="https://upayi.ml/sk7062563@okhdfcbank/500"
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="PayPal $",
                input_message_content=InputTextMessageContent(
                    "This is My PayPal Account For International Donation Or Payment."
                ),
                url="https://github.com/PredatorHackerzZ",
                description="Donate Us Some Amount as per your wish, If you want",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            " PayPal 💳",
                            url="https://paypal.me/AbhishekKumarIN47"
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="BTC 💰",
                input_message_content=InputTextMessageContent(
                    "You Can Donate Us BTC too for this Free Service. My BTC Account Coming Soon."
                ),
                url="https://github.com/PredatorHackerzZ",
                description="Donate Us 1 BTC if You Are Rich.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Created By Owner",
                            url="https://t.me/OwnYourBotz"
                        )]
                    ]
                )
            )
        ],
        cache_time=1
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
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

Bot.run()
