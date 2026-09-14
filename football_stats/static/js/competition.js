// Stage tabs
const stageTabs = document.querySelectorAll(".stage-tab");
const stages = document.querySelectorAll(".stage");

// Switch between competition stages
stageTabs.forEach((tab) => {
    tab.addEventListener("click", () => {
        const selectedStage = tab.dataset.stage;

        stages.forEach((stage) => {
            stage.hidden = stage.dataset.stage !== selectedStage;
        });
    });
});


// Content tabs inside each stage
stages.forEach((stage) => {
    const contentTabs = stage.querySelectorAll(".content-tab");
    const contentSections = stage.querySelectorAll(".stage-content");

    contentTabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            const selectedContent = tab.dataset.content;

            contentSections.forEach((section) => {
                section.hidden = !section.classList.contains(selectedContent);
            });
        });
    });
});


// Round tabs inside knockout stages
const roundsSections = document.querySelectorAll(".rounds");

roundsSections.forEach((roundsSection) => {
    const roundTabs = roundsSection.querySelectorAll(".round-tab");
    const rounds = roundsSection.querySelectorAll(".round");

    roundTabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            const selectedRound = tab.dataset.round;

            rounds.forEach((round) => {
                round.hidden = round.dataset.round !== selectedRound;
            });
        });
    });
});

// Group tabs inside league stages
const groupedStages = document.querySelectorAll(".groups");

groupedStages.forEach((groupsContainer) => {
    const groupTabs = groupsContainer.parentElement.querySelectorAll(".group-tab");
    const groups = groupsContainer.querySelectorAll(".group");

    groupTabs.forEach((tab) => {
        tab.addEventListener("click", () => {
            const selectedGroup = tab.dataset.group;

            groups.forEach((group) => {
                const isSelected = group.dataset.group === selectedGroup;

                group.hidden = !isSelected;

                if (isSelected) {
                    const standings = group.querySelector(".standings");
                    const fixtures = group.querySelector(".fixtures");

                    standings.hidden = false;
                    fixtures.hidden = true;
                }
            });
        });
    });
});