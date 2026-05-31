# -*- coding: utf-8 -*-

"""
This is the seventh example to perform an evaluation of a decentralized scenario.
Therefore the optimized operation of the devices is simulated and the key performance indicators are calculated.
"""

# Import classes of the districtgenerator to be able to use the district generator.
from districtgenerator.classes import *

def hangetal_simulation():

    # Initialize District
    data = Datahandler(scenario_name = "Hangetal", env_path=".env.CONFIG.Hangetal2015")

    data.generateDistrictComplete(calcUserProfiles=True, saveUserProfiles=True, gen_cars=False)

    # Calculation of the devices' optimal operation
    data.optimizationClusters()

    # Calculation of the key performance indicators using the devices' operation profiles of clustered time periods
    data.calculateKPIs()
    # Create a certificate (PDF) which summarizes the district parameters and calculated KPIs
    data.KPIs.create_certificate(data=data, result_path=data.resultPath)

    print("Congratulations! You calculated an optimized device operation for the selected neighborhood!")
    return data


if __name__ == '__main__':
    data = hangetal_simulation()