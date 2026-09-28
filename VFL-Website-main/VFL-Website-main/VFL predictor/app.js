const RunButton = document.getElementById("RunButton");
const RankingsBox = document.getElementById("PlayerRankings");

RunButton.addEventListener("click", function () {

    const PlayerList = Object.entries(window.finalOutput);
    console.log(PlayerList);

    PlayerList.sort(function (a, b) {
        return b[1].PredictedScore - a[1].PredictedScore;
    });

    RankingsBox.innerHTML = `
        <div class="ranking-row ranking-header">
            <div>Rank</div>
            <div>Player</div>
            <div>Team</div>
            <div>Role</div>
            <div>Predicted Score</div>
        </div>
    `;

    PlayerList.forEach(function (player, index) {

        const PlayerName = player[0];
        const PlayerStats = player[1];

        RankingsBox.innerHTML += `
            <div class="ranking-row">
                <div>${index + 1}</div>
                <div>${PlayerName}</div>
                <div>${PlayerStats.Team}</div>
                <div>${PlayerStats.Role}</div>
                <div>${PlayerStats.PredictedScore}</div>
            </div>
        `;
    });
});