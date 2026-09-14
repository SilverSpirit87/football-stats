// Favorites category tabs
const favoriteCountryTab = document.getElementById("country-tab");
const favoriteCompetitionTab = document.getElementById("competition-tab");
const favoriteTeamTab = document.getElementById("team-tab");

// Favorites category lists
const favoriteCountries = document.querySelector(".favorites-list.countries");
const favoriteCompetitions = document.querySelector(".favorites-list.competitions");
const favoriteTeams = document.querySelector(".favorites-list.teams");

// Favorites collapse/expand elements
const favoritesToggle = document.getElementById("favorites-toggle");
const favoritesContent = document.querySelector(".favorites-content");

// Display the selected Favorites category and hide the others
function showFavorites(elem) {
    favoriteCountries.hidden = true;
    favoriteCompetitions.hidden = true;
    favoriteTeams.hidden = true;

    elem.hidden = false;
}

// Switch between Favorites categories
favoriteCountryTab.addEventListener(
    "click",
    () => showFavorites(favoriteCountries)
);

favoriteCompetitionTab.addEventListener(
    "click",
    () => showFavorites(favoriteCompetitions)
);

favoriteTeamTab.addEventListener(
    "click",
    () => showFavorites(favoriteTeams)
);

// Home has no Favorites toggle because its Favorites panel is always expanded.
// On other pages, clicking the Favorites heading expands/collapses the panel.
if (favoritesToggle) {
    favoritesToggle.addEventListener("click", () => {
        favoritesContent.hidden = !favoritesContent.hidden;
    });
}