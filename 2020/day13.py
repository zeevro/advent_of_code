from itertools import count
import time

notes = '''1002461
29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,521,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,x,x,601,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,19'''

leave_ts, busses = notes.splitlines()
leave_ts = int(leave_ts)
busses = [int(b) for b in busses.split(',') if b != 'x']

for dt, ts in enumerate(count(leave_ts)):
    for bus in busses:
        if ts % bus == 0:
            print(bus * dt)
            break
    else:
        continue
    break

# busses = [None if b == 'x' else int(b) for b in notes.splitlines()[1].split(',')]
busses = [(int(b), dt) for dt, b in enumerate(notes.splitlines()[1].split(',')) if b != 'x']
step, step_dt = max(busses)
start_ts = 200000000000000

start_time = time.time()
for n, ts in enumerate(count(start_ts - step_dt - start_ts % step, step)):
    # print(ts, [(ts + dt) % b == 0 for b, dt in busses])
    if n % 10000000 == 0:
        print(time.time() - start_time, ts)
    if all((ts + dt) % b == 0 for b, dt in busses):
        print(ts)
        break


#print(', '.join(f'(x + {dt}) mod {b}' for b, dt in busses))
