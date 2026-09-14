// Search result tabs
const resultsCompetitionTab = document.getElementById("results-competition-tab");
const resultsTeamTab = document.getElementById("results-team-tab");

// Search result sections
const competitionResults = document.querySelector(".search-results .competitions");
const teamResults = document.querySelector(".search-results .teams");

// Display the selected result category and hide the other
function showResults(elem) {
    competitionResults.hidden = true;
    teamResults.hidden = true;

    elem.hidden = false;
}

// Switch between result categories
resultsCompetitionTab.addEventListener(
    "click",
    () => showResults(competitionResults)
);

resultsTeamTab.addEventListener(
    "click",
    () => showResults(teamResults)
);