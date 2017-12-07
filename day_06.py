# some_input = "0 2   7   0"
some_input = "2 8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"
known_states = set()
state_idx = {}


def find_max(memory):
    """
    :param memory: the list
    :return: the index of the first maximum value
    """
    import operator
    index, value = max(enumerate(memory), key=operator.itemgetter(1))
    return index


def distribute(max_idx, memory):
    val = memory[max_idx]
    length = len(memory)
    memory[max_idx] = 0
    idx = max_idx
    for i in range(val, 0, -1):
        if idx == length - 1:
            idx = 0
        else:
            idx += 1
        memory[idx] += 1


def create_fingerprint(memory):
    # ";".join(memory)
    # [int(i) for i in some_input.split()]
    from functools import reduce
    return reduce(lambda x, y: str(x) + ";" + str(y), memory)


def record_memory_state(memory, step):
    orig_len = len(known_states)
    fingerprint = create_fingerprint(memory)
    known_states.add(fingerprint)
    already_seen = orig_len == len(known_states)
    if not already_seen:
        state_idx[fingerprint] = step
    return already_seen


def process_memory(memory, step):
    max_idx = find_max(memory)
    distribute(max_idx, memory)
    return record_memory_state(memory, step)


def part1(memory):
    done = False
    step = 0
    while not done:
        step += 1
        done = process_memory(memory, step)
        print("memory is now {}".format(memory))
    return step


def test():
    my_list = [-1, 2, 4, 2, 5, 5, 5]
    import operator
    index, value = max(enumerate(my_list), key=operator.itemgetter(1))
    print("test: {}".format(index))

    for i in range(10, 0, -1):
        print("test2: {}".format(i))



def main():
    memory = [int(i) for i in some_input.split()]
    print("memory is {}".format(memory))

    step_count = part1(memory)
    print("It took {} steps".format(step_count))

    fingerprint = create_fingerprint(memory)
    print("The cycle count is {}".format(step_count - state_idx[fingerprint]))

    # test()


if __name__ == "__main__":
    main()
