import telegram
import asyncio

async def send_signal(trading_pair, signal_type):
    bot_token = "6119983782:AAGwSeqDU2E7UfyhIz6t2wh81AGopsMjZx8"
    bot = telegram.Bot(token=bot_token)
    channel_name = "@SignalBot100"
    await bot.send_message(chat_id=channel_name, text=trading_pair + ": " + signal_type)

async def main(trading_pair, signal_text):
    if signal_text == "Long1" or signal_text == "Long2":
        await send_signal(trading_pair, "Long Signal")
    elif signal_text == "Venta L1" or signal_text == "Venta L2":
        await send_signal(trading_pair, "Close Long Signal")
    elif signal_text == "Short1" or signal_text == "Short2":
        await send_signal(trading_pair, "Short Signal")
    elif signal_text == "Cierre S1" or signal_text == "Cierre S2":
        await send_signal(trading_pair, "Close Short Signal")

if __name__ == "__main__":
    trading_pair = input("Enter the trading pair: ")
    signal_text = input("Enter the signal text: ")
    asyncio.run(main(trading_pair, signal_text))
