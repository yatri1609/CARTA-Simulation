#!/usr/bin/env python

import os
import sys
import optparse
import csv
import sumolib

# import python modules from the sumo/tools directory

if '$SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['$SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

# checkBinary checks if the path to sumo/bin is correct
from sumolib import checkBinary
import traci

# include option for non-gui (sumo) interaction
def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                          default=False, help="run commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options

def get_geo():
    while traci.simulation.getMinExpectedNumber() > 0:
        stopID = traci.vehicle.getBusStopIDList()
        geo = traci.simulation.convertGeo(traci.vehicle.getPosition(self,vehID),x,y, isGeo=False)

        with open('data.csv','w') as geofile:
            geofileWriter = csv.writer(geofile)
            geofileWriter.writerow(stopID)


net = sumolib.net.readNet('final.net.xml')
new_route_file = []
for route in sumolib.output.parse_fast("myRoutes.rou.xml", 'route', ['edges']):
    edge_ids = route.edges.split()
    # do something with the vector of edge ids
    route_carta_new = new_route_file.append(edge_ids)
    print(node.getEdge(edge_ids).getCoord())

# run TraCI, most instructions for sim located here
def run():

    # keep count of steps in sim
    traci_step = 0

    # while all vehicles are still in a route
    while traci.simulation.getMinExpectedNumber() > 0:
        get_geo()
	# write out what to do here, comment out "pass"
        traci.simulationStep()

    # Close TracI
    traci.close()
    sys.stdout.flush()


# Main function
if __name__ == "__main__":
    options = get_options()

    # check binary for sumo or sumo-gui
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # start traCI with a given input (sumo config) file and a given output
    traci.start([sumoBinary, "-c", "GenericSUMOConfig.sumocfg", "--tripinfo-output", "tripInfo"])

    run()
