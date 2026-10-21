import requests
import json
from collections import defaultdict
import time

# 1) GET TEAMID FROM SEARCHING ORG LIST                                     ✔
# 2) USE TEAMID TO SEARCH FOR RECENT MATCHES, -> GET MATCHID FOR STAGE 2    ✔
# 3) COLLECT MATCHID DATA FOR CALCULATIONS                                  ✔
# 4) CALCULATE ALL TEAM MATCH DATA
# 5) OUTPUT INTO PANDA DF FOR USE IN SPREADHSHEET


base_Link = "http://127.0.0.1:3001"

orgIDsNoName = {"0": "278", "1": "4050", "2": "918", "3": "12694", "4": "8185", "5": "11060", "6": "624", "7": "878", "8": "14", "9": "6199", "10": "11229", "11": "5448", "12": "397", "13": "6392", "14": "2593", "15": "1184", "16": "14419", "17": "8877", "18": "12694", "19": "4915", "20": "3478", "21": "120", "22": "474", "23": "2059", "24": "120", "25": "188", "26": "5248", "27": "427", "28": "2406", "29": "11058", "30": "2355", "31": "2359", "32": "6961", "33": "7386", "34": "1034", "35": "2"}
orgIDs = {"DetonatioN FocusMe": "278", "FULL SENSE": "4050", "Global Esports": "918", "Gentle Mates": "12694", "KIWOOM DRX": "8185", "Nongshim RedForce": "11060", "Paper Rex": "624", "Rex Regum Qeon": "878", "T1": "14", "Team Secret": "6199", "VARREL": "11229", "ZETA DIVISION": "5448", "BBL Esports": "397", "Eternal Fire": "6392", "FNATIC": "2593", "FUT Esports": "1184", "GIANTX": "14419", "Karmine Corp": "8877", "Natus Vincere": "4915", "PCIFIC Esports": "3478", "Team Heretics": "1001", "Team Liquid": "474", "Team Vitality": "2059", "100 Thieves": "120", "Cloud9": "188", "Evil Geniuses": "5248", "ENVY": "427", "FURIA": "2406", "G2 Esports": "11058", "KR\u00dc Esports": "2355", "LEVIAT\u00c1N": "2359", "LOUD": "6961", "MIBR": "7386", "NRG": "1034", "Sentinels": "2"}
listOfEvents = ["vct-2026-americas-stage-2", "vct-2026-pacific-stage-2", "vct-2026-emea-stage-2"]
tempEventStore = 0
tempStore = 0

# change id to real teamid list
finalOutput = defaultdict(dict)
with open ('matchIDsForTeams.json', 'w', encoding='utf8') as file:
    for x in orgIDsNoName.values():
        statsResponse = requests.get(f"{base_Link}/v2/team?id={int(x)}&q=matches&page=1")
        if statsResponse.status_code == 200:
                statsData = statsResponse.json()
                print(statsData)
                for i in range(0, 35):
                    if any(event in statsData["data"]["segments"][i]["url"] for event in listOfEvents):
                            matchID = statsData["data"]["segments"][i]["match_id"]
                            teamName = statsData["data"]["segments"][0]["team1"]["name"]
                            teamScore = statsData["data"]["segments"][i]["score"]
                            finalOutput[teamName][tempEventStore] = matchID
                            tempEventStore += 1
                            time.sleep(0.5)
        tempStore += 1
        tempEventStore = 0
    file.write(json.dumps(finalOutput))