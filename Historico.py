from datetime import datetime

class historico:
    def __init__(self, url):
        self.__url = url
        self.__dataehora =datetime.now()

@property
def url(self):
    return self.__url
@property
def dataehora(self):
    return self.__dataehora

        