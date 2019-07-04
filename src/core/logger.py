# -*- coding: utf-8 -*-
"""Logger Class


"""
class LogItem(object):
  def __init__(self, logInfo):
    self.level = logInfo[0]
    self.sender = logInfo[1]
    self.msg = logInfo[2]
    self.info = logInfo[3]

class Logger(object):
  def __init__(self):
    self.__log = []

  def log(self, logInfo):
    self.__log.append(LogItem(logInfo))

  def getLog(self):
    return(self.__log)

  def getLogItem(self, index):
    if index < len(self.__log):
      return(self.__log[index])

  def popLog(self):
    if len(self.__log) > 0:
      return(self.__log.pop())