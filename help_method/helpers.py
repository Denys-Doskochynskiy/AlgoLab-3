def duplicate(male_amount_in_each_tribe, female_amount_in_each_tribe):
    return (male * female for male, female in zip(male_amount_in_each_tribe, female_amount_in_each_tribe))


def male_amount_in_family(tribe):
    return len({male_count for male_count in tribe if male_count % 2})


def female_amount_in_family(tribes):
    return len({female_count for female_count in tribes if not female_count % 2})
