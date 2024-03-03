from hashids import Hashids

class ServiceShorter:
    def __init__(self,salt_shorter='',url_id=0, name=''):
        self.salt_shorter = salt_shorter
        self.url_id = url_id
        self.name = name

    def encode(self):
        hashids = Hashids(salt=self.salt_shorter)
        return hashids.encode(self.url_id, 7)

    def decode(self):
        hashids = Hashids(salt=self.salt_shorter)
        return hashids.decode(self.name)
