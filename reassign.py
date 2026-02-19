from sheets import load_sheet

def urgent_reassignment(location):

    pilots = load_sheet("pilot_roster")
    drones = load_sheet("drone_fleet")

    available_pilot = pilots[
        (pilots["location"].str.contains(location, case=False)) &
        (pilots["status"] == "Available")
    ]

    available_drone = drones[
        (drones["location"].str.contains(location, case=False)) &
        (drones["status"] == "Available")
    ]

    if available_pilot.empty or available_drone.empty:
        return "❌ No immediate replacement available"

    p = available_pilot.iloc[0]
    d = available_drone.iloc[0]

    return f"""
🚑 URGENT REASSIGNMENT READY

Replacement Pilot: {p['name']}
Replacement Drone: {d['drone_id']}

Mission can continue.
"""
