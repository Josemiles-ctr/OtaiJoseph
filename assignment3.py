# match_results={
# 	"Home_goals" : int,
# 	"Away_goals" : int	
# }
# Detetmining Winnig team
def get_winner(home_goals, away_goals):
	winner={}
	if home_goals > away_goals:
		winner={
			"winning_team": "Home",
			"points": 3
		}
	elif away_goals > home_goals:
		winner={
			"winning_team": "Away",
			"points": 3
		}
	else:
		winner={
			"winning_team": None,
			"points": 1
		}
	return winner
# Testing
# print(get_winner(2, 2))

# Returning compact match results
def format_results(match):
	match_outcome={}
	winner=get_winner(match["Home_goals"], match["Away_goals"])
	if winner["winning_team"]=="Home":
		match_outcome={
			"Home":{
				"goals": match["Home_goals"],
				"points": 3
			},
			"Away":{
				"goals": match["Away_goals"],
				"points": 0
			}
		}
	elif winner["winning_team"]=="Away":
		match_outcome={
			"Home":{
				"goals":match["Home_goals"],
				"points": 0
			},
			"Away":{
				"goals": match["Away_goals"],
				"points": 3
			}
		}
	else:
		match_outcome={
			"Home":{
				"goals":match["Home_goals"],
				"points": 1
			},
			"Away":{
				"goals": match["Away_goals"],
				"points": 1
			}
		}
	return match_outcome
	
# Testing
# morrocco={
# 	"Home_goals":3,
# 	"Away_goals":3
# }
# results= format_results(morrocco)
# print(results)
fixture={
	"match1":["England", "Uganda"],
	"match2" :["Uganda", "Ghana"],
	"match3":["Ghana", "England"]
}

# Creating a group stage fixture
def make_group_stage_fixture(teams):
	if len(teams)!=3:
		raise ValueError("Expects only three teams")
	
	fixture={
		"match1":[teams[0], teams[1]],
		"match2":[teams[1], teams[2]],
		"mach3" :[teams[2], teams[0]]
	}
	return fixture
	

def get_group_stage_results(fixture):
	results={}
	for matches,index in fixture:
		for team in matches:
			results["match{index+1}"][team]= int(input("Enter the goles of team {team[0]}"))
		pass
		
# Fixture Results structure
fixture_results={
	"match1":{
		fixture["match1"][0]: int,
		fixture["match1"][1]:int
	},
	"match2":{
		fixture["match1"][0]: int,
		fixture["match1"][1]:int
	},
	"match3":{
		fixture["match1"][0]: int,
		fixture["match1"][1]:int
	},
	}
	
def group_stage_results(fixture):
	group_stage_results={
		"match1": {
			"Home_goals": int,
			"Away_goals": int
		},
		"match2": {
			"Home_goals": int,
			"Away_goals": int
		},
		"match3": {
			"Home_goals": int,
			"Away_goals": int
		}
	}
	for match in fixture:
		fixture_results={}
		home_team_goals=int(input("Enter Home team goals : "))
		away_team_goals=int(input("Enter Away team goals : "))
		fixture_results[match]={
			fixture[match][0]: home_team_goals,
		    fixture[match][1]:away_team_goals
		}
		group_stage_results[match]=fixture_results
		
	return group_stage_results

# Team performance attributes
team_stats = {
    "morale": 50,
    "injuries": 0,
    "strength": 50
}

