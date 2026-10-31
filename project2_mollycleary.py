print("===== PLATFORM ADVENTURE =====")
levels = [1, 2, 3, 4, 5]
coins = [5, 8, 3, 10, 7]
enemies = [2, 4, 1, 5, 3]
power_ups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]
for level in range(0, 5):
    print(f"Level: {levels[level]}")
    print(f"Coins: {coins[level]}")
    print(f"Enemies: {enemies[level]}")
    print(f"Power ups: {power_ups[level]}\n")
print("===== PLAYER INFORMATION =====")
player_name = "Hero"
lives = 3
score = 0
total_coins = 0

print(f"Player name: {player_name}")
print(f"Lives: {lives}")
print(f"Score: {score}")
print(f"Total coins: {total_coins}")

print("===== LEVEL SCORES =====")
level_scores = [40, 85, 25, 75, 80]
for i in range(0, 5):
    print(f"Level {levels[i]} Score: {level_scores[i]}")

print("===== ADVENTURE ACTIONS =====")
actions = [0, 1, 0, 2, 1]
action_results = []

for a in actions:
    if a == 0:
        action_results.append("Collect Coins")
    elif a == 1:
        action_results.append("Fight Enemies")
    elif a == 2:
        action_results.append("Use Power-Up")

for i in range(0, 5):
    print(f"Level {levels[i]}: {action_results[i]}")

print("===== LIFE HISTORY =====")
life_history = []
current_lives = 3

if enemies[0] >= 4 and power_ups[0] != "Star":
    current_lives -= 1
life_history.append(current_lives)
print(f"After Level 1: {current_lives} lives")

if enemies[1] >= 4 and power_ups[1] != "Star":
    current_lives -= 1
life_history.append(current_lives)
print(f"After Level 2: {current_lives} lives")

if enemies[2] >= 4 and power_ups[2] != "Star":
    current_lives -= 1
life_history.append(current_lives)
print(f"After Level 3: {current_lives} lives")

if enemies[3] >= 4 and power_ups[3] != "Star":
    current_lives -= 1
life_history.append(current_lives)
print(f"After Level 4: {current_lives} lives")

if enemies[4] >= 4 and power_ups[4] != "Star":
    current_lives -= 1
life_history.append(current_lives)
print(f"After Level 5: {current_lives} lives")

print("===== COIN COLLECTION =====")
total_coins_collected = coins[0] + coins[1] + coins[2] + coins[3] + coins[4]
print(f"Coins collected: {total_coins_collected}")

bonus_coin_levels = [coin for coin in coins if coin >= 7]
print(f"Levels with 7 or more coins: {bonus_coin_levels}")

print("===== POWER-UP INVENTORY =====")
inventory = ["Mushroom", "Star", "Flower"]
used_powerups = ["Mushroom", "Star"]

print(f"Starting Inventory: {inventory}")
print(f"Used Power-Ups: {used_powerups}")

inventory.pop(0)
inventory.pop(0)
print(f"Remaining Inventory: {inventory}")

print("===== LEVEL ANALYSIS =====")
print(f"Total Coins: {total_coins_collected}")
print(f"Most Coins in One Level: 10")
print(f"Fewest Coins in One Level: 3")
print(f"Average Coins per Level: {total_coins_collected / 5}")
print(f"Total Enemies: {enemies[0] + enemies[1] + enemies[2] + enemies[3] + enemies[4]}")
print(f"Most Enemies in One Level: 5")

print("===== HIGH SCORES =====")
high_scores = [s for s in level_scores if s >= 50]
print(f"Scores of 50 or Higher: {high_scores}")

print("===== SCORE HISTORY =====")
score1 = level_scores[0]
score2 = score1 + level_scores[1]
score3 = score2 + level_scores[2]
score4 = score3 + level_scores[3]
score5 = score4 + level_scores[4]

score_history = [score1, score2, score3, score4, score5]

print(f"After Level 1: {score1}")
print(f"After Level 2: {score2}")
print(f"After Level 3: {score3}")
print(f"After Level 4: {score4}")
print(f"After Level 5: {score5}")

print(f"First Two Scores: {score_history[:2]}")
print(f"Last Two Scores: {score_history[3:]}")

print("===== FINAL STATUS =====")
if score5 >= 250:
    final_status = "Adventure Champion"
elif score5 >= 150:
    final_status = "Great Adventure"
else:
    final_status = "Keep Practicing"

print(final_status)

print("===== ADVENTURE RANKING =====")
print(f"Final Score: {score5}")
print(f"Final Lives: {life_history[-1]}")
print("Rank: Legend")








