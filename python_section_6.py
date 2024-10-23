import polyline
import pandas as pd
from geopy.distance import geodesic

def decode_polyline_to_df(polyline_str):

    coordinates = polyline.decode(polyline_str)
    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])

    df['distance'] = 0.0
  
    for i in range(1, len(df)):
       
        previous_point = (df.loc[i-1, 'latitude'], df.loc[i-1, 'longitude'])
        current_point = (df.loc[i, 'latitude'], df.loc[i, 'longitude'])
        df.loc[i, 'distance'] = geodesic(previous_point, current_point).meters
    
    return df

polyline_str = '_p~iF~ps|U_ulLnnqC_mqNvxq`@'
df = decode_polyline_to_df(polyline_str)
print(df)
