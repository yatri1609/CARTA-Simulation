
import osmnx as ox
from pandana.loaders import osm

G = ox.graph_from_address('Chattanooga, Tennessee, USA')
ox.plot_graph(G)

# define your selected amenities and bounding box
amenities = ['busstops']
bbox = [33.49422570442377,-7.709587097167969,33.64046399626814,-7.494117736816405]

# request them from the OpenStreetMap API (Overpass)
pois = osm.node_query(bbox[0], bbox[1], bbox[2], bbox[3],tags=osm_tags)
pois = pois[pois['amenity'].isin(amenities)]

#List how many we downloaded
pois.amenity.value_counts()