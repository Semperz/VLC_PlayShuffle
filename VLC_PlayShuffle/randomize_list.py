from random import sample
from extract_data_XML import extract_xspf_list
def randomize_xspf():
    assert isinstance(extract_xspf_list(), list)
    randomized_list = sample(extract_xspf_list(), k=(len(extract_xspf_list())))
    assert isinstance(randomized_list, list)
    return randomized_list