from collections import Counter
from functools import reduce

class Slice:
    def __init__(self, prev_shape, shape):
        self.prev_shape = prev_shape
        self.shape = shape

def parse_input(path):
    with open(path, 'r') as f:
        r, c, _min, _max = list(map(int, f.readline().split()))
        data_frame = list(map(lambda s: s[:-1], f.readlines()))
        return r, c, _min, _max, data_frame

def get_shapes(row, column, min_elem, max_space):
    shapes = []
    for i in range(max_space + 1):
        for j in range(max_space + 1):
            if (min_elem * 2 <= i * j <= max_space and i <= row and j <= column):
                shapes.append([i, j])
    return(shapes)

def put_slice(prev_shape, min_elem, shape, data_frame):
    tomato_counter = 0
    mushr_counter = 0
    for i in range(prev_shape[0], shape[0] + prev_shape[0]):
        for j in range(prev_shape[1], shape[1] + prev_shape[1]):
            if data_frame[i][j] == 'M':
                mushr_counter += 1
            if data_frame[i][j] == 'T':
                tomato_counter += 1

    if (tomato_counter < min_elem or mushr_counter < min_elem):
        return (0)
    return (shape)

def go_forward(prev_shape, shapes, r, c, min_elem, max_space, data_frame):
    one_slice = 0
    for shape in shapes:
        if (prev_shape[0] + shape[0] > r or prev_shape[1] + shape[1] > c):
            continue
        one_slice = put_slice(prev_shape, min_elem, shape, data_frame)
        if (one_slice):
            prev_shape = [prev_shape[0], prev_shape[1] + shape[1]]
            break
    return (prev_shape, one_slice)

def main_algo(r, c, min_elem, max_space, data_frame):
    shapes = sorted(get_shapes(r, c, min_elem, max_space), reverse=True)
    print(shapes)
    answer = []
    prev_shape= [0,0]
    while True:
        prev_shape, one_slice = go_forward(prev_shape, shapes, r, c, min_elem, max_space, data_frame)
        if not one_slice:
            prev_shape[1] -= answer[-1].shape[1]
            shapes.remove(answer[-1].shape)
            prev_shape, one_slice = go_forward(prev_shape, shapes, r, c, min_elem, max_space, data_frame)
            shapes = [answer[-1].shape] + shapes
            answer = answer[:-1]
        if not one_slice:
            break
        answer.append(Slice(prev_shape, one_slice))
        if prev_shape[1] >= c:
            break
    return (answer)

r, c, min_elem, max_space, data_frame = parse_input("./a_example.in")
answer = main_algo(r, c, min_elem, max_space, data_frame)
print(len(answer))
for i in answer:
    print("{} {} {} {}".format(i.prev_shape[0], i.prev_shape[1] - i.shape[1], i.shape[0] - 1, i.prev_shape[1] - 1))

    


# print(min_elem, count_elem)

# shapes = get_shapes(3, 5, 1, 6)
# print(shapes)