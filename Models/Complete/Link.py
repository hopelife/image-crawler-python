from Models.Model import Model


class Link(Model):
    file_path = 'storage/complete/links.txt'

    def __init__(self):
        self.links.clear()
        self.fetch()
        Model.__init__(self)

