import requests
import json
from collections import defaultdict
import pandas

base_Link = "http://127.0.0.1:3001"

playerStatsList = ["org", "agents", "rating", "average_damage_per_round", "kills_per_round"]
orgList = ["DFM","FS","GE","GEN", "KRX","NS","PRX","RRQ","T1","TS","VL","ZETA","BBL","EF","FNC","FUT","GX","JL","KC","M8","NAVI","PCF","TH","TL","VIT","100T","C9","EG","ENVY","FUR","G2","KRÜ","LEV","LOUD","MIBR","NRG","SEN"]


statsResponse = requests.get(f"{base_Link}/v2/stats?region=china&timespan=all")
if statsResponse.status_code == 200:
    statsData = statsResponse.json()
    print(statsData)

    finalOutput = defaultdict(dict)
    with open ('PlayerStatsRecent.txt', 'w', encoding='utf8') as file:
        for i in range(0, 100):
            print(i)
            playerOrg = statsData["data"]["segments"][i]["org"]
            if (playerOrg in orgList):
                targetPlayerName = statsData["data"]["segments"][i]["player"]
            
                for y in playerStatsList:
                    targetPlayerStats = statsData["data"]["segments"][i][y]
                    finalOutput[targetPlayerName][y] = targetPlayerStats
        file.write(json.dumps(finalOutput))
    finalOutputDF = pandas.DataFrame(finalOutput)
    finalOutputDF.to_csv('outputCSV.csv', index=False)