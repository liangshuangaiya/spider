# 获取键盘输入，发送给联系人

import itchat
from click._compat import raw_input


# 保存登陆信息，免密登陆
itchat.auto_login(hotReload=True)


inputStr = raw_input()
while inputStr != "null":
    itchat.send(str(inputStr), 'filehelper')
    inputStr = raw_input()

