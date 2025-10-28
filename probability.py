from random import choice

def creat_lists() ->tuple[list,list]:
    num_list = [1,2,3,2,3,1,2]
    letter_list = ['a','b','c','d','e','f','g','h']
    return num_list, letter_list

def creat_counts() ->tuple[int,int,int]:
    count_hit = 0
    count_miss = 0
    count_total = 0
    return count_hit, count_miss, count_total

def spin_wheel(num_list, letter_list) ->tuple[int,int]:
    num_choice = choice(num_list)
    letter_choice = choice(letter_list)
    return num_choice, letter_choice
    
def count_spins(num_choice, letter_choice, count_hit, count_miss, count_total) ->tuple[int,int,int]:
    if num_choice == 3 or letter_choice in ['b','c','d','f','g','h']:
        count_hit += 1
        count_total += 1
    elif num_choice != 3 and letter_choice not in ['b','c','d','f','g','h']:
        count_miss += 1
        count_total += 1
    return count_hit, count_miss, count_total
       