import os
import requests
import zipfile
import pandas as pd
import io
import shutil


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

    def extract(self):
        self.__download()
        if os.path.isdir("temp/bkk"):
            shutil.rmtree("temp/bkk")
        archive = zipfile.ZipFile(self.path, 'r')
        archive.extractall("temp/bkk")
        for i, path in enumerate(os.listdir("temp/bkk")):
            os.rename("temp/bkk/" + path, "temp/bkk/" + path.replace(".txt", ".csv"))

    def __getFile(self, path):
        self.__download()
        archive = zipfile.ZipFile(self.path, 'r')
        return archive.read(path).decode("utf-8")

    def __getDataFrame(self, path):
        csv = self.__getFile(path)
        handler = io.StringIO(csv)
        return pd.read_csv(handler)

    def getAgency(self):
        return self.__getDataFrame("agency.txt").set_index('agency_id')

    def getCalendarDates(self):
        return self.__getDataFrame("calendar_dates.txt").set_index('service_id')

    def getPathways(self):
        return self.__getDataFrame("pathways.txt").set_index(['pathway_id', 'from_stop_id', 'to_stop_id'])

    def getRoutes(self):
        return self.__getDataFrame("routes.txt").set_index(['route_id', 'agency_id'])

    def getShapes(self):
        return self.__getDataFrame("shapes.txt").set_index('shape_id')

    def getStopTimes(self):
        return self.__getDataFrame("stop_times.txt").set_index(['stop_id', 'trip_id'])

    def getStops(self):
        return self.__getDataFrame("stops.txt").set_index('stop_id')

    def getTrips(self):
        return self.__getDataFrame("trips.txt").set_index(['trip_id', 'route_id', 'service_id', 'shape_id'])

    def getAll(self):
        return self.getAgency()\
            .join(self.getRoutes())\
            .join(self.getTrips())\
            .join(self.getStopTimes())\
            .join(self.getStops())
