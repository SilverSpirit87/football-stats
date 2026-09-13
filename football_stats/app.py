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