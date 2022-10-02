# Crypto Currency Bot for Telegram
This bot is outdated, but still works. The updated bot is here: [Click me](https://t.me/OnCCryptoBot)

The telegram bot shows the current rate of cryptocurrencies

About
------------
**A simple telegram bot that shows the exchange rate of cryptocurrencies relative to USDT in the game. Used by the Binance API, data refresh varies by 5 seconds. The bot also works in group chats**

Installation
------------
```shell
# Clone the repository
$ git clone https://github.com/onilyxe/CryptoCurrency.git

# Change the working directory to CryptoCurrency
$ cd CryptoCurrency
```

## Configuring
**Open `config.py` configuration file with text editor and set the token:**
```ini
TOKEN='0000000000:0000000000000000000000000000000000'
```
* `TOKEN` is token for your Telegram bot. You can get it here: [BotFather](https://t.me/BotFather).

## Running
### Using Python
```shell
# Install requirements
$ python3 -m pip install -r requirements.txt

# Run script
$ python3 bot.py
```