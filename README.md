# wechatbot

WechatBot serves as a basic tool for automatical Wechat message processing (receiving and sending) based on Web Wechat APIs using Python.

We note that no official Web Wechat APIs are available, thus the stability of the project is not guaranteed.

We would thank https://github.com/liuwons/wxBot and https://github.com/Urinx/WeixinBot for their work on Python based Web Wechat projects. Most APIs in this projects are implemented according to their work.

## Usage

qrcode is required to use wechatbot. PIL or pillow is optional.

A user can run main.py directly for a simple WechatBot demo, which prints and auto replies all received plain text messages (except the ones sent by itself), and supports manual message sending. After starting up, the demo demonstrates a QRcode for cellphone scanning, and manual confirmation on the cellphone is required. Afterwards, one can type 'h', 'q', 'si', or 'sn' in the terminal, for 'help', 'quit', 'send message by ID', or 'send message by name', respectively.

## Extension

The WechatBot is designed for easy and flexible extension. Message processing and / or sending extensions can be added to the framework by overriding the following functions:
- run(conf)           : start the wechatbot with configuration conf (dict)
- help()              : print help information
- sendMsgTextByID(id, content)        : send a plain text message content to the group/contact with ID id
- sendMsgTextByName(name, content)    : send a plain text message content to the group/contact with remark name or nickname name
- procMsgText(self, grpName, usrName, content, msg)   : process a plain text message content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
- procMsgImage(self, grpName, usrName, content, msg)  : process an image content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
- procMsgVoice(self, grpName, usrName, content, msg)  : process a voice message content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
- procMsgCard(self, grpName, usrName, content, msg)   : process a card message content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
- procMsgEmoji(self, grpName, usrName, content, msg)  : process an emoji content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
- procMsgAppLink(self, grpName, usrName, content, msg)    : process an app link message content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
- procMsgVideo(self, grpName, usrName, content, msg)  : process a video message content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
- procMsgRecall(self, grpName, usrName, content, msg) : process a message recalled content, sent by user usrName, in group grpName (if not empty); original message is provided in msg
By default, content provides processed message body (such as plain text, xml data, image url, etc.), and msg provides the raw message in json format.

The following functions are provided for convenience:
- getGrpNameByID(id)  : obtain a group's nickname by its ID (a.k.a. UserName, string)
- getUsrNameByID(id)  : obtain a contact's remark name (if valid) or nickname by its ID (a.k.a. UserName, string)
- getIDByName(id)     : obtain a group/contact's ID by its remark name (contact only) or nickname

Furthermore, more sendMsg functions can be defined.
