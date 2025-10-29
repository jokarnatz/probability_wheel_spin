# this script explores the probabilities of a wheel spinning game
# imagine you spin two wheels at a time
# one with numbers and one with letters
# how are the probabilities that on one of the wheels appears a 3 OR a consonant on the other wheel?
# and how big are the probabilities that no 3 AND no consonant appears?

from random import choice
from time import perf_counter

NUM_WINNER: int = 3
LETTER_WINNER: list = ['b','c','d','f','g','h']
DEF_ROUNDS: int = 1_000_000

def create_lists() ->tuple[list,list]:
    num_list = [1,2,3,2,3,1,2]
    letter_list = ['a','b','c','d','e','f','g','h']
    return num_list, letter_list

def create_counts() ->tuple:
    count_hit = 0
    count_num_hit = 0
    count_letter_hit = 0
    count_miss = 0
    count_total = 0
    return count_hit, count_num_hit, count_letter_hit, count_miss, count_total

def spin_wheel(num_list: list, letter_list: list) ->tuple[int,int]:
    num_choice = choice(num_list)
    letter_choice = choice(letter_list)
    return num_choice, letter_choice
    
def count_spins(
        num_choice: int, 
        letter_choice: int, 
        count_hit: int, 
        count_num_hit: int, 
        count_letter_hit: int, 
        count_miss: int, 
        count_total: int
        ) ->tuple:
    count_total += 1
    if num_choice == NUM_WINNER: # winning conditions: 3 
        count_num_hit += 1
        count_hit += 1
    elif letter_choice in LETTER_WINNER: # winning conditions: consonant
        count_letter_hit += 1
        count_hit += 1
    elif num_choice != NUM_WINNER and letter_choice not in LETTER_WINNER: # losing condition: no 3 AND no consonant
        count_miss += 1
    return count_hit, count_num_hit, count_letter_hit, count_miss, count_total

def calc_probability_result(count_hit: int, count_num_hit: int, count_letter_hit: int, count_miss: int, count_total: int) ->tuple:
    hit_probability: float = (count_hit / count_total) * 100
    num_hit_probability: float = (count_num_hit / count_total) * 100
    letter_hit_probability: float = (count_letter_hit / count_total) * 100
    miss_probability: float = (count_miss / count_total) * 100
    return hit_probability, num_hit_probability, letter_hit_probability, miss_probability

def main():
    num_list, letter_list = create_lists()
    count_hit, count_num_hit, count_letter_hit, count_miss, count_total = create_counts()
    rounds = 0
    t1 = perf_counter()
    while rounds < DEF_ROUNDS:
        num_choice, letter_choice = spin_wheel(num_list, letter_list)
        count_hit, count_num_hit, count_letter_hit, count_miss, count_total = count_spins(
            num_choice,
            letter_choice, 
            count_hit, 
            count_num_hit, 
            count_letter_hit, 
            count_miss, 
            count_total)
        rounds += 1
    t2 = perf_counter()
    hit_probability, num_hit_probability, letter_hit_probability, miss_probability = calc_probability_result(count_hit, count_num_hit, count_letter_hit, count_miss, count_total)
    
    print(f"""
        # imagine you spin two wheels at a time
        # one with numbers and one with letters
        # how are the probabilities that on one of the wheels appears a 3 OR a consonant on the other wheel?
        # and how big are the probabilities that no 3 AND no consonant appears?  

        Simulation results after {DEF_ROUNDS:,} rounds:   

        Hit probability: {hit_probability:.2f} % | hits: {count_hit:,.0f}
                        |
                        \u2514\u2192 Numbers probability: {num_hit_probability:.2f} % | hits: {count_num_hit:,.0f}
                        \u2514\u2192 Letters probability: {letter_hit_probability:.2f} % | hits: {count_letter_hit:,.0f}

        Miss probability: {miss_probability:.2f} % | misses: {count_miss:,.0f}
        
        Total counts: {count_total:,.0f}
        """)
    print(f"""
        Performed in {(t2 - t1):.6f} seconds
        """)

if __name__ == '__main__':
    main()       