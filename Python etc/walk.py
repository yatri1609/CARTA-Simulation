import geopandas as gpd
import pandana as pdna
roads = gpd.read_file("/home/cuip/edges/edges.shp")
stops = gpd.read_file("/home/cuip/Archive/Stops.shp")
net= pdna.Network(stops["Latitude"], stops["Longitude"], roads["from"], roads["to"],
                 roads[["length"]])
net.precompute(420)
net.set_pois(stops, 420, 10, stops.Latitude, stops.Longitude)
net.nearest_pois(420, stops, num_pois=10)