from telegram.ext import Updater, CommandHandler

import rates
import config
    
# Start
def handler_start(update, context):
    update.message.reply_text('Узнать курс - /rates \nПомощь - /help')

# Help
def handler_help(update, context):
    update.message.reply_text('*Доступные команды*:\nУзнать курс - /rates \nПомощь - /help\nСписок монет - /list\nМожно смотреть курс всех монет сразу, или одной.\n\nКурс указывается в USDT. Информацию бот берет через [API Binance](https://binance-docs.github.io/apidocs/spot/en/#symbol-price-ticker). Обновление данных каждые 5 секунд.\n\n[Исходный код](https://github.com/onilyxe/CryptoCurrency)' ,parse_mode="Markdown", disable_web_page_preview = True)

# List
def handler_list(update, context):
    update.message.reply_text('*Доступные криптовалюты*:\n/rates - курс всех монет\n/BTC\n/ETH\n/ATOM\n/ADA\n/FTM\n/SOL\n/XRP\n/XTZ\n/OMG\n/LUNA\n/MANA\n/LINK\n/KSM\n\nХочешь добавить монету?\nПиши: @onilyxe',parse_mode="Markdown")


# Rates
def handler_rates(update, context):
    data = rates.get_rates_cached()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.8s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")
    
# BTC
def handler_BTC(update, context):
    data = rates.get_rates_cachedBTC()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.8s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")

# ETH
def handler_ETH(update, context):
    data = rates.get_rates_cachedETH()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.7s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")

# ATOM
def handler_ATOM(update, context):
    data = rates.get_rates_cachedATOM()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.6s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")

# ADA
def handler_ADA(update, context):
    data = rates.get_rates_cachedADA()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.6s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")
    
# FTM
def handler_FTM(update, context):
    data = rates.get_rates_cachedFTM()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.6s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")
    
# SOL
def handler_SOL(update, context):
    data = rates.get_rates_cachedSOL()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.5s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")
    
# XRP
def handler_XRP(update, context):
    data = rates.get_rates_cachedXRP()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.6s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")
    
# XTZ
def handler_XTZ(update, context):
    data = rates.get_rates_cachedXTZ()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.5s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")
    
# OMG
def handler_OMG(update, context):
    data = rates.get_rates_cachedOMG()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.5s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")
    
# LUNA
def handler_LUNA(update, context):
    data = rates.get_rates_cachedLUNA()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.6s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")
    
# MANA
def handler_MANA(update, context):
    data = rates.get_rates_cachedMANA()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.6s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")
    
# LINK
def handler_LINK(update, context):
    data = rates.get_rates_cachedLINK()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.5s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")
    
# KSM
def handler_KSM(update, context):
    data = rates.get_rates_cachedKSM()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.7s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")
    
# DOGE
def handler_DOGE(update, context):
    data = rates.get_rates_cachedDOGE()
    output = ""
    for currency, rate in data.items():
        if rate != None:
            output += ("*%s*: _%.7s_ \n" % (currency, rate))
    update.message.reply_text(output ,parse_mode="Markdown")

# Errors
def error(update, context):
    update.message.reply_text('an error occured')

# Commands
def register_handlers(dp):
    dp.add_handler(CommandHandler("start", handler_start))
    dp.add_handler(CommandHandler("help", handler_help))
    dp.add_handler(CommandHandler("list", handler_list))
    dp.add_handler(CommandHandler("rates", handler_rates))
    dp.add_handler(CommandHandler("btc", handler_BTC))
    dp.add_handler(CommandHandler("eth", handler_ETH))
    dp.add_handler(CommandHandler("atom", handler_ATOM))
    dp.add_handler(CommandHandler("ada", handler_ADA))
    dp.add_handler(CommandHandler("ftm", handler_FTM))
    dp.add_handler(CommandHandler("sol", handler_SOL))
    dp.add_handler(CommandHandler("xrp", handler_XRP))
    dp.add_handler(CommandHandler("xtz", handler_XTZ))
    dp.add_handler(CommandHandler("omg", handler_OMG))
    dp.add_handler(CommandHandler("luna", handler_LUNA))
    dp.add_handler(CommandHandler("mana", handler_MANA))
    dp.add_handler(CommandHandler("link", handler_LINK))
    dp.add_handler(CommandHandler("ksm", handler_KSM))
    dp.add_handler(CommandHandler("doge", handler_DOGE))
    dp.add_error_handler(error)

def main():
    updater = Updater(config.TOKEN, use_context=True)
    register_handlers(updater.dispatcher)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()