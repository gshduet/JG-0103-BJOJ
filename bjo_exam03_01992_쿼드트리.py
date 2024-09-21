import sys

sinput = sys.stdin.readline

def divide_quadrants(n: int, data: list) -> list:
    if n == 2:
        return [''.join(data)]

    half = n // 2

    quadrant_a = [row[:half] for row in data[:half]]
    quadrant_b = [row[half:] for row in data[:half]]
    quadrant_c = [row[:half] for row in data[half:]]
    quadrant_d = [row[half:] for row in data[half:]]

    result = []
    for quadrant in [quadrant_a, quadrant_b, quadrant_c, quadrant_d]:
        result.extend(divide_quadrants(half, quadrant))

    return result

def compress_quadtree(quads):
    answer = ''

    for v in quads:
        match v:
            case '1111' | '0000':
                answer += v[0]

            case _:
                answer += f"({v})"

    return f"({answer})"



# nums:int = int(sinput())
# data:list = [''.join(input().strip()) for _ in range(nums)]
nums = 4
data = ['1111', '1111', '0001', '0001']
# nums = 8
# data = ['11110000', '11110000', '00011100', '00011100', '11110000', '11110000', '11110011', '11110011']

divided_screen = divide_quadrants(nums, data)
print(divided_screen)
print(len(divided_screen))
print(compress_quadtree(divided_screen))