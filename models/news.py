import datetime


class News:
    def __init__(self, text="", user=None, time_created=None, photo_source=None):
        self.text = text
        self.user = user
        self.photo_source = photo_source
        self.time_created = time_created

    def __repr__(self):
        return "{} text={}, {} photo".format(
            self.__class__,
            self.text,
            "with" if self.photo_source else "without"
        )


if __name__ == "__main__":
    news = News(text="dsefdsf")
    news.time_created = datetime.datetime.now()
    print(news.time_created)
