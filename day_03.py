

# selected = 50
selected = 289326

vals_dict = {"0,0": 1}


def get_sum(p):
    x, y = p
    a_l = vals_dict.get(get_key(x-1, y+1), 0)
    a_c = vals_dict.get(get_key(x, y+1), 0)
    a_r = vals_dict.get(get_key(x+1, y+1), 0)
    l_c = vals_dict.get(get_key(x-1, y), 0)
    b_l = vals_dict.get(get_key(x-1, y-1), 0)
    b_c = vals_dict.get(get_key(x, y-1), 0)
    b_r = vals_dict.get(get_key(x+1, y-1), 0)
    r_c = vals_dict.get(get_key(x+1, y), 0)

    print("stuff to add: {},{},{},{},{},{},{},{}".format(a_l, a_c, a_r, l_c, b_l, b_c, b_r, r_c))

    return a_l + a_c + a_r + l_c + b_l + b_c + b_r + r_c


def get_key(x, y):
    return "{},{}".format(x, y)


def two():
    loop_count = 1
    x = 0
    y = 0

    while True:
        x, y = walk_a_loop((x, y), loop_count)
        if vals_dict[get_key(x, y)] > selected:
            break
        loop_count += 1


def walk_a_loop(p, loop_count):
    x, y = p
    x_factor = 0
    y_factor = 1
    x += 1
    y -= 1
    for edge in range(4):
        for distance in range(2 * loop_count):
            x += x_factor
            y += y_factor
            my_key = get_key(x, y)
            my_sum = get_sum((x, y))
            print("coords are {} with {}".format(my_key, my_sum))

            vals_dict[my_key] = my_sum

            if my_sum > selected:
                print("Yowzah! we hit {}".format(my_sum))
                return x, y

        if edge == 0:
            x_factor = -1
            y_factor = 0
        elif edge == 1:
            x_factor = 0
            y_factor = -1
        elif edge == 2:
            x_factor = 1
            y_factor = 0

    return x, y


def determine_radius(val):
    count = 1
    radius = 0
    while True:
        if val <= count:
            return radius
        else:
            radius += 1
            count = (1 + 2 * radius)**2


def find_dist(num_to_count, radius):
    return abs(num_to_count - radius) + radius


def one():
    radius = determine_radius(selected)
    print("radius is {}".format(radius))

    prev_circle = (1 + 2 * (radius-1)) ** 2
    num_to_count = selected - prev_circle

    # first edge
    if num_to_count <= 2 * radius:
        dist = find_dist(num_to_count, radius)
    # second edge
    elif num_to_count <= 2 * (2 * radius):
        dist = find_dist(num_to_count - (2 * radius), radius)
    # third edge
    elif num_to_count <= 3 * (2 * radius):
        dist = find_dist(num_to_count - (2 * 2 * radius), radius)
    # last edge
    else:
        dist = find_dist(num_to_count - (3 * 2 * radius), radius)

    print("distance is {}".format(dist))


def main():
    # one()
    two()
    print("dict is {}".format(vals_dict))


if __name__ == "__main__":
    main()
