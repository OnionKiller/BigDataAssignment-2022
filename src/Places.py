
from time import sleep
import pandas as pd
import googlemaps

from typing import Tuple
from config import Config
from tqdm import tqdm


class Places(object):

    __gClient:googlemaps.Client
    #lattitude row index as string
    lattitude_name:str='stop_lat'
    longitude_name:str='stop_lon'



    def __init__(self) -> None:
        conf = Config()
        self.__gClient = googlemaps.Client(key=conf.PLACES_API_KEY)


    def get_bars(self,location: Tuple[int,int],radius:int)->pd.DataFrame:
        result = self.__gClient.places_nearby(location=location,radius=radius,type='bar')
        bars = result['results']
        #limited  do while cicle
        for _ in range(10):
            #check for paging token
            if 'next_page_token' not in result:
                break
            # credit to https://stackoverflow.com/a/15452661/8659684
            # the docs say, that there is a delay in pages getting public, I guess it is throttling
            sleep(2)
            result = self.__gClient.places_nearby(location=location,radius=radius,type='bar',page_token=result['next_page_token'])
            bars += result['results']
        df = pd.DataFrame(bars)
        return df


    def get_bars_batch(self,locations: pd.DataFrame,radius:int=1000) -> pd.DataFrame:
        """Get all bars within 1 km
        """
        locations_glob = [ z for z in zip(locations[self.lattitude_name],locations[self.longitude_name])]
        bar_list_list = [ self.get_bars(loc,radius) for loc in tqdm(locations_glob)]
        r_ = pd.concat(bar_list_list)
        r_ = self._format_bar_df(r_)
        return r_
    
    def get_bars_ranged_batch(self,locations: pd.DataFrame,radius_row_name:str) -> pd.DataFrame:
        """Get all bars around points. radius should be defined in the dataframe for each item
        """
        locations_glob = [ z for z in zip(locations[self.lattitude_name],locations[self.longitude_name],locations[radius_row_name])]
        bar_list_list = [ self.get_bars((dat[0],dat[1]),dat[2]) for dat in tqdm(locations_glob, position=0, leave=True)]
        r_ = pd.concat(bar_list_list)
        r_ = self._format_bar_df(r_)
        return r_

    def _format_bar_df(self,df:pd.DataFrame):
        df.drop(columns=['icon','icon_background_color','icon_mask_base_uri','photos','opening_hours','reference','scope'],inplace=True)
        df['bar_lat'] = [x['location']['lat'] for x in df['geometry']]
        df['bar_lon'] = [x['location']['lng'] for x in df['geometry']]
        return df


