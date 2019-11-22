class Event(object):
    def __init__(self):
        self.__event_handlers = []

    def __iadd__(self, handler):
        self.__event_handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__event_handlers.remove(handler)
        return self

    def __call__(self, *args, **kwargs):
        for eh in self.__event_handlers:
            eh(*args, **kwargs)
