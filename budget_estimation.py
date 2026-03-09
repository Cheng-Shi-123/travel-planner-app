def estimate_budget(trip_details):
    """
    Estimate the budget for a trip based on trip_details dictionary.
    trip_details: dict with keys like 'duration', 'destination', 'num_people', etc.
    Returns estimated budget as float.
    """
    # Example simple estimation logic
    base_cost = 500.0  # base cost per person
    days = trip_details.get('duration', 1)
    num_people = trip_details.get('num_people', 1)
    destination = trip_details.get('destination', 'unknown')
    destination_multiplier = 1.2 if destination.lower() == 'paris' else 1.0
    return base_cost * days * num_people * destination_multiplier

if __name__ == "__main__":
    example_trip = {
        'duration': 5,
        'num_people': 2,
        'destination': 'Paris'
    }
    budget = estimate_budget(example_trip)
    print(f"Estimated budget: ${budget:.2f}")
