import ast
from collections import defaultdict
import json
import copy

# WANTS FROM DATA
#       MAP WIN/LOSS                                    DONE
#       BO3: NUMBER, 2-0 %                              DONE
#       BO5: NUMBER, 3-0 %, 3-1 %                       DONE
#       SHUTOUT %                                       DONE
#       WIN BY 13 ROUNDS %, 10 ROUNDS %, 5 ROUNDS %
#       LOSE BY 13 ROUNDS %, 10 ROUNDS %

with open ('VLR DATA\Data Outputs\MatchIDResponse.json', 'r') as file:
    matchData = ast.literal_eval(file.read())
file.close()

with open ('VLR DATA\Data Outputs\orgIDs', 'r') as file2:
    getTeamID = ast.literal_eval(file2.read())
file.close()

finaloutput = defaultdict(dict)
for (teamName, teamStats) in matchData.items():
    mapsNum = teamStats[0]["Win"] + teamStats[0]["Loss"]

    mapWinPercent = round(teamStats[0]["Win"] / mapsNum, 3)

    bo3ShutoutPercent = round((teamStats[1]["2-0"] / teamStats[1]["Games"]), 3)

    if (teamStats[2]["Games"] == 0):
        bo5ShutoutPercent = 0
        bo5_31Percent = 0
    else:
        bo5ShutoutPercent = round((teamStats[2]["3-0"] / teamStats[2]["Games"]), 3)
        bo5_31Percent = round((teamStats[2]["3-1"] / teamStats[2]["Games"]), 3)

    shutoutGamesPercent = round((teamStats[1]["2-0"] + teamStats[2]["3-0"]) / (teamStats[1]["Games"] + teamStats[2]["Games"]), 3)

    