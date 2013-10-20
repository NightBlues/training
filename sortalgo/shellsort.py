__author__ = 'NightBlues'

def pop_and_insert_with_step(data, src_pos, dst_pos, d):
    if src_pos != dst_pos:
        cur = data[src_pos]
        j_next = None
        for j in reversed(range(dst_pos, src_pos+1, d)):
            if j_next is not None:
                data[j_next] = data[j]
            j_next = j
        data[dst_pos] = cur

def find_place_for_element_with_step(data, elem_pos, d, comp):
    place_for_elem=elem_pos
    while place_for_elem>=d and comp(data[place_for_elem-d],  data[elem_pos]):
        place_for_elem -= d
    return place_for_elem


def shell_sort(data, d=1, comp=lambda a, b: a > b):
    #    cur_sublist_i is a shift of list
    for cur_sublist_i in range(d):
        for i in range(cur_sublist_i, len(data), d):
            index_to_insert = find_place_for_element_with_step(data, i, d, comp)
            pop_and_insert_with_step(data, i, index_to_insert, d)
    if d > 1:
        shell_sort(data, d/2, comp)
