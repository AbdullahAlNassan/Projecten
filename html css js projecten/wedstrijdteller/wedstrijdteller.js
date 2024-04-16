let game = {
    team1punten: 0,
    team2punten: 0,
    serving: 0,
    lastService: 0,
    lastScored: 0,
    setTeller: 1, 
    setScores: [] 
};
 
inputTeam1.value = '';
inputTeam2.value = '';
 
function updatescreen() {
    counterTeam2.classList.remove("serving");
    counterTeam1.classList.remove("serving");
    if (game.serving == 1) {
        counterTeam1.classList.add("serving");
    } else {
        counterTeam2.classList.add("serving");
    }
 
    counterTeam1.innerText = game.team1punten;
    counterTeam2.innerText = game.team2punten;
 
    document.getElementById("setUitslagen").innerText = `Set Uitslagen: ${game.setScores.join(', ')}`; // Voeg dit toe aan je HTML
}
 
function start(event) {
    console.log('You pressed start!');
    if (nameTeam1.innerText == '' || nameTeam2.innerText == '') {
        alert("Er mist een naam!")
        return;
    };
 
    if (!servingTeam1.checked && !servingTeam2.checked) {
        alert("Wie moet er beginnen");
        return;
    };
 
    input_teams.style.display = "none";
    counterTeam1.disabled = false;
    counterTeam2.disabled = false;
 
    game.serving = 2;
    if (servingTeam1.checked) {
        game.serving = 1;
    };
 
    updatescreen();
}
 
function count(event) {
    game.lastService = game.serving
    if (this.id == 'counterTeam1') {
        game.team1punten += 1;
        game.serving = 1;
        game.lastScored = 1;
    } else {
        game.team2punten += 1;
        game.serving = 2;
        game.lastScored = 2;
    }

    if (game.team1punten >= 25 || game.team2punten >= 25) {
        if (Math.abs(game.team1punten - game.team2punten) >= 2) { 
            game.setScores.push(`${game.team1punten}-${game.team2punten}`);
            game.team1punten = 0;
            game.team2punten = 0;

            // Increment setTeller
            game.setTeller++;

            // Check if any team has won the match
            
        }
    }

    undoButton.disabled = false;
    updatescreen();
    checkMatchWinner();
}

 
function displayNames(event) {
    nameTeam1.innerText = inputTeam1.value;
    nameTeam2.innerText = inputTeam2.value;
}
 
function undoLastPoint(event) {
    undoButton.disabled = true;
    if (game.lastScored == 1) {
        game.team1punten -= 1;
        game.serving = 2;
    } else {
        game.team2punten -= 1;
        game.serving = 1;
    }
    updatescreen();
}
 
function checkMatchWinner() {
    if (game.setTeller === 3) { 
        undoButton.disabled = true;
        counterTeam1.disabled = true;
        counterTeam2.disabled = true;
        alert(`${nameTeam1.innerText} heeft de wedstrijd gewonnen!`);
    }
}
 
startButton.addEventListener('click', start);
counterTeam1.addEventListener('click', count);
counterTeam2.addEventListener('click', count);
inputTeam1.addEventListener('change', displayNames);
inputTeam2.addEventListener('change', displayNames);
undoButton.addEventListener('click', undoLastPoint);
 
undoButton.disabled = true;
counterTeam1.disabled = true;
counterTeam2.disabled = true;
 