from datetime import datetime


class Helper:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        self.__instance = None

    def get_formatted_today(self, d_format='%Y-%m-%d'):
        return datetime.today().strftime(d_format)
