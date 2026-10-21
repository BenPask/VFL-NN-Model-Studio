import requests
import json
from collections import defaultdict
import time

base_Link = "http://127.0.0.1:3001"

teamIdAmerList = [1034, 2359, 7386, 5248, 427, 2406, 120, 6961, 11058, 2, 188, 2355]

nearFinalOutput = defaultdict(dict)
finalOutput = defaultdict(dict)
for i in range(len(teamIdAmerList)):
    statsResponse = requests.get(f"{base_Link}/v2/team?id={teamIdAmerList[i]}")
    if statsResponse.status_code == 200:
        statsData = statsResponse.json()

        for y in range (0, 5) :
            targetPlayerName = statsData["data"]["segments"][0]["roster"][y]["alias"]
            targetPlayerIdScrape = statsData["data"]["segments"][0]["roster"][y]["id"]
            storeOrg = statsData["data"]["segments"][0]["tag"]
            nearFinalOutput[targetPlayerName] = {"Org" : storeOrg, "ID" : targetPlayerIdScrape}
            
        finalOutput = nearFinalOutput
    time.sleep(1)
with open('playerIDAndOrg', 'w', encoding='utf8') as file:
    file.write(json.dumps(finalOutput))