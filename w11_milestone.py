with open("life-expectancy.csv") as dataset:
    year = int(input("Enter the year of interest: "))
    next(dataset)
    # Variables to store the year and the life expectancy
    # Max Year consulted year
    max_expentance = 0
    max_expentance_country = ""

    # Min Year consulted year
    min_expentance = 100
    min_expetance_country = ""

    # Average
    averages_expentances = []
    average_expentance = 0

    # Overall Variables
    overall_min_expentance = 100
    overall_min_expetance_country = ""
    overall_min_expentance_year = 0

    overall_max_expentance = 0
    overall_max_expentance_country = ""
    overall_max_expentance_year = 0

    for row in dataset:
        cell = row.split(",")
        dataset_year = int(cell[2])
        country = str(cell[0])
        country_code = str(cell[1])
        life_expectancy = float(cell[3])
        
        # Store the life expectancy to calculate the average of all countries

        ## Check and save the max and min life expectancy for specific year
        if dataset_year == year:
            averages_expentances.append(life_expectancy)
            if life_expectancy > max_expentance:
                max_expentance = life_expectancy
                max_expentance_country = country
            elif life_expectancy  < min_expentance:
                min_expentance = life_expectancy
                min_expentance_country = country
    
        ## Overall min and max life expectancy
        if life_expectancy > overall_max_expentance:
            overall_max_expentance = life_expectancy
            overall_max_expentance_country = country
            overall_max_expentance_year = dataset_year
        elif life_expectancy  < overall_min_expentance:
            overall_min_expentance = life_expectancy
            overall_min_expetance_country = country
            overall_min_expentance_year = dataset_year 
    
    # The overall max life expectancy is: 86.751 from Monaco in 2019
    print(f"\nThe overall max life expectancy is: {overall_max_expentance} from {overall_max_expentance_country} in {overall_max_expentance_year}")
    print(f"The overall min life expectancy is: {overall_min_expentance} from {overall_min_expetance_country} in {overall_min_expentance_year}")

    # Calculates the average of all countries
    for element in averages_expentances:
        average_expentance += element

    # Results for the spefice year
    print(f"\nFor the year {year}: ")
    print(f"The average life expectancy across all countries was {round(average_expentance/len(averages_expentances), 2)}")
    print(f"The overall max life expectancy is: {max_expentance} from {max_expentance_country}")
    print(f"The overall min life expectancy is: {min_expentance} from {min_expentance_country}")