from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time
import logging
import os
import random

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def help(bot, update):
  msg = "오늘의 급식 , /Today\n월요일 급식, /Mon\n화요일 급식, /Tue\n수요일 급식, /Wed\n목요일 급식, /Thu\n금요일 급식, /Fri\n봇 오류 발생시 @leejun9hun 혹은\nezraeffect@ezra.ml으로 연락 바랍니다."
  bot.sendMessage(update.message.chat_id, text=msg)

def iam(bot, update):
  chat_id = update.message.chat_id
  msg = "my chat_id is %d" %(chat_id)
  bot.sendMessage(chat_id=update.message.chat_id, text=msg)

def start(bot, update):
  chat_id = update.message.chat_id
  user = update.message.from_user
  msg = "오늘의 급식 , /Today\n월요일 급식, /Mon\n화요일 급식, /Tue\n수요일 급식, /Wed\n목요일 급식, /Thu\n금요일 급식, /Fri\n봇 오류 발생시 @leejun9hun 혹은\nezraeffect@ezra.ml으로 연락 바랍니다."
  bot.sendMessage(update.message.chat_id, text=msg)
### 여기를 수정하세요 ###

#급식 파싱 부분
def Today(bot, update):
  n = time.localtime().tm_wday
  user = update.message.from_user
  f = open(str(n) + ".txt", 'r')
  bot.sendMessage(update.message.chat_id, text= "오늘 급식\n" + f.read())
  f.close()

def Mon(bot, update):
  n = time.localtime().tm_wday
  user = update.message.from_user
  f = open("0.txt", 'r')
  bot.sendMessage(update.message.chat_id, text= "이번주 월요일 급식\n" + f.read())
  f.close()

def Tue(bot, update):
  n = time.localtime().tm_wday
  user = update.message.from_user
  f = open("1.txt", 'r')
  bot.sendMessage(update.message.chat_id, text= "이번주 화요일 급식\n" + f.read())
  f.close()

def Wed(bot, update):
  n = time.localtime().tm_wday
  user = update.message.from_user
  f = open("2.txt", 'r')
  bot.sendMessage(update.message.chat_id, text= "이번주 수요일 급식\n" + f.read())
  f.close()

def Thu(bot, update):
  n = time.localtime().tm_wday
  user = update.message.from_user
  f = open("3.txt", 'r')
  bot.sendMessage(update.message.chat_id, text= "이번주 목요일 급식\n" + f.read())
  f.close()

def Fri(bot, update):
  n = time.localtime().tm_wday
  user = update.message.from_user
  f = open("4.txt", 'r')
  bot.sendMessage(update.message.chat_id, text= "이번주 금요일 급식\n" + f.read())
  f.close()
### Don't Touch ###
def query(msg) :
  return msg

def response(bot, update):
  chat_id = update.message.chat_id
  user = update.message.from_user
  user_name = "%s%s" %(user.last_name, user.first_name)

  r_msg = query(update.message.text)
  bot.sendMessage(chat_id,
                  text=r_msg)

def error(bot, update, error):
  logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
  # Create the EventHandler and pass it your bot's token.
  with open(os.path.join('/home/ubuntu/telegram_jingyomeal/','my.keyfile'), 'r') as f :
    token = f.readline().strip()

  updater = Updater(token)

  # Get the dispatcher to register handlers
  dp = updater.dispatcher

  # on different commands - answer in Telegram
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("help", help))
  dp.add_handler(CommandHandler("iam", iam))
  dp.add_handler(CommandHandler("Today", Today))
  dp.add_handler(CommandHandler("Mon", Mon))
  dp.add_handler(CommandHandler("Tue", Tue))
  dp.add_handler(CommandHandler("Wed", Wed))
  dp.add_handler(CommandHandler("Thu", Thu))
  dp.add_handler(CommandHandler("Fri", Fri))

  # on noncommand i.e message - echo the message on Telegram
  dp.add_handler(MessageHandler([Filters.text], response))

  # log all errors
  dp.add_error_handler(error)

  # Start the Bot
  updater.start_polling()

  # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
  # SIGTERM or SIGABRT. This should be used most of the time, since
  # start_polling() is non-blocking and will stop the bot gracefully.
  updater.idle()

if __name__ == '__main__':
  main()
