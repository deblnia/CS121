'''
Epidemic modelling

Deblina Mukherjee

Functions for running a simple epidemiological simulation
'''

import random

import click


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
    count = 0 
    for y in city:
        if y[0] == 'I':
            count += 1
        elif y == 'R':
            count += 1
    return int(count)


def has_an_infected_neighbor(city, position):
#     '''
#     Determine whether a person has an infected neighbor

#     Inputs:
#       city (list): the state of all people in the simulation at the
#         start of the day
#       position (int): the position of the person to check

#     Returns:
#       True, if the person has an infected neighbor, False otherwise.
#     '''
    
    assert city[position] == "S"

    if len(city) == 1: #list of one 
        return False 
    elif position == 0: #first element 
        if city[1][0] == "I": 
          return True
        else: 
          return False 
    elif position == len(city) - 1: #last element 
        if city[-2][0] == "I":
          return True 
        else: 
            return False 
    else: 
        if city[position + 1][0] == "I": 
          return True
        elif city[position - 1][0] == "I":
          return True 
        else: 
            return False 

def gets_infected_at_position(city, position, infection_rate):
#     '''
#     Determine whether the person at the specified position gets
#     infected.

#     Inputs:
#       city (list): the state of all people in the simulation at the
#         start of the day
#       position (int): the position of the person to check
#       infection_rate (float): the chance of getting infected given an
#         infected neighbor


#     Returns (boolean):
#       True, if the person would become infected, False otherwise.
#     '''
#     # This function should only be called when the person at position
#     # is susceptible to infection.
#     assert city[position] == "S"

    if has_an_infected_neighbor(city, position) == True: 
        if random.random() < infection_rate: 
            return True
        else: 
            return False 
    else: 
        return False     


def advance_person_at_position(city, position,
                                infection_rate, days_contagious):
#     '''
#     Compute the next state for the person at the specified position.

#     Inputs:
#       city (list): the state of all people in the simulation at the
#         start of the day
#       position (int): the position of the person to check
#       infection_rate (float): the chance of getting infected given an
#         infected neighbor
#       days_contagious (int): the number of a days a person is infected

#     Returns: (string) disease state of the person after one day
#     '''
    if city[position] == "S": 
        if gets_infected_at_position(city, position, infection_rate): 
            return "I0"
        else: 
            return 'S'
    elif city[position][0] == "I":
        days = int(city[position][1:])
        if days + 1 < days_contagious: 
            return "I" + str(days + 1)
        else: 
            return 'R'
    elif city[position] == "R": 
        return 'R'

def simulate_one_day(starting_city, infection_rate, days_contagious):
#     '''
#     Move the simulation forward a single day.

#     Inputs:
#       starting_city (list): the state of all people in the simulation at the
#         start of the day
#       infection_rate (float): the chance of getting infected given an
#         infected neighbor
#       days_contagious (int): the number of a days a person is infected
#     Returns:
#       new_city (list): disease state of the city after one day
#     '''

    end_city = []
    for i in range(len(starting_city)): #could also use ennumerate 
        end_city.append(advance_person_at_position(starting_city,i,
            infection_rate, days_contagious))
    return end_city 


def run_simulation(starting_city, random_seed, max_num_days,
                   infection_rate, days_contagious):
#     '''
#     Run the entire simulation for up to the specified maximum number
#     of days.

#     Inputs:
#       starting_city (list): the state of all people in the city at the
#         start of the simulation
#       random_seed (int): the random seed to use for the simulation
#       max_num_days (int): the maximum days of the simulation
#       infection_rate (float): the chance of getting infected given an
#         infected neighbor
#       days_contagious (int): the number of a days a person is infected

#     Returns tuple (list of strings, int): the final state of the city
#       and the number of days actually simulated.
#     '''
    assert max_num_days >= 0

    random.seed(random_seed)
    post_sim_1day = [] #list of all cities
    post_sim_1day.append(simulate_one_day(starting_city, 
        infection_rate, days_contagious))
    num_days = 1
    if post_sim_1day[0] == starting_city: 
        return(post_sim_1day[0], num_days)
    else: 
        for i in range(max_num_days-1): 
            num_days += 1
            post_sim_1day.append(simulate_one_day(post_sim_1day[-1], 
                infection_rate, days_contagious))
            if post_sim_1day[-1] == post_sim_1day[-2]: 
                return (post_sim_1day[-1], num_days)
        return (post_sim_1day[-1], num_days)


def calc_avg_num_newly_infected(
         starting_city, random_seed, max_num_days,
         infection_rate, days_contagious, num_trials):
#     '''
#     Conduct N trials with the specified infection probability and
#     calculate the number of people on average get infected over time.

#     Inputs:
#       starting_city (list): the state of all people in the city at the
#         start of the simulation
#       random_seed (int): the starting random seed. Use this value for
#         the FIRST simulation, and then increment it once for each
#         subsequent run.
#       max_num_days (int): the maximum days of the simulation
#       infection_rate (float): the chance of getting infected given an
#         infected neighbor
#       days_contagious (int): the number of a days a person is infected
#       num_trials (int): the number of trials to run

#     Returns (float): the average number of people infected over time
#     '''
    assert max_num_days >= 0
    assert num_trials > 0

def calc_avg_num_newly_infected(
         starting_city, random_seed, max_num_days,
         infection_rate, days_contagious, num_trials):
    start_inf = count_ever_infected(starting_city)
    all_sim = []
    diff = []
    for i in range(num_trials): 
        print(start_inf, "starting infected")
        print(random_seed, "random")
        all_sim.append(run_simulation(starting_city, random_seed, max_num_days, 
                                      infection_rate, days_contagious)[0])
        print(all_sim[i])
        end_inf = int(count_ever_infected(all_sim[-1]))
        print(end_inf, "ever infected")
        print(end_inf - start_inf, "new infected")
        diff.append(end_inf - start_inf)
        random_seed += 1
    start_inf = end_inf 
    diffsum = sum(diff)
    return diffsum/num_trials


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
