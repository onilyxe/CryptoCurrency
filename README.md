<h1 align="center">Crypto Currency Bot for Telegram</a> 
<img src="https://raw.githubusercontent.com/onilyxe/CryptoCurrency/main/image/telegram.webp" height="32"/></h1>
<p align="center"><b>The telegram bot shows the current rate of cryptocurrencies.</b></p>
<p align="center"><b><a href="https://t.me/OnCCryptoBot" target="_blank">Try the my bot</b></p>

## About
**A simple telegram bot that shows the exchange rate of cryptocurrencies relative to USDT in the game. Used by the Binance API, data refresh varies by 5 seconds. The bot also works in group chats.**

## Installation
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
```e