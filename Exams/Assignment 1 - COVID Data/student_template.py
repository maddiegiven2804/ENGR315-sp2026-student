import sys


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """

    for (date, county, state, flips, cases, deaths) in data: 

        if county == 'Rockingham' and state == 'Virginia' and cases > 0:
            print('First Case in Rockingham County', date) 
            break

    for (date, county, state, flips, cases, deaths) in data: 
        if county == 'Harrisonburg city' and state == 'Virginia' and cases > 0:
            print('First Case in Harrisonburg', date)
            break

    return 

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:    
    """
    max_rocking = 0
    previous_rocking = None
    max_harris = 0
    previous_harris = None


    for (date, county, state, flips, cases, deaths) in data: 
        if county == 'Rockingham' and state == 'Virginia': 
            if previous_rocking is not None:
                Rise_in_cases = int(cases) - previous_rocking

                if Rise_in_cases > max_rocking:
                    max_rocking = Rise_in_cases 
                    rock_date = date
            previous_rocking = int(cases)

    for (date, county, state, flips, cases, deaths) in data: 
        if county == 'Harrisonburg city' and state == 'Virginia':
            if previous_harris is not None: 
                Rise_in_cases = int(cases) - previous_harris
            
                if Rise_in_cases > max_harris:
                    max_harris = Rise_in_cases
                    hburg_date = date
            previous_harris = int(cases)
            
    print('Day with the highest new cases in Harrisonburg is', hburg_date) 
    print('Day with the highest new cases in Rockingham is', rock_date)  
 
    return

def third_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    :return:
    """
    
    # Rockingham 
    max_rocking = 0 
    previous_rocking = None
    max_cases = []

    for (date, county, state, flips, cases, deaths) in data: 
        if county == 'Rockingham' and state == 'Virginia': 
            if previous_rocking is not None:
                max_cases.append((date, int(cases) - previous_rocking))
        previous_rocking = int(cases)

    for i in range(len(max_cases) - 6): 
        week_sum = sum(cases for (date, cases) in max_cases[i: i + 7])
        if week_sum > max_rocking:
            max_rocking = week_sum
            date1 = max_cases[i][0]
            date2 = max_cases[i + 6][0]

    print("The range of the dates is " + date1 + "-" + date2)


    return

if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

 ##   for (date,county, state, fips, cases, deaths) in data:
  ##      print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question: Use print() to display your responses.
    # What was the worst seven day period in Harrisonburg for new COVID cases (in terms of absolute number of cases)?
    # What was the worst seven day period in Rockingham County for new COVID cases (in terms of absolute number of cases)?
    third_question(data)


