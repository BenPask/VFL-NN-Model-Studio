import requests
import json
from collections import defaultdict
import time
import ast
import copy

# 1) GET TEAMID FROM SEARCHING ORG LIST                                     ✔
# 2) USE TEAMID TO SEARCH FOR RECENT MATCHES, -> GET MATCHID FOR STAGE 2    ✔
# 3) COLLECT MATCHID DATA FOR CALCULATIONS                                  ✔
# 4) CALCULATE ALL TEAM MATCH DATA
# 5) OUTPUT INTO PANDA DF FOR USE IN SPREADHSHEET

base_Link = "http://127.0.0.1:3001"

with open ('VLR DATA\Data Outputs\matchIDsForTeams.json', 'r') as file:
      matchIDs = ast.literal_eval(file.read())
file.close()



#WinLoss = {"Win" : 0, "Loss" : 0}                            #0
#Bo3 = {"Games" : 0, "Shutout" : 0}                           #1
#Bo5 = {"Games" : 0, "Shutout" : 0, "Win 3-1" : 0}            #2
#WinRounds = {"WinBy13": 0, "WinBy10" : 0, "WinBy5" : 0}      #3
#LoseRounds = {"LoseBy13" : 0, "LoseBy10" : 0}                #4

tempStatsTemplate = ([{"Win":0, "Loss":0}, {"Games":0, "2-0":0}, 
            {"Games" : 0, "3:0": 0, "3-1" : 0},
            {"WinBy13": 0, "WinBy10" : 0, "WinBy5" : 0}, {"LoseBy13" : 0, "LoseBy10" : 0}])



# WANTS FROM DATA
#       MAP WIN/LOSS                      
#       BO3: NUMBER, 2-0 %
#       BO5: NUMBER, 3-0 %, 3-1 %
#       SHUTOUT %
#       WIN BY 13 ROUNDS %, 10 ROUNDS %, 5 ROUNDS %
#       LOSE BY 13 ROUNDS %, 10 ROUNDS %

# DATA VALUES
#       MAP WIN/LOSS                            DONE
#       BO3: NUMBER, 2-0                        DONE
#       BO5: NUMBER, 3-0, 3-1                   DONE
#       WIN BY 13 ROUNDS, 10 ROUNDS, 5 ROUNDS   DONE
#       LOSE BY 13 ROUNDS, 10 ROUNDS            DONE
finaloutput = defaultdict(dict)
with open ('MatchIDResponse.json', 'w', encoding='utf8') as statsFile:
      for (teamName, matchID) in matchIDs.items():
            tempStats = copy.deepcopy(tempStatsTemplate)

            for i in matchID.values():
                  statsResponse = requests.get(f"{base_Link}/v2/match/details?match_id={i}")
                  if statsResponse.status_code == 200:
                        statsData = statsResponse.json()

                        

                        team1Check = statsData["data"]["segments"][0]["teams"][0]["name"]
                        team2Check = statsData["data"]["segments"][0]["teams"][1]["name"]

                        # Team1 or Team2
                        if (teamName == team1Check):
                              team = "team1"
                              teamVal = 0          

                        else:
                              team = "team2"
                              teamVal = 1
                              
                        
                        

                        # Win/Loss
                        totalMaps = int(statsData["data"]["segments"][0]["teams"][0]["score"]) + int(statsData["data"]["segments"][0]["teams"][1]["score"])
                        wonMaps = int(statsData["data"]["segments"][0]["teams"][teamVal]["score"])
                        lostMaps = totalMaps - wonMaps
                        
                        
                        tempStats[0]["Win"] += wonMaps
                        tempStats[0]["Loss"] += lostMaps

                        # BO3 2-0, BO5 3-0 & 3-1 + games
                        if (totalMaps <= 3):
                              tempStats[1]["Games"] += 1
                              if ((totalMaps - wonMaps) == 0):
                                    tempStats[1]["2-0"] += 1
                        else:
                              tempStats[2]["Games"] += 1
                              if ((totalMaps - wonMaps) == 0):
                                    tempStats[2]["3-0"] += 1
                              elif ((totalMaps - wonMaps) == 1):
                                    tempStats[2]["3-1"] += 1

                        # Round Wins/Lost by
                        for j in range(0, totalMaps):
                              totalRounds = int(statsData["data"]["segments"][0]["maps"][j]["score"]["team1"]) + int(statsData["data"]["segments"][0]["maps"][j]["score"]["team2"])

                              roundsWonBy = totalRounds - int(statsData["data"]["segments"][0]["maps"][j]["score"][team])
                              if (teamVal == 0):
                                    roundsLostBy = totalRounds - int(statsData["data"]["segments"][0]["maps"][j]["score"]["team1"])
                              else:
                                    roundsLostBy = totalRounds - int(statsData["data"]["segments"][0]["maps"][j]["score"]["team2"])

                              # Rounds won and lost by
                              if   (roundsWonBy  ==  0                      ):        tempStats[3]["WinBy13"]  += 1
                              elif (roundsWonBy  <=  3 and roundsWonBy >   0):        tempStats[3]["WinBy10"]  += 1
                              elif (roundsWonBy  <=  8 and roundsWonBy >   3):        tempStats[3]["WinBy5"]   += 1
                              elif (roundsLostBy == 0                       ):        tempStats[4]["LoseBy13"] += 1
                              elif (roundsLostBy <=  3 and roundsLostBy > 0 ):        tempStats[4]["LoseBy10"] += 1


                              time.sleep(2)


                              
            finaloutput[teamName] = tempStats



                        #statsData["data"]["segments"][0]["teams"][0/1] gives team info + winner/not + map wins
                        #statsData["data"]["segments"][0]["maps"][0/1/2] gives map info
                        #statsData["data"]["segments"][0]["maps"][0]["rounds"][0-23] gives individual round wins
                        

      statsFile.write(json.dumps(finaloutput))
      statsFile.close()