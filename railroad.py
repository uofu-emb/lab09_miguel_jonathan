from collections import namedtuple

State = namedtuple('State', ('barrier', 'alarm', 'north', 'south'))
Input = namedtuple('Input', ('northbound_approach', 'southbound_approach',
                   'northbound_depart', 'southbound_depart', 'elapsed'))

def update(s, i):
    out = None
    barrier, alarm, north, south = s
    if i.northbound_approach:
        if not (south or north):
            out = True # reset timer
        north = True
    elif i.northbound_depart:
        north = None
    if i.southbound_approach:
        if not (s.south or s.north):
            out = True # reset timer
        south = True
    elif i.southbound_depart:
        south = None
    if north or south:
        alarm = True # on
        if i.elapsed:
            barrier = True # lowered
    elif barrier:
        barrier = False # raised
        out = True # reset timer
    elif i.elapsed:
        alarm = False # off
    return State(barrier, alarm, north, south), out

headers = ('number', 'arms_down', 'alarm_on', 'northbound_present', 'southbound_present',
           'north_approach', 'south_approach', 'north_depart', 'south_depart', 'elapsed', 'safety_hazard')
hazards = ['']+[25]*3+['']*12 # TODO finish
bad_events = {(0, 2): 19, (0, 3): 19, (0, 4): 24} # TODO finish

def rowstr(entries, fill=' '):
    return f'|{fill}' + f'{fill}|{fill}'.join(str(e).ljust(len(headers[i]), fill) for i, e in enumerate(entries)) + f'{fill}|'

def table_row(n):
    s2n = lambda s: sum(int(bool(s[i])) << (3-i) for i in range(4))
    s = State(n & 8, n & 4, n & 2, n & 1)
    iargs = [None]*5
    entries = [n]
    entries += [int(bool(sv)) for sv in s]
    for i in range(5):
        iargs[i] = True
        if (n, i) in bad_events:
            entries.append(bad_events[(n, i)])
        else:
            entries.append(s2n(update(s, Input(*iargs))[0]))
        iargs[i] = None
    entries.append(hazards[n])
    return rowstr(entries)

print(rowstr(headers))
print(rowstr(['']*len(headers), '-'))
for n in range(16):
    print(table_row(n))

print()

with open('Invariants.md', 'r') as file:
    s = file.read()
    print(s[:s.find('**', s.find('16.'))].strip())
