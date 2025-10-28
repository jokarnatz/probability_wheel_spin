from random import choice
from time import perf_counter

def create_lists() ->tuple[list,list]:
    num_list = [1,2,3,2,3,1,2]
    letter_list = ['a','b','c','d','e','f','g','h']
    return num_list, letter_list

def create_counts() ->tuple[int,int,int]:
    count_hit = 0
    count_miss = 0
    count_total = 0
    return count_hit, count_miss, count_total

def spin_wheel(num_list: list, letter_list: list) ->tuple[int,int]:
    num_choice = choice(num_list)
    letter_choice = choice(letter_list)
    return num_choice, letter_choice
    
def count_spins(num_choice: int, letter_choice: int, count_hit: int, count_miss: int, count_total: int) ->tuple[int,int,int]:
    if num_choice == 3 or letter_choice in ['b','c','d','f','g','h']: # winning conditions: 3 OR a consonant
        count_hit += 1
        count_total += 1
    elif num_choice != 3 and letter_choice not in ['b','c','d','f','g','h']: # losing condition: no 3 AND no konsonant
        count_miss += 1
        count_total += 1
    return count_hit, count_miss, count_total

def calc_probability_result(count_hit: int, count_miss: int, count_total: int) ->tuple[float,float]:
    hit_probability: float = (count_hit / count_total) * 100
    miss_probability: float = (count_miss / count_total) * 100
    return hit_probability, miss_probability

def main():
    num_list, letter_list = create_lists()
    count_hit, count_miss, count_total = create_counts()
    rounds = 0
    t1 = perf_counter()
    while rounds < 1000:
        num_choice, letter_choice = spin_wheel(num_list, letter_list)
        count_hit, count_miss, count_total = count_spins(num_choice,letter_choice, count_hit, count_miss, count_total)
        rounds += 1
    t2 = perf_counter()
    hit_probability, miss_probability = calc_probability_result(count_hit, count_miss, count_total)
    print(f"Hit probability: {hit_probability:.2f}% | hits: {count_hit}\nMiss probability: {miss_probability:.2f}% | misses: {count_miss}\nTotal counts: {count_total}")
    print(f"Performed in {(t2 - t1):.6f} seconds")

if __name__ == '__main__':
    main()       