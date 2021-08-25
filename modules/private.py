from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAELcSphJP9zfZgHUVwbgJr3ctDcwXj2rAACuAcAArHWCFUxMUPx-GRPIiAE")
    await message.reply_text(
        f"""**Hemlo 👋 
I am dark music Bot, Use me to play music in your groups Voice Chat.
Hosted On VPS, So no lag
✅Need Help /help 
Owner - @akshi_s_ashu**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Support", url="https://t.me/phoenix_music_suport}"
                    ),
                    InlineKeyboardButton(
                        "🔊 Updates", url="https://t.me/phoenix_music_new}"
                    ),
                    InlineKeyboardButton(
                        "🌍 Chat Group", url="https://t.me/red_vibe_s"
                    )
                ],
                [ 
                    InlineKeyboardButton(
                        "🤔Commands", url="https://t.me/OneUpdates/2"
                    )],
                [ 
                    InlineKeyboardButton(
                        "➕ Add To Your sexy group ➕", url="https://t.me/OneMusicRoBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**dark music online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 Chat Group", url="https://t.me/red_vibe_s")
                ]
            ]
        )
   )


