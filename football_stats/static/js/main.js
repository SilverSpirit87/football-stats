const countriesTab = document.getElementById("country-tab");
const competitionsTab = document.getElementById("competition-tab");
const teamsTab = document.getElementById("team-tab");

const countriesFavorites = document.querySelector(".favorites-list.countries");
const competitionsFavorites = document.querySelector(".favorites-list.competitions");
const teamsFavorites = document.querySelector(".favorites-list.teams");

function toggleFavorites(elem) {
    countriesFavorites.hidden = true;
    competitionsFavorites.hidden = true;
    teamsFavorites.hidden = true;

    elem.hidden = false;
}

countriesTab.addEventListener("click", () => toggleFavorites(countriesFavorites));
competitionsTab.addEventListener("click", () => toggleFavorites(competitionsFavorites));
teamsTab.addEventListener("click", () => toggleFavorites(teamsFavorites));