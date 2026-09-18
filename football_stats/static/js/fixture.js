// Search bar functionality
const metricSearch = document.getElementById("metric-search");
const metricRows = document.querySelectorAll(".unique-metric");

metricSearch.addEventListener("input", () => {
    const searchTerm = metricSearch.value.trim().toLowerCase();

    metricRows.forEach(row => {
        const metricName = row.querySelector(".metric-name").textContent.toLowerCase();

        row.hidden = !metricName.includes(searchTerm);
    });
});

// Toggle button for Pre-Match view
const roleLabel = document.querySelector('.mode-label[data-mode="role"]');
const overallLabel = document.querySelector('.mode-label[data-mode="overall"]');

const statisticsModeToggle = document.getElementById("statistics-mode-toggle");

const roleStatistics = document.getElementById("role-statistics");
const overallStatistics = document.getElementById("overall-statistics");

statisticsModeToggle.addEventListener("change", () => {
    // Change which statistics are displayed
    roleStatistics.hidden = statisticsModeToggle.checked;
    overallStatistics.hidden = !statisticsModeToggle.checked;

    // Update the labels' active state
    roleLabel.classList.toggle("active", !statisticsModeToggle.checked);
    overallLabel.classList.toggle("active", statisticsModeToggle.checked);
});


// Switching between view tabs
const fixtureTabs = document.querySelectorAll(".fixture-tab");
const fixtureViews = document.querySelectorAll(".fixture-view");
const statisticsModeControl = document.querySelector(".statistics-mode-toggle");

fixtureTabs.forEach(tab => {
    tab.addEventListener("click", () => {
        const selectedView = tab.dataset.view;

        statisticsModeControl.hidden = selectedView !== "pre-match";

        fixtureViews.forEach(view => {
            view.hidden = view.id !== `${selectedView}-view`;
        });

        fixtureTabs.forEach(tab => {
            tab.classList.remove("active");
        });

        tab.classList.add("active");
    });
});