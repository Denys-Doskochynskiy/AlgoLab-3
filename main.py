from reader_writer.writer import create_write_to_file
from help_method.helpers import duplicate
from help_method.helpers import female_amount_in_family
from help_method.helpers import male_amount_in_family
from reader_writer.reader import read_graph_from_file
from reader_writer.reader import read_len_of_graph_from_file
from help_method.brute_force import brute_force


def wedd(people_list, len_of_graph):
    print(people_list)

    families = brute_force(people_list, len_of_graph)

    male_amount_in_each_family = [male_amount_in_family(family) for family in families]

    female_amount_in_each_family = [female_amount_in_family(family) for family in families]
    print(families)
    print(male_amount_in_each_family)
    print(female_amount_in_each_family)

    all_pair = sum(male_amount_in_each_family) * sum(female_amount_in_each_family)

    duplicate_pair = sum(duplicate(male_amount_in_each_family, female_amount_in_each_family))

    create_write_to_file(all_pair - duplicate_pair)

    return all_pair - duplicate_pair


if __name__ == '__main__':
    graph = []
    graph = read_graph_from_file("test.in", graph)

    print("How much group: " + str(len(graph)) + " ;")
    res = wedd(graph, read_len_of_graph_from_file("test.in"))
    print(res)
