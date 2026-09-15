from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    data = {
        "countries": {
            1: {"name": "Italy"},
            2: {"name": "Spain"},
            3: {"name": "Romania"},
        },

        "teams": {
            1: {
                "name": "AC Milan",
                "type": "club",
                "country_id": 1
            },
            2: {
                "name": "FC Barcelona",
                "type": "club",
                "country_id": 2
            },
            3: {
                "name": "Italy",
                "type": "national",
                "country_id": 1
            },
            4: {
                "name": "Spain",
                "type": "national",
                "country_id": 2
            },
            5: {
                "name": "FCSB",
                "type": "club",
                "country_id": 3
            },
            6: {
                "name": "Romania",
                "type": "national",
                "country_id": 3
            }
        },

        "competitions": {
            1: {
                "name": "Serie A",
                "scope": "domestic",
                "team_type": "club",
                "country_id": 1
            },
            2: {
                "name": "La Liga",
                "scope": "domestic",
                "team_type": "club",
                "country_id": 2
            },
            3: {
                "name": "Liga I",
                "scope": "domestic",
                "team_type": "club",
                "country_id": 3
            },
            4: {
                "name": "UEFA Champions League",
                "scope": "international",
                "team_type": "club",
                "country_id": None
            },
            5: {
                "name": "FIFA World Cup",
                "scope": "international",
                "team_type": "national",
                "country_id": None
            }
        },

        "competition_teams": {
            1: {1},
            2: {2},
            3: {5},
            4: {1, 2, 5},
            5: {3, 4, 6}
        }
    }

    favorites = {
        "countries": {1, 3},
        "competitions": {1, 4},
        "teams": {1, 6}
    }

    countries = [
        country["name"]
        for country in data["countries"].values()
    ]

    competitions = [
        competition["name"]
        for competition in data["competitions"].values()
    ]

    teams = [
        team["name"]
        for team in data["teams"].values()
    ]

    favorite_countries = [
        data["countries"][country_id]["name"]
        for country_id in favorites["countries"]
    ]

    favorite_competitions = [
        data["competitions"][competition_id]["name"]
        for competition_id in favorites["competitions"]
    ]

    favorite_teams = [
        data["teams"][team_id]["name"]
        for team_id in favorites["teams"]
    ]

    return render_template(
        "home.html",
        countries=countries,
        competitions=competitions,
        teams=teams,
        favorite_countries=favorite_countries,
        favorite_competitions=favorite_competitions,
        favorite_teams=favorite_teams
    )


@app.route("/country/<int:country_id>")
def country(country_id):
    country = {
        "id": country_id,
        "name": "Romania"
    }

    competitions = [
        "Liga I",
        "Liga II",
        "Cupa României"
    ]

    teams = [
        "FCSB",
        "Rapid București",
        "CFR Cluj"
    ]

    favorite_countries = ["Romania", "Italy"]
    favorite_competitions = ["Liga I", "Serie A"]
    favorite_teams = ["FCSB", "AC Milan"]

    return render_template(
        "country.html",
        country=country,
        competitions=competitions,
        teams=teams,
        favorite_countries=favorite_countries,
        favorite_competitions=favorite_competitions,
        favorite_teams=favorite_teams
    )


