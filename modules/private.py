from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIp9mBtwBBZGywWEmV-WC8gcMArjusuAAKMAgACTp1xV6m-mtC1YTfoHgQ")
    await message.reply_text(
        f"""**Hemlo 👋 
I am One Music Bot, Use me to play music in your groups Voice Chat.
Hosted On VPS, So no lag
✅Need Help /help 
Owner - @SherShahxD**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Support", url="https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "🔊 Updates", url="https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                        "🌍 Chat Group", url="https://t.me/friends_ka_adda"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/OneMusicRoBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**One Music Bot Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/LaylaList")
                ]
            ]
        )
   )


