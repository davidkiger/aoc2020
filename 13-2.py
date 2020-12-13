from sympy.ntheory.modular import crt

timestamp, bus_list = [x.strip() for x in open('13-1.in').readlines()]
buses = [x for x in bus_list.split(',')]

in_service = [int(x) for x in buses if x != 'x']
times = [-1 * buses.index(str(x)) for x in in_service]

print(crt(in_service, times)[0])

'''
The only reason I got this was courtesy of the reddit thread talking about
the Chinese Remainder Theorum. I wouldn't have even known what the hell to
search for. I very much dislike problems of this type where you either know
the math trick, or you don't.

However, this person is incredible: https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfnhrk3/
'''
