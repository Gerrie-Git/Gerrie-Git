⚽ Intermediate Python Practice Project: Football League Manager

📋 Project Overview
Build a Football League Management System that manages clubs, players, matches, and standings. Enums drive every state and category in the system, while classes handle all the logic. You'll practice:

Enum & IntEnum — for player position, match status, form, and card types
Enum methods & properties — adding behaviour directly onto enum members
Classes — for Player, Club, Match, and League objects
Dataclasses — for clean data modelling
Class relationships — clubs have players, matches have clubs, league tracks everything
Dunder methods — __str__, __repr__, __eq__


🗺️ Step-by-Step Plan
Step 1 — Set up Enums
Define Position (GOALKEEPER, DEFENDER, MIDFIELDER, FORWARD), MatchStatus (SCHEDULED, LIVE, COMPLETED, POSTPONED), CardType (YELLOW, RED), and Form (using IntEnum for WIN, DRAW, LOSS so points can be calculated directly).
Step 2 — Add methods to Enums
Give Position a typical_shirt_number property. Give Form a points property (WIN=3, DRAW=1, LOSS=0) and a label property. Give MatchStatus a can_advance property.
Step 3 — Build the Player dataclass
Attributes: name, player_id, position (a Position enum), goals, yellow_cards, red_cards. Add a property is_suspended (2+ yellow cards or 1 red) and __str__.
Step 4 — Build the Club class
Attributes: name, club_id, a list of players, and a list of form (recent Form results). Add properties: points, goals_scored, clean_sheets possible, and a method add_result. Add __str__.
Step 5 — Build the Match class
Attributes: match_id, home_club, away_club, status (a MatchStatus enum), home_score, away_score. Methods: kick_off, score_goal, issue_card, full_time, and __str__.
Step 6 — Build the League class
The controller. Holds clubs and matches. Methods: register_club, schedule_match, play_match, and standings_report.
Step 7 — Wire it all together
A demo that registers clubs, signs players, schedules matches, plays them out with goals and cards, and prints the full league standings.