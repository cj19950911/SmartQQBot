from random import randint

from smart_qq_bot.messages import GroupMsg, PrivateMsg
from smart_qq_bot.signals import on_all_message, on_bot_inited
from smart_qq_bot.logger import logger


@on_bot_inited("PluginManager")
def manager_init(bot):
    logger.info("Plugin Manager is available now:)")

@on_all_message(name="SamplePlugin")
def sample_plugin(msg, bot):
    """
    :type bot: smart_qq_bot.bot.QQBot
    :type msg: smart_qq_bot.messages.GroupMsg
    """
    msg_id = randint(1, 10000)
    
    # 发送一条群消息
    if isinstance(msg, GroupMsg):
        bot.send_group_msg("msg", msg.from_uin, msg_id)
    # 发送一条私聊消息
    elif isinstance(msg, PrivateMsg):
        bot.send_friend_msg("msg", msg.from_uin, msg_id)
