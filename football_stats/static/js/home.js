// Search result tabs
const resultsCountryTab = document.getElementById("results-country-tab");
const resultsCompetitionTab = document.getElementById("results-competition-tab");
const resultsTeamTab = document.getElementById("results-team-tab");

// Search result sections
const countryResults = document.querySelector(".search-results .countries");
const competitionResults = document.querySelector(".search-results .competitions");
const teamResults = document.querySelector(".search-results .teams");

// Display the selected result category and hide the others
function showResults(elem) {
    countryResults.hidden = true;
    competitionResults.hidden = true;
    teamResults.hidden = true;

    elem.hidden = false;
}

// Switch between result categories
resultsCountryTab.addEventListener(
    "click",
    () => showResults(countryResults)
);

resultsCompetitionTab.addEventListener(
    "click",
    () => showResults(competitionResults)
);

resultsTeamTab.addEventListener(
    "click",
    () => showResults(teamResults)
);