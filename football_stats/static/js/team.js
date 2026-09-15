// Moves the active class to the selected tab.
function setActiveTab(tabs, selectedTab) {
    tabs.forEach((tab) => {
        tab.classList.remove("active");
    });

    selectedTab.classList.add("active");
}


// Synchronizes all Statistics components with the current state.
function updateStatistics(
    statisticsBlocks,
    selectedLocation,
    selectedDirection,
    selectedView
) {
    statisticsBlocks.forEach((statisticsBlock) => {
        const locationTabs =
            statisticsBlock.querySelectorAll(".location-tab");

        const directionTabs =
            statisticsBlock.querySelectorAll(".direction-tab");

        const viewTabs =
            statisticsBlock.querySelectorAll(".statistics-view-tab");

        const statisticsPanels =
            statisticsBlock.querySelectorAll(".statistics-panel");

        const statisticsViews =
            statisticsBlock.querySelectorAll(".statistics-view");

        statisticsPanels.forEach((panel) => {
            panel.hidden = !(
                panel.dataset.location === selectedLocation &&
                panel.dataset.direction === selectedDirection
            );
        });

        statisticsViews.forEach((view) => {
            view.hidden = view.dataset.view !== selectedView;
        });

        locationTabs.forEach((tab) => {
            tab.classList.toggle(
                "active",
                tab.dataset.location === selectedLocation
            );
        });

        directionTabs.forEach((tab) => {
            tab.classList.toggle(
                "active",
                tab.dataset.direction === selectedDirection
            );
        });

        viewTabs.forEach((tab) => {
            tab.classList.toggle(
                "active",
                tab.dataset.view === selectedView
            );
        });
    });
}


// Competition tabs
const competitionTabs = document.querySelectorAll(".competition-tab");
const competitionPanels = document.querySelectorAll(".competition-panel");

competitionTabs.forEach((tab) => {
    tab.addEventListener("click", () => {
        const selectedCompetition = tab.dataset.competition;

        setActiveTab(competitionTabs, tab);

        competitionPanels.forEach((panel) => {
            panel.hidden =
                panel.dataset.competition !== selectedCompetition;
        });
    });
});
setActiveTab(competitionTabs, competitionTabs[0]);


// Stage tabs inside individual competitions
competitionPanels.forEach((competitionPanel) => {
    const stageTabs = competitionPanel.querySelectorAll(".stage-tab");
    const stagePanels = competitionPanel.querySelectorAll(".stage-panel");

    stageTabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            const selectedStage = tab.dataset.stage;

            setActiveTab(stageTabs, tab);

            stagePanels.forEach((panel) => {
                panel.hidden = panel.dataset.stage !== selectedStage;
            });
        });
    });

    if (stageTabs.length > 0) {
        setActiveTab(stageTabs, stageTabs[0]);
    };
});


// Statistics controls
const statisticsBlocks = document.querySelectorAll(".statistics");

let selectedLocation = "overall";
let selectedDirection = "for";
let selectedView = "distribution";

statisticsBlocks.forEach((statisticsBlock) => {
    const locationTabs =
        statisticsBlock.querySelectorAll(".location-tab");

    const directionTabs =
        statisticsBlock.querySelectorAll(".direction-tab");

    const viewTabs =
        statisticsBlock.querySelectorAll(".statistics-view-tab");

    locationTabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            selectedLocation = tab.dataset.location;

            updateStatistics(
                statisticsBlocks,
                selectedLocation,
                selectedDirection,
                selectedView
            );
        });
    });

    directionTabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            selectedDirection = tab.dataset.direction;

            updateStatistics(
                statisticsBlocks,
                selectedLocation,
                selectedDirection,
                selectedView
            );
        });
    });

    viewTabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            selectedView = tab.dataset.view;

            updateStatistics(
                statisticsBlocks,
                selectedLocation,
                selectedDirection,
                selectedView
            );
        });
    });
});

updateStatistics(
    statisticsBlocks,
    selectedLocation,
    selectedDirection,
    selectedView
);


// All Competitions filters
const competitionCheckboxes =
    document.querySelectorAll(".competition-checkbox");

const selectAllCompetitions =
    document.getElementById("select-all-competitions");

const deselectAllCompetitions =
    document.getElementById("deselect-all-competitions");

selectAllCompetitions.addEventListener("click", () => {
    competitionCheckboxes.forEach((checkbox) => {
        checkbox.checked = true;
    });
});

deselectAllCompetitions.addEventListener("click", () => {
    competitionCheckboxes.forEach((checkbox) => {
        checkbox.checked = false;
    });
});