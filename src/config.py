import os


class Config(object):
    PLACES_API_KEY: str

    def __init__(self) -> None:
        from dotenv import load_dotenv

        load_dotenv()
        self.PLACES_API_KEY = os.environ.get("PLACES_API_KEY", "")
