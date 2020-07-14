import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = {'all','january','february','march','april','may','june'}
DAYS = {'all', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:

        entered_city = input('For what city are you interested in getting statistics - Texas, Chicago, New York City, or Washington? ').lower()

        if entered_city in CITY_DATA:
            break
        elif entered_city == 'q':
            exit()
        else:
            print('That city is not valid.  Please enter a city in the list or q to quit. ')

    city = entered_city

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        entered_month = input('For what month do you want statistics - all, January, February, March, April, May, June, July? ').lower()

        if entered_month in MONTHS:
            break
        elif entered_month == 'q':
            exit()
        else:
            print('That month is not a valid selection.  Please enter a month in the list or q to quit. ')

    month = entered_month

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        entered_day = input('For what day of the week do you want statistic - all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? ').lower()

        if entered_day in DAYS:
            break
        elif entered_day == 'q':
            exit()
        else:
            print('That month is not a valid selection.  Please enter a day of the week in the list or q to quit. ')

    day = entered_day

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
    df=pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns

    df['Month'] = df['Start Time'].dt.month
    df['Day_Of_Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding list
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['Day_Of_Week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]
    print('Most Popular Month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['Day_Of_Week'].mode()[0]
    print('Most Popular Day of Week: ', most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['Hour'].mode()[0]
    print('Most Popular Start Hour: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station: ', most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + ' - ' + df['End Station']
    most_common_combination = df['Combination'].mode()[0]
    print('Most Popular Combination: ', most_common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('The Total Trip Duration - ', total_trip_duration)

    # TO DO: display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print('The Mean Trip Duration - ', mean_trip_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_distinct_values = df['User Type'].nunique()
    print('Number of Distinct User Types -', user_type_distinct_values)
    user_type_cnt = df['User Type'].value_counts()
    print('See below for Counts by User Type \n', user_type_cnt)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_distinct_values = df['Gender'].nunique()
        print('\nNumber of Distinct Genders -', gender_distinct_values)
        gender_cnt = df['Gender'].value_counts()
        print('See below for Counts by Gender \n', gender_cnt)
    else:
        print('Note: the file does not contain Gender information')

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        print('\nThe earliest Birth Year -', int(df['Birth Year'].min()))
        print('The most recent Birth Year -', int(df['Birth Year'].max()))
        print('The most common Birth Year -', int(df['Birth Year'].mode()))
    else:
        print('Note: the file does not contain Birth Year information')


    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


    show_data = 'n'
    r=0
    pd.set_option('display.max_columns', None)
    while True:
        show_data = input('\nWould you like to see 5 rows of detail data (y/n)? ').lower()
        if show_data == 'y':
            print(df.iloc[r:r+5])
            r = r + 5
        else:
            print('\n')
            print('-'*117)
            print('-'*19, 'Whoohooo! Having fun with python.  Thank you for your help on this project!! ', '-'*19)
            print('-'*117)
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart (y/n)? ')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
