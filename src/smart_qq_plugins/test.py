import thread  
from random import randint

from smart_qq_bot.messages import GroupMsg, PrivateMsg
from smart_qq_bot.signals import on_all_message, on_bot_inited
from smart_qq_bot.logger import logger

def tick():
       print('Tick! The time is:a')
        
def loop0():
      scheduler = BlockingScheduler()
     scheduler.add_job(tick,'cron', second='*/20', hour='*')    
     print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown() 


@on_bot_inited("PluginManager")
def manager_init(bot):
    logger.info("Plugin Manager is available now:)")
　　thread.start_new_thread(loop0, ())  
