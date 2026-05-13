
import random, time

def intro():
    print("\n?? Stellar Delivery! Nova, your ship Interglow awaits.")
    print("Complete missions, manage fuel, and keep your ship in one piece.")
    time.sleep(1)

def create_pilot():
    return {"name": "Nova", "credits": 100, "fuel": 100, "reputation": 50,
            "ship_health": 100, "cargo_capacity": 3, "current_cargo": [],
            "missions_completed": 0}

def create_missions():
    return [
        {"destination": "Lava Orbital Station", "reward": 80, "fuel_cost": 20, "difficulty": 3},
        {"destination": "Crystal Reef Colony", "reward": 60, "fuel_cost": 15, "difficulty": 2},
        {"destination": "Aurora Outpost", "reward": 40, "fuel_cost": 10, "difficulty": 1},
        {"destination": "Nebula Research Hub", "reward": 100, "fuel_cost": 25, "difficulty": 4},
    ]

def show_status(pilot):
    print("\n=== Pilot Status ===")
    print(f"Name: {pilot['name']}  Credits: {pilot['credits']}  Fuel: {pilot['fuel']}%")
    print(f"Reputation: {pilot['reputation']}  Health: {pilot['ship_health']}%")
    cargo = ", ".join(pilot['current_cargo']) if pilot['current_cargo'] else "Empty"
    print(f"Cargo: {cargo} ({len(pilot['current_cargo'])}/{pilot['cargo_capacity']})")
    print("====================")

def choose_action(missions):
    print("\nAvailable missions:")
    for idx, m in enumerate(missions, 1):
        print(f"{idx}. {m['destination']} - {m['reward']}cr, {m['fuel_cost']}% fuel, diff {m['difficulty']}")
    print("5. Rest and refuel\n6. Visit the market\n7. Quit")
    while True:
        choice = input("Choose 1-7: ").strip()
        if choice in [str(i) for i in range(1, 8)]:
            return int(choice)
        print("Enter a number from 1 to 7.")

def handle_event(pilot, event):
    if event == "meteor":
        d = random.randint(5, 15); pilot['ship_health'] -= d
        print(f"Meteor impact! -{d}% health.")
    elif event == "pirate":
        if pilot['reputation'] > 60:
            print("Pirates back off due to your reputation."); pilot['reputation'] += 2
        else:
            loss = random.randint(10, 25); pilot['credits'] = max(0, pilot['credits'] - loss)
            pilot['ship_health'] -= 10
            print(f"Pirates steal {loss} credits and damage the ship.")
    elif event == "engine":
        d = random.randint(5, 15); pilot['ship_health'] -= d
        print(f"Engine trouble costs -{d}% health.")
    else:
        bonus = random.randint(10, 25); pilot['credits'] += bonus; pilot['reputation'] += 2
        print(f"Friendly trader gives you {bonus} bonus credits.")

def perform_mission(pilot, mission):
    print(f"\nLaunching to {mission['destination']}...")
    time.sleep(1)
    if pilot['fuel'] < mission['fuel_cost']:
        print("Not enough fuel."); return
    pilot['fuel'] -= mission['fuel_cost']
    if random.randint(1, 10) <= mission['difficulty']:
        print("?? Random event on route!")
        handle_event(pilot, random.choice(["meteor", "pirate", "engine", "friendly"]))
    else:
        print("The route is clear.")
    success = random.randint(1, 100) <= 70 + pilot['reputation'] - mission['difficulty'] * 10
    if success:
        print(f"? Delivery completed to {mission['destination']}!")
        pilot['credits'] += mission['reward']; pilot['reputation'] = min(100, pilot['reputation'] + 5)
        pilot['missions_completed'] += 1
        if random.random() < 0.4 and len(pilot['current_cargo']) < pilot['cargo_capacity']:
            item = random.choice(["Rare Crystal", "Quantum Chip", "Galactic Spice"])
            pilot['current_cargo'].append(item)
            print(f"Bonus cargo found: {item}.")
    else:
        print("? Delivery failed and your ship took damage.")
        pilot['ship_health'] -= 15; pilot['reputation'] = max(0, pilot['reputation'] - 10)

def rest_and_refuel(pilot):
    print("\nDocking for rest and refuel..."); time.sleep(1)
    pilot['fuel'] = min(100, pilot['fuel'] + 40)
    pilot['ship_health'] = min(100, pilot['ship_health'] + 20)
    pilot['reputation'] = min(100, pilot['reputation'] + 1)
    print("Fuel and health restored.")

def visit_market(pilot):
    print("\nMarket options:\n1. Fuel boost (30cr)\n2. Repair (40cr)\n3. Cargo upgrade (60cr)\n4. Leave")
    while True:
        c = input("Choose 1-4: ").strip()
        if c == "1":
            if pilot['credits'] >= 30: pilot['credits'] -= 30; pilot['fuel'] = min(100, pilot['fuel'] + 50); print("Fuel boost purchased.")
            else: print("Not enough credits.")
            break
        if c == "2":
            if pilot['credits'] >= 40: pilot['credits'] -= 40; pilot['ship_health'] = min(100, pilot['ship_health'] + 50); print("Ship repaired.")
            else: print("Not enough credits.")
            break
        if c == "3":
            if pilot['credits'] >= 60: pilot['credits'] -= 60; pilot['cargo_capacity'] += 1; print("Cargo hold upgraded.")
            else: print("Not enough credits.")
            break
        if c == "4": print("Leaving market."); break
        print("Enter a number from 1 to 4.")

def main():
    pilot = create_pilot(); missions = create_missions(); intro(); show_status(pilot)
    while True:
        action = choose_action(missions)
        if 1 <= action <= 4:
            perform_mission(pilot, missions[action - 1])
        elif action == 5:
            rest_and_refuel(pilot)
        elif action == 6:
            visit_market(pilot)
        else:
            print("\n?? Returning to the starport. Thanks for playing!"); break
        if pilot['ship_health'] <= 0:
            print("\nYour ship is too damaged to continue. Game over."); break
        if pilot['fuel'] <= 0:
            print("\nYou're out of fuel and drifting. Game over."); break
        show_status(pilot)
    print(f"\nFinal score: {pilot['missions_completed']} missions completed, {pilot['credits']} credits, {pilot['reputation']} reputation.")

if __name__ == "__main__":
    main()