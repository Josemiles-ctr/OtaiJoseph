# match_results={
# 	"Home_goals" : int,
# 	"Away_goals" : int	
# }

def make_group_stage_fixture(teams):
    if len(teams) != 3:
        raise ValueError("Expects exactly three teams")
    fixture = {
        "match1": [teams[0], teams[1]],
        "match2": [teams[1], teams[2]],
        "match3": [teams[2], teams[0]]
    }
    return fixture


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
    
    fixture = make_group_stage_fixture(teams)
    
    for match_key, (home_team, away_team) in fixture.items():
        print(f"\n{match_key}: {home_team} vs {away_team}")
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
            break
    
    return points

# Knockout stages simulation
def knockout_stages(team_name):
    print(f"\n=== KNOCKOUT STAGES ({team_name}) ===")
    stages = ["Round of 16", "Quarter-final", "Semi-final", "Final"]
    current_stage = 0
    tournament_won = False
    
    while current_stage < len(stages):
        print(f"\n--- {stages[current_stage]} ---")
        
        # Check if team can progress
        if team_stats["morale"] < 20:
            print(f"{team_name}: Morale too low! Team eliminated.")
            break
        
        result = input(f"Result for {team_name} in {stages[current_stage]}? (w/l): ").lower()
        
        if result == "w":
            team_stats["morale"] += 15
            team_stats["strength"] += 5
            print(f"{team_name} wins! Morale +15, Strength +5")
        elif result == "l":
            print(f"{team_name} loses! Team eliminated.")
            break
        else:
            print("Invalid result, match replayed.")
            continue
        
        # Advance to next stage
        current_stage += 1
        
        if current_stage == len(stages):
            tournament_won = True
            break
    
    return tournament_won

# Main tournament simulation
def run_tournament_simulation():
    print("=== 2026 FIFA WORLD CUP SIMULATION ===")
    
    # Pre-tournament (friendlies and training)
    pre_tournament_preparation()
    
    # Enter group stage teams after preparation
    print("\n=== ENTER GROUP STAGE TEAMS ===")
    teams = [
        input("Team 1: ").strip(),
        input("Team 2: ").strip(),
        input("Team 3: ").strip()
    ]
    team_name = input("Which team are you managing? ").strip()
    if team_name not in teams:
        raise ValueError("Selected team must be one of the 3 entered teams")
    
    # Group stage
    points = group_stage_simulation(teams)
    
    print(f"\nGroup Standings: {points}")
    
    # Check qualification
    if points[team_name] < 4:
        print(f"{team_name} failed to qualify for knockout stages!")
        return
    
    # Knockout stages
    if knockout_stages(team_name):
        print(f"\nCONGRATULATIONS! {team_name} HAS WON THE WORLD CUP!")
    else:
        print(f"\n{team_name} eliminated from tournament.")

# Run the simulation
if __name__ == "__main__":
    run_tournament_simulation()