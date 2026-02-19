from sheets import load_sheet
from conflicts import check_conflicts

def suggest_assignment(skill, location):

    pilots = load_sheet("pilot_roster")
    drones = load_sheet("drone_fleet")

    pilot_df = pilots[
        (pilots["skills"].str.contains(skill, case=False)) &
        (pilots["location"].str.contains(location, case=False))
    ]

    drone_df = drones[
        (drones["location"].str.contains(location, case=False))
    ]

    if pilot_df.empty:
        return "❌ No pilot found"

    if drone_df.empty:
        return "❌ No drone found"

    pilot = pilot_df.iloc[0]
    drone = drone_df.iloc[0]

    warnings = check_conflicts(pilot, drone, location)

    result = f"""
✅ Assignment Suggestion

Pilot: {pilot['name']}
Drone: {drone['drone_id']}
Location: {location}
Skill: {skill}
"""

    if warnings:
        result += "\n\n⚠ Warnings:\n" + "\n".join(warnings)

    return result
