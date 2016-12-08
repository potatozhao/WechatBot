# coding=utf-8

# system module for resolving command line arguments, etc
import  sys
reload(sys)
sys.setdefaultencoding("utf-8")
# trace back for exception processing and debugging
import  traceback
# logging configuration
import  logging
logging.basicConfig(format="%(levelname)-9s[%(asctime)s][%(filename)s:%(funcName)s:%(lineno)d] %(message)s \\EOF", level=logging.INFO);
# time processing and thread sleeping
import  time
# random module for generating random strings
import  random

# wechatbot
import  wechatbot

class WechatBotDemo(wechatbot.WechatBot):

    """
    Supported public functions:

        run(conf)           : start the wechatbot with configuration conf (dict)
        
        help()              : print help information
        
        getGrpNameByID(id)  : obtain a group's nickname by its ID (a.k.a. UserName, string)
        getUsrNameByID(id)  : obtain a contact's remark name (if valid) or nickname by its ID (a.k.a. UserName, string)
        getIDByName(id)     : obtain a group/contact's ID by its remark name (contact only) or nickname

        sendMsgTextByID(id, content)        : send a plain text message content to the group/contact with ID id
        sendMsgTextByName(name, content)    : send a plain text message content to the group/contact with remark name or nickname name

        procMsgText(self, grpName, usrName, content, msg)   : process a plain text message content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
        procMsgImage(self, grpName, usrName, content, msg)  : process an image content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
        procMsgVoice(self, grpName, usrName, content, msg)  : process a voice message content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
        procMsgCard(self, grpName, usrName, content, msg)   : process a card message content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
        procMsgEmoji(self, grpName, usrName, content, msg)  : process an emoji content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
        procMsgAppLink(self, grpName, usrName, content, msg)    : process an app link message content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
        procMsgVideo(self, grpName, usrName, content, msg)  : process a video message content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
        procMsgRecall(self, grpName, usrName, content, msg) : process a message recalled content, sent by user usrName, in group grpName (if not empty); original message is provided in msg

    """

    # override processing function
    def procMsgText(self, grpName, usrName, content, msg):

        if usrName != self._User["NickName"]:
            if "" != grpName:
                self.sendMsgTextByName(grpName, "At " + str(time.asctime(time.localtime(time.time()))) + ", " + usrName + " says : " + content)
            else:
                self.sendMsgTextByName(usrName, "[" + str(time.asctime(time.localtime(time.time()))) + "][Auto reply]您的消息我已收到。")

        return

    # override processing function
    def procMsgImage(self, grpName, usrName, content, msg):

        return

    # override processing function
    def procMsgVoice(self, grpName, usrName, content, msg):

        return

    # override processing function
    def procMsgCard(self, grpName, usrName, content, msg):

        return

    # override processing function
    def procMsgEmoji(self, grpName, usrName, content, msg):

        return

    # override processing function
    def procMsgAppLink(self, grpName, usrName, content, msg):

        return

    # override processing function
    def procMsgVideo(self, grpName, usrName, content, msg):

        return

    # override processing function
    def procMsgRecall(self, grpName, usrName, content, msg):

        return    
        
def main():

    # default configuration
    conf = {
            #"AppID"             : "wx782c26e4c19acffb",
            #"Lang"              : "zh_CN",
            #"DeviceID"          : "e" + repr(random.random())[2 : 17],
            #"MessageSyncInterval"   : 1,
        }

    # configuration in command line arguments
    for i in range(1, len(sys.argv)):
        logging.debug("Argument : %s", sys.argv[i])
        arg = string.split(sys.argv[i], "=", 1)
        if 1 == len(arg):
            conf[arg[0]] = True
        else:
            conf[arg[0]] = arg[1]
    
    # wechat bot
    wbot = WechatBotDemo()
    wbot.run(conf)

    return
    
if __name__ == "__main__" :
    
    main()
