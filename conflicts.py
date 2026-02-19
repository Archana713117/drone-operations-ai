from sheets import load_sheet

def check_conflicts(pilot, drone, location):

    warnings = []

    # location mismatch
    if pilot["location"].lower() != location.lower():
        warnings.append("⚠ Pilot not in mission location")

    if drone["location"].lower() != location.lower():
        warnings.append("⚠ Drone not in mission location")

    # maintenance
    if drone["status"].lower() == "maintenance":
        warnings.append("⚠ Drone under maintenance")

    # unavailable pilot
    if pilot["status"].lower() != "available":
        warnings.append("⚠ Pilot not available")

    return warnings