# Pre-tournament preparation phase
def pre_tournament_preparation():
    print("\n=== PRE-TOURNAMENT PREPARATION ===")
    preparation_complete = False
    while not preparation_complete:
        print(f"\nCurrent Team Status:")
        print(f"Morale: {team_stats['morale']}, Injuries: {team_stats['injuries']}, Strength: {team_stats['strength']}")
        
        print("\nPreparation Options:")
        print("1. Training Session")
        print("2. Friendly Match")
        print("3. Recovery Session")
        print("4. Finish Preparation")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            # Training increases strength
            team_stats["strength"] += 10
            team_stats["morale"] += 5
            print("Training completed! Strength +10, Morale +5")
            pass  # Placeholder for advanced training features
        elif choice == "2":
            # Friendly match affects morale and injuries
            result = input("Did you win the friendly? (y/n): ").lower()
            if result == "y":
                team_stats["morale"] += 10
                print("Friendly win! Morale +10")
            else:
                team_stats["morale"] -= 5
                print("Friendly loss! Morale -5")
        elif choice == "3":
            # Recovery reduces injuries
            team_stats["injuries"] = max(0, team_stats["injuries"] - 2)
            team_stats["morale"] += 3
            print("Recovery completed! Injuries reduced, Morale +3")
            pass  # Placeholder for medical staff features
        elif choice == "4":
            preparation_complete = True
            print("Preparation phase complete!")
        else:
            print("Invalid choice, try again.")
            continue  # Skip to next iteration for invalid input

# Group stage simulation
def group_stage_simulation(teams):
    print("\n=== GROUP STAGE ===")
    points = {team: 0 for team in teams}
    
    # Match pairings: team0 vs team1, team1 vs team2, team2 vs team0
    match_pairings = [
        (teams[0], teams[1]),
        (teams[1], teams[2]),
        (teams[2], teams[0])
    ]
    
    for i, (home_team, away_team) in enumerate(match_pairings):
        print(f"\nMatch {i+1}: {home_team} vs {away_team}")
        home_goals = int(input(f"Goals scored by {home_team}: "))
        away_goals = int(input(f"Goals scored by {away_team}: "))
        
        # Apply team stats modifiers
        if team_stats["strength"] >= 60:
            home_goals += 1
        if team_stats["morale"] < 30:
            home_goals = max(0, home_goals - 1)
        
        if home_goals > away_goals:
            points[home_team] += 3
            print(f"{home_team} wins!")
        elif away_goals > home_goals:
            points[away_team] += 3
            print(f"{away_team} wins!")
        else:
            points[home_team] += 1
            points[away_team] += 1
            print("It's a draw!")
        
        # Check for forfeit due to injuries
        if team_stats["injuries"] >= 5:
            print("Critical injuries! Match forfeited.")
            continue  # Skip remaining group matches
    
    return points

# Knockout stages simulation
def knockout_stages():
    print("\n=== KNOCKOUT STAGES ===")
    stages = ["Round of 16", "Quarter-final", "Semi-final", "Final"]
    current_stage = 0
    tournament_won = False
    
    while current_stage < len(stages):
        print(f"\n--- {stages[current_stage]} ---")
        
        # Check if team can progress
        if team_stats["morale"] < 20:
            print("Morale too low! Team eliminated.")
            break  # Exit loop - tournament lost
        
        result = input(f"Result in {stages[current_stage]}? (w/l): ").lower()
        
        if result == "w":
            team_stats["morale"] += 15
            team_stats["strength"] += 5
            print("Victory! Morale +15, Strength +5")
        elif result == "l":
            print("Defeat! Team eliminated.")
            break  # Exit loop - tournament lost
        else:
            print("Invalid result, match replayed.")
            continue  # Skip to next iteration
        
        # Advance to next stage
        current_stage += 1
        
        if current_stage == len(stages):
            tournament_won = True
            break  # Exit loop - tournament won
    
    return tournament_won

# Main tournament simulation
def run_tournament_simulation():
    print("=== 2026 FIFA WORLD CUP SIMULATION ===")
    
    # Pre-tournament
    pre_tournament_preparation()
    
    # Group stage
    teams = ["Your Team", "Team B", "Team C"]
    points = group_stage_simulation(teams)
    
    print(f"\nGroup Standings: {points}")
    
    # Check qualification
    if points["Your Team"] < 4:
        print("Failed to qualify for knockout stages!")
        return
    
    # Knockout stages
    if knockout_stages():
        print("\nCONGRATULATIONS! YOU HAVE WON THE WORLD CUP!")
    else:
        print("\nTeam eliminated from tournament.")

# Run the simulation
if __name__ == "__main__":
    run_tournament_simulation()