# -*- coding: utf-8 -*-
"""ErrorSender AbstractClass

This AbstractClass is a pattern for error sending.   
  from a *<Lexer> buffer*.  It checks whether the sequence
  of <Tokens> matches a valid pattern.  If it matches then
  a _Pass_ ParseFlag is outputted, otherwise a _Fail_
  ParseFlag is outputted.

Input: <Lexer>
Output: <ParseFlag>
"""
class ErrorSender(object):
    def __init__(self):
        self._receivers = []

    def register_receiver(self, receiver):
        self._receivers.append(receiver)

    def unregister_receiver(self, receiver):
        self._receivers.remove(receiver)

    def _notify_receivers(self, sender, msg, info):
        for receiver in self._receivers:
            receiver.notify({"sender":sender, "msg":msg, "info":info})

    @abstractmethod
    def _error(self):
        raise NotImplementedError

    __register_receiver, __unregister_receiver = register_receiver, unregister_receiver
    __receivers, __notify_receivers = _receivers, _notify_receivers