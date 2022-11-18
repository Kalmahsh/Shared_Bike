import time
import numpy as np
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
CITIES = list(CITY_DATA.keys())


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_name = ''
    while city_name.lower() not in CITIES:
        city_name = input("\nWhich city do you select from chicago, new york city, washington'\n")
        if city_name.lower() in CITIES:
             # We continue to analyze data.
            city = city_name.lower()
        else:
            # There is no data for this case and we continue the loop.  
            print("There is no data for this case, Please input either chicago, new york city or washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTHS:
        month_name = input("\nWhich month do you select from january until june or 'all'\n")
        if month_name.lower() in MONTHS:
            # We continue to analyze data.
            month = month_name.lower()
        else:
            # There is no data for this case and we continue the loop.
            print("There is no data for this case, Please input from january until june or 'all'\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAYS:
        day_name = input("\nWhich day in a week do you select or 'all'\n")
        if day_name.lower() in DAYS:
            # We continue to analyze data.
            day = day_name.lower()
        else:
            # There is no data for this case and we continue the loop.
            print("There is no data for this case, Please input monday, tuesday, ... sunday or 'all'\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file 
    df = pd.read_csv(CITY_DATA[city])

    # define start Time column with datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # make new columns  from Start Time for month and day of week 
    df['month'] = df['Start Time'].dt.month
    # df['day_of_week'] = df['Start Time'].dt.weekday
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # select the month
    if month != 'all':
        # determind the index of the months list 
        month = MONTHS.index(month) + 1

        # define the dataframe of month
        df = df[df['month'] == month]

    # select the week of day
    if day != 'all':
        # define the dataframe of day of week
        df = df[df['day_of_week'] == day.title()]    

    return df


def time_stats(df):
    """ Displays statistics on the most frequent times of travel. """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common start hour                                                                
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: " + str(common_start_hour))
    
    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + str(common_day_of_week))

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    # print("The most common month  is: " + str(common_month))
    print("The most common month  is: " + str(MONTHS[common_month-1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + " " + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #df = pd.read_csv(CITY_DATA[city])

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types is: \n" + str(user_types))   

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("The count of user gender is: \n" + str(gender))
    except:
        print("There is no data.")
            
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth is: {}\n'.format(earliest_birth))
        print('Most recent birth is: {}\n'.format(most_recent_birth))
        print('Most common birth is: {}\n'.format(most_common_birth))
    except:
        print("There is no data.")
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    i = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        i = i + 5
        print(df.iloc[i:i+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
    main()  
