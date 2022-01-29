import random

import telebot

TOKEN = '5161627286:AAFuMEU9GjOrWnIIwdZTaMZ5Y6k_kQnEtSA'

DICES = {
    1: 'CAACAgIAAxkBAAMdYes-TyIzK-sOSfaCvqIR7PhkG1gAAtzGAQABY4tGDLG1EhRKLhr_IwQ',
    2: 'CAACAgIAAxkBAAMeYes-X3sfZRiR-N4CSLbU3kXumsIAAt3GAQABY4tGDOtPKTvsIwJRIwQ',
    3: 'CAACAgIAAxkBAAMfYes-aYGnrAO_KGd5y4O1Vic6wgIAAt7GAQABY4tGDFRx_YWr-yC5IwQ',
    4: 'CAACAgIAAxkBAAMiYes-mGnfX1kOsOwHAAGmBvoWjf3yAALfxgEAAWOLRgwcRRMg1btjFyME',
    5: 'CAACAgIAAxkBAAMjYes-oVEP3rhyFFRtViiuWtfKJRwAAuDGAQABY4tGDEix8_rI_yapIwQ',
    6: 'CAACAgIAAxkBAAMkYes-qEmTabr-3fWMpH3plnss6gIAAuHGAQABY4tGDO-afM2nv7R6IwQ',
}


def roll_dice():
    dice_index = random.randint(1, 6)
    return DICES[dice_index]


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def on_start(message):
    bot.reply_to(message, 'Hi ✋, I can roll 🎲 for you.')


@bot.message_handler(commands=['roll_dice'])
def on_roll_dice(message):
    dice = roll_dice()
    bot.send_sticker(
        chat_id=message.chat.id,
        sticker=dice,
    )


bot.infinity_polling()