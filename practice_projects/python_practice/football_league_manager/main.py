from enum import Enum, IntEnum
import enums as e


class Player:
    def __init__(self, name, player_id, position:e.Position):
        self.name = name
        self.player_id = player_id
        self.position = position
        self.goals = 0
        self.yellow_cards = 0
        self.red_cards = 0

    def is_suspended(self):
        if self.yellow_cards >= 2 or self.red_cards >= 1:
            return True
        
    def __str__(self):
        suspended = "Yes" if self.is_suspended else "No"
        return (f"Name: {self.name} | "
                f"Player ID: {self.player_id} | "
                f"Position: {self.position.value} | "
                f"Goals: {self.goals} | "
                f"Suspended: {suspended} | "
                )
    

class Club:
    def __init__(self, name, club_id):
        self.name = name
        self.club_id = club_id
        self.players = []
        self.form_list = []

    @property
    def points(self):
        self.points = 0
        for results in self.form_list:
            self.points += results.value 
 
    @property
    def goals_scored(self)->int:
        pass

    @property
    def clean_sheets(self)->int:
        pass

    def sign_player(self, player:Player):
        self.players.append(player)
        print(f"  ✅ {player.name} signed by {self.name} "
              f"({player.position.value}, shirt #{player.position.typical_shirt_number})")


    def add_result(self):
        self.form_list.append(e.Form.name)

    def __str__(self):
        return (f"Club : {self.name} | "
                f"Club ID : {self.club_id} | "
                f"Players : {self.player_list} | "
                f"Recent Form : {self.form_list} | "
                f"Points : {self.points} | "
     )



class Match:
    def __init__(self, match_id, home_club:Club, away_club:Club, status:e.MatchStatus.SCHEDULED):
        self.match_id = match_id
        self.home_club = home_club
        self.away_club = away_club
        self.status = status
        self.home_score = 0
        self.away_score = 0

    def kick_off(self):
        self.status = e.MatchStatus.LIVE

    def score_goal(self, club):
        if club == self.home_club:
            self.home_score += 1
        elif club == self.away_club:
            self.away_club += 1

    def issue_card(self, player:Player, colour:e.CardType):
        if colour == e.CardType.RED:
            player.red_cards += 1
        elif colour == e.CardType.YELLOW:
            player.yellow_cards += 1

    def full_time(self):
        self.status = e.MatchStatus.COMPLETED

    def __str__(self):
        return (f"Match ID : {self.match_id} | "
                f"Home CLub : {self.home_club} | "
                f"Away Club : {self.away_club} | "
                f"Home Score : {self.home_score} | "
                f"Away Score : {self.away_score} | ")
        

#Step 6 — Build the League class
#The controller. Holds clubs and matches. Methods: register_club, schedule_match, play_match, and standings_report.

class League:
    def __init__(self, name):
        self.name = name
        self._club: dict[int, Club] = {}
        self._match: dict[int, Match] = {}
        self._next_match_id = 1
    
    def register_club(self, club:Club):
        self._club[club.club_id] = club
        print(f"  ✅ {club.name} registered to {self.name}.")

    def schedule_match(self):
        Match(self.home_club, self.away_club, self.status)

    def play_match(self):
        pass

    def standings_report(self):
        pass



if __name__ == "__main__":
    league = League("Eredivisie")

    # Register clubs
    print("\n── Registering Clubs ──")
    ajax    = Club("Ajax",    club_id=1)
    psv     = Club("PSV",     club_id=2)
    feyenoord = Club("Feyenoord", club_id=3)
    for club in (ajax, psv, feyenoord):
        league.register_club(club)

    # Sign players
    print("\n── Signing Players ──")
    ajax.sign_player(Player("Remko Pasveer",  1, e.Position.GOALKEEPER))
    ajax.sign_player(Player("Devyne Rensch",  2, e.Position.DEFENDER))
    ajax.sign_player(Player("Kenneth Taylor", 3, e.Position.MIDFIELDER))
    ajax.sign_player(Player("Brian Brobbey",  4, e.Position.FORWARD))

    psv.sign_player(Player("Walter Benitez",  5, e.Position.GOALKEEPER))
    psv.sign_player(Player("Olivier Boscagli",6, e.Position.DEFENDER))
    psv.sign_player(Player("Joey Veerman",    7, e.Position.MIDFIELDER))
    psv.sign_player(Player("Luuk de Jong",    8, e.Position.FORWARD))

    feyenoord.sign_player(Player("Timon Wellenreuther", 9,  e.Position.GOALKEEPER))
    feyenoord.sign_player(Player("Bart Nieuwkoop",      10, e.Position.DEFENDER))
    feyenoord.sign_player(Player("Quinten Timber",      11, e.Position.MIDFIELDER))
    feyenoord.sign_player(Player("Santiago Gimenez",    12, e.Position.FORWARD))

    # Schedule matches
   # print("\n── Scheduling Matches ──")
   # m1 = league.schedule_match(1, 2)   # Ajax vs PSV
   # m2 = league.schedule_match(3, 1)   # Feyenoord vs Ajax
   # m3 = league.schedule_match(2, 3)   # PSV vs Feyenoord

    # Play Match 1: Ajax vs PSV
    #print("\n── Match 1: Ajax vs PSV ──")
    #m1.kick_off()
    #m1.score_goal(ajax, 4)    # Brobbey scores
    #m1.score_goal(psv,  8)    # de Jong scores
    #m1.issue_card(psv,  6, CardType.YELLOW)   # Boscagli booked
    #m1.score_goal(ajax, 4)    # Brobbey scores again
    #m1.issue_card(ajax, 3, CardType.YELLOW)   # Taylor booked
    #m1.full_time()

    # Play Match 2: Feyenoord vs Ajax
    #print("\n── Match 2: Feyenoord vs Ajax ──")
    #m2.kick_off()
    #m2.score_goal(feyenoord, 12)   # Gimenez scores
    #m2.score_goal(feyenoord, 12)   # Gimenez scores again
    #m2.issue_card(ajax, 2, CardType.RED)      # Rensch sent off
    #m2.full_time()

    # Play Match 3: PSV vs Feyenoord
    #print("\n── Match 3: PSV vs Feyenoord ──")
    #m3.kick_off()
    #m3.score_goal(psv, 8)          # de Jong scores
    #m3.score_goal(psv, 7)          # Veerman scores
    #m3.score_goal(feyenoord, 11)   # Timber scores
    #m3.full_time()

    # Final standings
    #league.standings_report()