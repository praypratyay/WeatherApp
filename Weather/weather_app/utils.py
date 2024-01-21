
def get_qualitative_name(pollutant, concentration):
    """
    Convert pollutant concentration to qualitative name based on defined ranges.

    Args:
    - pollutant (str): The pollutant component (e.g., 'so2', 'no2', 'pm10', 'pm2_5', 'o3', 'co').
    - concentration (float): The concentration level of the pollutant.

    Returns:
    - str: Qualitative name corresponding to the concentration level.
    """
    ranges = {
        'so2': [0, 20, 80, 250, 350],
        'no2': [0, 40, 70, 150, 200],
        'pm10': [0, 20, 50, 100, 200],
        'pm2_5': [0, 10, 25, 50, 100],
        'o3': [0, 60, 100, 140, 180],
        'co': [0, 4400, 9400, 12400, 15400],
    }

    qualitative_names = {
        1: "Good",
        2: "Fair",
        3: "Moderate",
        4: "Poor",
        5: "Very Poor",
    }

    if pollutant not in ranges:
        return "N/A"
    
    for i in range(4,-1,-1): 
        if concentration >= ranges[pollutant][i]:
            return qualitative_names[i+1]
        
    return "N/A"
