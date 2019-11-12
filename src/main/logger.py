# -*- coding: utf-8 -*-
"""Logger Class


"""
class LogItem(object):
    def __init__(self, logLevel:int, sender:str, msg:str, info:str):
        self.level = logLevel
        self.sender = sender
        self.msg = msg
        self.info = info

    def __str__(self):
        return("LogItem[ Warning Level:{lvl} From:{sender}, {msg}\t{info}".format(
            lvl=self.level,
            sender=self.sender,
            msg=self.msg,
            info=self.info
        ))

class Logger(object):
    def __init__(self):
        self.__log = []

    def log(self, logLevel:int, sender:str, msg:str, info:str):
        self.__log.append(LogItem(logLevel, sender, msg, info))

    def getLog(self):
        return(self.__log)

    def getLogItem(self, index):
        if index < len(self.__log):
            return(self.__log[index])

    def popLog(self):
        if len(self.__log) > 0:
            return(self.__log.pop())