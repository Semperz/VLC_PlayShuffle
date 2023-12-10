from random import sample

def randomize_xspf(xspf_list):
    try:
        randomized_list = sample(xspf_list, k=(len(xspf_list)))
        return randomized_list
    except AssertionError as notListError:
        print(f'Error: {notListError}')
        return None