@app.route("/competition/champions-league")
def competition():
    competition = {
        "id": 1,
        "name": "Champions League",
        "category": "hybrid",
        "stages": [
            {
                "name": "Qualifying",
                "structure": "knockout",
                "teams": [
                    "Team A",
                    "Team B",
                    "Team C",
                    "Team D"
                ],
                "rounds": [
                    {
                        "name": "First Qualifying Round",
                        "fixtures": [
                            {
                                "home": "Team A",
                                "away": "Team B"
                            },
                            {
                                "home": "Team C",
                                "away": "Team D"
                            }
                        ]
                    },
                    {
                        "name": "Second Qualifying Round",
                        "fixtures": [
                            {
                                "home": "Winner of First Qualifying Round Match 1",
                                "away": "Winner of First Qualifying Round Match 2"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "League Phase",
                "structure": "league",
                "standings": [
                    "Team A",
                    "Team B",
                    "Team C",
                    "Team D"
                ],
                "fixtures": [
                    {
                        "home": "Team A",
                        "away": "Team C"
                    },
                    {
                        "home": "Team B",
                        "away": "Team D"
                    }
                ]
            },
            {
                "name": "Knockout Phase",
                "structure": "knockout",
                "teams": [
                    "Team A",
                    "Team B"
                ],
                "rounds": [
                    {
                        "name": "Round of 16",
                        "fixtures": [
                            {
                                "home": "Team A",
                                "away": "Team B"
                            }
                        ]
                    },
                    {
                        "name": "Quarter-finals",
                        "fixtures": [
                            {
                                "home": "Winner of Round of 16 Match 1",
                                "away": "Winner of Round of 16 Match 2"
                            }
                        ]
                    },
                    {
                        "name": "Semi-finals",
                        "fixtures": [
                            {
                                "home": "Winner of Quarter-finals Match 1",
                                "away": "Winner of Quarter-finals Match 2"
                            }
                        ]
                    },
                    {
                        "name": "Final",
                        "fixtures": [
                            {
                                "home": "Winner of Semi-finals Match 1",
                                "away": "Winner of Semi-finals Match 2"
                            }
                        ]
                    }
                ]
            }
        ]
    }

    favorite_countries = ["Romania", "Italy"]
    favorite_competitions = ["Champions League", "Serie A"]
    favorite_teams = ["FCSB", "AC Milan"]

    return render_template(
        "competition.html",
        competition=competition,
        favorite_countries=favorite_countries,
        favorite_competitions=favorite_competitions,
        favorite_teams=favorite_teams
    )


@app.route("/competition/liga-i")
def liga_i():
    competition = {
        "id": 2,
        "name": "Liga I",
        "category": "league",
        "stages": [
            {
                "name": "Regular Season",
                "structure": "league",
                "standings": [
                    "FCSB",
                    "CFR Cluj",
                    "Rapid București",
                    "Universitatea Craiova"
                ],
                "fixtures": [
                    {
                        "home": "FCSB",
                        "away": "CFR Cluj"
                    },
                    {
                        "home": "Rapid București",
                        "away": "Universitatea Craiova"
                    }
                ]
            },
            {
                "name": "Play-Off / Play-Out",
                "structure": "league",
                "groups": [
                    {
                        "name": "Play-Off",
                        "standings": [
                            "FCSB",
                            "CFR Cluj"
                        ],
                        "fixtures": [
                            {
                                "home": "FCSB",
                                "away": "CFR Cluj"
                            }
                        ]
                    },
                    {
                        "name": "Play-Out",
                        "standings": [
                            "Rapid București",
                            "Universitatea Craiova"
                        ],
                        "fixtures": [
                            {
                                "home": "Rapid București",
                                "away": "Universitatea Craiova"
                            }
                        ]
                    }
                ]
            }
        ]
    }

    favorite_countries = ["Romania", "Italy"]
    favorite_competitions = ["Champions League", "Serie A"]
    favorite_teams = ["FCSB", "AC Milan"]

    return render_template(
        "competition.html",
        competition=competition,
        favorite_countries=favorite_countries,
        favorite_competitions=favorite_competitions,
        favorite_teams=favorite_teams
    )

def mock_statistics():
    return {
        "overall": {
            "for": [
                {
                    "criteria": "Goals",
                    "low_5": 0.8,
                    "average": 1.9,
                    "high_5": 3.2,
                    "last_7": 2.0,
                    "last_5": 2.2,
                    "last_3": 2.7
                },
                {
                    "criteria": "Shots",
                    "low_5": 7.4,
                    "average": 12.1,
                    "high_5": 17.2,
                    "last_7": 12.8,
                    "last_5": 13.4,
                    "last_3": 14.0
                },
                {
                    "criteria": "Corners",
                    "low_5": 2.6,
                    "average": 5.1,
                    "high_5": 7.8,
                    "last_7": 5.4,
                    "last_5": 5.8,
                    "last_3": 6.3
                }
            ],

            "against": [
                {
                    "criteria": "Goals",
                    "low_5": 0.2,
                    "average": 1.1,
                    "high_5": 2.4,
                    "last_7": 1.0,
                    "last_5": 0.8,
                    "last_3": 0.7
                },
                {
                    "criteria": "Shots",
                    "low_5": 5.8,
                    "average": 9.7,
                    "high_5": 14.1,
                    "last_7": 9.2,
                    "last_5": 8.8,
                    "last_3": 8.3
                },
                {
                    "criteria": "Corners",
                    "low_5": 1.8,
                    "average": 4.2,
                    "high_5": 6.6,
                    "last_7": 4.0,
                    "last_5": 3.8,
                    "last_3": 3.7
                }
            ]
        },

        "home": {
            "for": [
                {
                    "criteria": "Goals",
                    "low_5": 1.0,
                    "average": 2.2,
                    "high_5": 3.6,
                    "last_7": 2.3,
                    "last_5": 2.4,
                    "last_3": 3.0
                }
            ],
            "against": [
                {
                    "criteria": "Goals",
                    "low_5": 0.0,
                    "average": 0.8,
                    "high_5": 1.8,
                    "last_7": 0.7,
                    "last_5": 0.6,
                    "last_3": 0.3
                }
            ]
        },

        "away": {
            "for": [
                {
                    "criteria": "Goals",
                    "low_5": 0.6,
                    "average": 1.6,
                    "high_5": 2.8,
                    "last_7": 1.7,
                    "last_5": 1.8,
                    "last_3": 2.0
                }
            ],
            "against": [
                {
                    "criteria": "Goals",
                    "low_5": 0.4,
                    "average": 1.4,
                    "high_5": 2.8,
                    "last_7": 1.3,
                    "last_5": 1.2,
                    "last_3": 1.0
                }
            ]
        }
    }

@app.route("/team/fcsb")
def team():
    team = {
        "id": 1,
        "name": "FCSB",

        "all_competitions": {
            "statistics": mock_statistics()
        },

        "competitions": [
            {
                "name": "Liga I",
                "stages": [
                    {
                        "name": "Regular Season",
                        "statistics": mock_statistics()
                    },
                    {
                        "name": "Play-Off",
                        "statistics": mock_statistics()
                    }
                ]
            },
            {
                "name": "Champions League",
                "stages": [
                    {
                        "name": "League Phase",
                        "statistics": mock_statistics()
                    },
                    {
                        "name": "Knockout Phase",
                        "statistics": mock_statistics()
                    }
                ]
            },
            {
                "name": "Cupa României",
                "stages": [
                    {
                        "name": "Round of 32",
                        "statistics": mock_statistics()
                    },
                    {
                        "name": "Round of 16",
                        "statistics": mock_statistics()
                    },
                    {
                        "name": "Quarter-finals",
                        "statistics": mock_statistics()
                    }
                ]
            }
        ]
    }

    favorite_countries = ["Romania", "Italy"]
    favorite_competitions = ["Champions League", "Serie A"]
    favorite_teams = ["FCSB", "AC Milan"]

    return render_template(
        "team.html",
        team=team,
        favorite_countries=favorite_countries,
        favorite_competitions=favorite_competitions,
        favorite_teams=favorite_teams
    )