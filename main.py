from model.Connection import Connection
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from model.MDbLog import MDbLog

connect_db = None
logger = logging.getLogger(__name__)
tVersion = MDbLog()
iStep = -1
flag = 0

def start(update, context):
  """Send a message when the command /start is issued."""
  update.message.reply_text('Hi!')
def error(update, context):
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, context.error)

def insertLog(update, context):
  global iStep
  global flag
  flag =0
  st =update.message.text
  print(getMsgContinue(iStep))
  iStep = 0
  update.message.reply_text(getMsgContinue(iStep))
  
def changeLog(update,context):
  global iStep
  global flag
  flag =1
  iStep = 0
  update.message.reply_text(getMsgChangeLogContinue(iStep))

def getMsgContinue(i):
  switcher = {
    0:"Nhập tên phiên bản (ex: 1.0.1)",
    1:"Nhập link phiên bản ( google driver) - Nếu không có/chưa có thể gõ bỏ qua(nhập cancle)",
    2:"Nhập log phiên bản - Nếu không có có thể bỏ qua (nhập cancle)",
    3:"nhập end để kết thúc!"
  }
  return switcher.get(i,"Invalid day of week")
def getMsgChangeLogContinue(i):
    switcher = {
    0:"Nhập phiên bản cần thay đổi",
    1:"Nhập thuộc tính cần thay đổi:\n 1 - Version\n 2 - link Version\n 3 - Log Version",
    2:"Nhập nội dung thanh đổi",
    3:"nhập end để kết thúc!"
    }
    return switcher.get(i,"Invalid day of week")

def messageHandle(update, context):
  global flag
  if flag ==0:
    _creat_log(update)
  elif flag ==1:
    _change_log(update)





def _change_log(update):
  global iStep
  global tVersion
  global connect_db
  if iStep >= 0 and iStep < 3:
    if iStep ==0:
      record = connect_db.get_version_by_name(update.message.text)
      if record != None:
        print(update.message.text)
      else:
         update.message.reply_text("Version không tồn tại! Vui lòng nhập lai")
         return
    elif iStep ==1:
      if update.message.text=="cancle":
        tVersion.link_version= None
      else:
         tVersion.link_version= update.message.text
    elif iStep ==2:
      if update.message.text=="cancle":
        tVersion.decreption_version= None
      else:
         tVersion.decreption_version= update.message.text
    
    print(iStep)
    iStep +=1
    update.message.reply_text(getMsgChangeLogContinue(iStep))
  elif iStep <=3:
    
    result = connect_db.create_log(tVersion)
    print("ket thuc",result)
      
def _creat_log(update):
  global iStep
  global tVersion
  global connect_db
  if iStep >= 0 and iStep < 3:
    if iStep ==0:
      success = connect_db.check_version(update.message.text)
      if success:
        tVersion.name_version= update.message.text
      else:
         update.message.reply_text("Version đã trùng, vui lòng nhập lại!")
         return
    elif iStep ==1:
      if update.message.text=="cancle":
        tVersion.link_version= None
      else:
         tVersion.link_version= update.message.text
    elif iStep ==2:
      if update.message.text=="cancle":
        tVersion.decreption_version= None
      else:
         tVersion.decreption_version= update.message.text
    
    print(iStep)
    iStep +=1
    update.message.reply_text(getMsgContinue(iStep))
  elif iStep <=3:
    
    result = connect_db.create_log(tVersion)
    print("ket thuc",result)



def main():
  
  global iStep
  global connect_db 
  connect_db = Connection()
  iStep =-1
  print("db connect tion __Main__")
  updater = Updater('1954009854:AAHTp2SnqveJre2kGV_i66MsXqTU7xLLiog',use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("insertLog",insertLog))
  dp.add_handler(CommandHandler("changeLog",changeLog))
  dp.add_handler(MessageHandler(Filters.text,messageHandle))


  dp.add_error_handler(error)

    # Start the Bot
  updater.start_polling()

  updater.idle()

if __name__=="__main__":
  main()
