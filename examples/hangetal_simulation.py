# -*- coding: utf-8 -*-

"""
This is the seventh example to perform an evaluation of a decentralized scenario.
Therefore the optimized operation of the devices is simulated and the key performance indicators are calculated.
"""

# Import classes of the districtgenerator to be able to use the district generator.
from districtgenerator.classes import *

def hangetal_simulation():

    # Initialize District
    data = Datahandler(env_path=".env.Hangetal_ist_2015.txt")
    data.generateDistrictComplete(calcUserProfiles=False, saveUserProfiles=False, gen_cars=False, designEnergyhub=False)
    data.optimizationClusters()
    data.calculateKPIs()
    data.KPIs.create_certificate(data=data, result_path=data.resultPath)

    data = Datahandler(env_path=".env.Hangetal_erweitert_2015_gesamtwirtschaftlich.txt")
    data.generateDistrictComplete(calcUserProfiles=False, saveUserProfiles=True, gen_cars=False, designEnergyhub=False)
    data.optimizationClusters()
    data.calculateKPIs()
    data.KPIs.create_certificate(data=data, result_path=data.resultPath)

    data = Datahandler(env_path=".env.Hangetal_erweitert_2015_elektrisch.txt")
    data.generateDistrictComplete(calcUserProfiles=False, saveUserProfiles=True, gen_cars=False, designEnergyhub=False)
    data.optimizationClusters()
    data.calculateKPIs()
    data.KPIs.create_certificate(data=data, result_path=data.resultPath)

    data = Datahandler(env_path=".env.Hangetal_erweitert_2015_oekologisch.txt")
    data.generateDistrictComplete(calcUserProfiles=False, saveUserProfiles=True, gen_cars=False, designEnergyhub=False)
    data.optimizationClusters()
    data.calculateKPIs()
    data.KPIs.create_certificate(data=data, result_path=data.resultPath)
    #
    data = Datahandler(env_path=".env.Hangetal_erweitert_2015_resilienz.txt")
    data.generateDistrictComplete(calcUserProfiles=False, saveUserProfiles=True, gen_cars=False, designEnergyhub=False)
    data.optimizationClusters()
    data.calculateKPIs()
    data.KPIs.create_certificate(data=data, result_path=data.resultPath)

    print("Congratulations! You calculated an optimized device operation for the selected neighborhood!")
    return data


if __name__ == '__main__':
    data = hangetal_simulation()