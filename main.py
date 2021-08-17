from model.Connection import Connection
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

connect_db = None
logger = logging.getLogger(__name__)
tVersion = {}
iStep = -1

def start(update, context):
  """Send a message when the command /start is issued."""
  update.message.reply_text('Hi!')
def error(update, context):
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, context.error)

def insertLog(update, context):
  global iStep
  
  st =update.message.text
  print(getMsgContinue(iStep))
  iStep = 0
  update.message.reply_text(getMsgContinue(iStep))
  


def getMsgContinue(i):
  switcher = {
    0:"Nhập tên phiên bản (ex: 1.0.1)",
    1:"Nhập link phiên bản ( google driver) - Nếu không có/chưa có thể gõ bỏ qua(nhập cancle)",
    2:"Nhập log phiên bản - Nếu không có có thể bỏ qua (nhập cancle)",
    3:"nhập end để kết thúc!"
  }
  return switcher.get(i,"Invalid day of week")
def messageHandle(update, context):
  global iStep
  global tVersion
  if iStep >= 0 & iStep < 3:
    if iStep ==0:
      tVersion["version"]= update.mesage.text
    elif iStep ==1:
      if update.mesage.text=="cancle":
        tVersion.url= None
      else:
         tVersion.url= update.mesage.text
    elif iStep ==2:
      if update.mesage.text=="cancle":
        tVersion.des= None
      else:
         tVersion.des= update.mesage.text
    else:
      print("deo co gi")

    iStep +=1
    update.message.reply_text(getMsgContinue(iStep))
  elif iStep ==3:
    print("ket thuc",tVersion)






def main():
  connect_db = Connection()
  global iStep
  iStep =-1
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
