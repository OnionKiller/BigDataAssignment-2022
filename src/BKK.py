import os
import requests
import zipfile
import pandas as pd
import io


class BKK:

    def __init__(self, url):
        self.path = "temp/bkk.zip"
        self.url = url
        self.__download()

    def __download(self, chunk_size=128):
        if not os.path.isdir("temp"):
            os.mkdir("temp")

        if not os.path.isfile(self.path):
            r = requests.get(self.url, stream=True)
            with open(self.path, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    fd.write(chunk)

    def update(self):
        os.remove(self.path)
        self.__download()

    def __getFile(self, path):
        self.__download()
        archive = zipfile.ZipFile(self.path, 'r')
        return archive.read(path).decode("utf-8")

    def __getDataFrame(self, path):
        csv = self.__getFile(path)
        handler = io.StringIO(csv)
        return pd.read_csv(handler)

    def getAgency(self):
        return self.__getDataFrame("agency.txt")

    def getCalendarDates(self):
        return self.__getDataFrame("calendar_dates.txt")

    def getFeedInfo(self):
        return self.__getDataFrame("feed_info.txt")

    def getPathways(self):
        return self.__getDataFrame("pathways.txt")

    def getRoutes(self):
        return self.__getDataFrame("routes.txt")

    def getShapes(self):
        return self.__getDataFrame("shapes.txt")

    def getStopTimes(self):
        return self.__getDataFrame("stop_times.txt")

    def getStops(self):
        return self.__getDataFrame("stops.txt")

    def getTrips(self):
        return self.__getDataFrame("trips.txt")
