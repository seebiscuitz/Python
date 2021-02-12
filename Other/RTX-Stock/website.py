class website:

    def __init__(self, name, url, status, items):
        #amazon, amazon.co.uk, Buy Now, items...
        self.name = name
        self.url = url
        self.status = status
        self.items = []
        for nitem in items:
            self.items.append([nitem[0],nitem[1]])
        return

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_items(self):
        return self.items

    def get_status(self):
        return self.status