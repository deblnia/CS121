'''
Epidemic modelling

YOUR NAME

Functions for running a simple epidemiological simulation
'''

import random

import click

# This seed should be used for debugging purposes only!  Do not refer
# to it in your code.
TEST_SEED = 20170217

def count_ever_infected(city):
    '''
    Count the number of people infected or recovered

    Inputs:
      city (list of strings): the state of all people in the
        simulation at the start of the day
    Returns (int): count of the number of people who have been
      infected at some time.
    '''

    # YOUR CODE HERE

    # REPLACE -1 WITH THE APPROPRIATE INTEGER
    return -1


def has_an_infected_neighbor(city, position):
    '''
    Determine whether a person has an infected neighbor

    Inputs:
      city (list): the state of all people in the simulation at the
        start of the day
      position (int): the position of the person to check

    Returns:
      True, if the person has an infected neighbor, False otherwise.
    '''

    assert city[position] == "S"

    # YOUR CODE HERE

    # REPLACE None WITH THE APPROPRIATE BOOLEAN VALUE

    return None


def gets_infected_at_position(city, position, infection_rate):
    '''
    Determine whether the person at the specified position gets
    infected.

    Inputs:
      city (list): the state of all people in the simulation at the
        start of the day
      position (int): the position of the person to check
      infection_rate (float): the chance of getting infected given an
        infected neighbor


    Returns (boolean):
      True, if the person would become infected, False otherwise.
    '''
    # This function should only be called when the person at position
    # is susceptible to infection.
    assert city[position] == "S"

    # YOUR CODE HERE

    # REPLACE None WITH THE APPROPRIATE BOOLEAN VALUE
    return None


def advance_person_at_position(city, position,
                               infection_rate, days_contagious):
    '''
    Compute the next state for the person at the specified position.

    Inputs:
      city (list): the state of all people in the simulation at the
        start of the day
      position (int): the position of the person to check
      infection_rate (float): the chance of getting infected given an
        infected neighbor
      days_contagious (int): the number of a days a person is infected

    Returns: (string) disease state of the person after one day
    '''

    # YOUR CODE HERE

    # REPLACE None WITH THE APPROPRIATE STRING
    return None


def simulate_one_day(starting_city, infection_rate, days_contagious):
    '''
    Move the simulation forward a single day.

    Inputs:
      starting_city (list): the state of all people in the simulation at the
        start of the day
      infection_rate (float): the chance of getting infected given an
        infected neighbor
      days_contagious (int): the number of a days a person is infected
    Returns:
      new_city (list): disease state of the city after one day
    '''

    # YOUR CODE HERE

    # REPLACE None WITH THE APPROPRIATE LIST OF STRINGS
    return None


def run_simulation(starting_city, random_seed, max_num_days,
                   infection_rate, days_contagious):
    '''
    Run the entire simulation for up to the specified maximum number
    of days.

    Inputs:
      starting_city (list): the state of all people in the city at the
        start of the simulation
      random_seed (int): the random seed to use for the simulation
      max_num_days (int): the maximum days of the simulation
      infection_rate (float): the chance of getting infected given an
        infected neighbor
      days_contagious (int): the number of a days a person is infected

    Returns tuple (list of strings, int): the final state of the city
      and the number of days actually simulated.
    '''
    assert max_num_days >= 0

    # YOUR CODE HERE

    # REPLACE (None, None) WITH THE APPROPRIATE TUPLE
    #  (city, number of days simulated)
    return (None, None)


def calc_avg_num_newly_infected(
        starting_city, random_seed, max_num_days,
        infection_rate, days_contagious, num_trials):
    '''
    Conduct N trials with the specified infection probability and
    calculate the number of people on average get infected over time.

    Inputs:
      starting_city (list): the state of all people in the city at the
        start of the simulation
      random_seed (int): the starting random seed. Use this value for
        the FIRST simulation, and then increment it once for each
        subsequent run.
      max_num_days (int): the maximum days of the simulation
      infection_rate (float): the chance of getting infected given an
        infected neighbor
      days_contagious (int): the number of a days a person is infected
      num_trials (int): the number of trials to run

    Returns (float): the average number of people infected over time
    '''
    assert max_num_days >= 0
    assert num_trials > 0

    # YOUR CODE HERE

    # REPLACE -1.0 WITH THE APPROPRIATE FLOATING POINT VALUE
    return -1.0


################ Do not change the code below this line #######################


@click.command()
@click.argument("city", type=str)
@click.option("--random_seed", default=None, type=int)
@click.option("--max-num-days", default=1, type=int)
@click.option("--infection-rate", default=0.5, type=float)
@click.option("--days-contagious", default=2, type=int)
@click.option("--num-trials", default=1, type=int)
@click.option("--task-type", default="single",
              type=click.Choice(['single', 'average']))
def cmd(city, random_seed, max_num_days, infection_rate,
        days_contagious, num_trials, task_type):
    '''
    Process the command-line arguments and do the work.
    '''

    # Convert the city string into a city list.
    city = [p.strip() for p in city.split(",")]
    emsg = ("Error: people in the city must be susceptible ('S'),"
            " recovered ('R'), or infected ('Ix', where *x* is an integer")
    for p in city:
        if p[0] == "I":
            try:
                _ = int(p[1])
            except ValueError:
                print(emsg)
                return -1
        elif p not in {"S", "R"}:
            print(emsg)
            return -1

    if task_type == "single":
        print("Running one simulation...")
        final_city, num_days_simulated = run_simulation(
            city, random_seed, max_num_days, infection_rate, days_contagious)
        print("Final city:", final_city)
        print("Days simulated:", num_days_simulated)
    else:
        print("Running multiple trials...")
        avg_infected = calc_avg_num_newly_infected(
            city, random_seed, max_num_days, infection_rate,
            days_contagious, num_trials)
        msg = "Over {} trial(s), on average, {:3.1f} people were infected"
        print(msg.format(num_trials, avg_infected))

    return 0


if __name__ == "__main__":
    cmd() # pylint: disable=no-value-for-parameter
