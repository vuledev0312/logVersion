from model.Connection import Connection
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

connect_db = None
logger = logging.getLogger(__name__)
insert_code=-1
def start(update, context):
  """Send a message when the command /start is issued."""
  update.message.reply_text('Hi!')
def error(update, context):
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, context.error)

def insertLog(update, context):
  st =update.message.text
  insert_code=0
  print(getMsgContinue(insert_code))
  #update.message.reply_text()


def getMsgContinue(i):
  switcher = {
    0:"Nhập tên phiên bản (ex: 1.0.1)",
    1:"Nhập link phiên bản ( google driver) - Nếu không có/chưa có thể gõ bỏ qua",
    2:"Nhập log phiên bản - Nếu không có có thể bỏ qua",
    3:"nhập end để kết thúc!"
  }
  return switcher(i,"Invalid day of week")
def messageHandle(update, context):
  if insert_code ==0:
    return
  #print(update.message.text)


def main():
  connect_db = Connection()
  print("db connect tion __Main__")
  updater = Updater('1954009854:AAHTp2SnqveJre2kGV_i66MsXqTU7xLLiog',use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("insertLog",insertLog))
  dp.add_handler(MessageHandler(Filters.text,messageHandle))


  dp.add_error_handler(error)

    # Start the Bot
  updater.start_polling()

  updater.idle()

if __name__=="__main__":
  main()
