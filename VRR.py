turnt = []
no = input('enter number of processes: ')
n=int(no)
qt = input('enter quantum time: ')
process = []
ready_queue = []
waiting_queue = []
auxiliary_queue = []

for i in range(0, n):
    p = input('enter process name: ')
    process = [p]
    bt = input('enter process burst time: ')
    process.append(bt)
    io = input('enter after what time process goes to i/o: ')
    process.append(io)
    at = input('enter process arrival time: ')
    process.append(at)
    process.append(qt)
    ready_queue.append(process)

iot = input('enter waiting (i/o) time: ')
for i in range(0, n):
    j = i + 1
    while j < n:
        if ready_queue[j][3] < ready_queue[i][3]:
            temp = ready_queue[i]
            ready_queue[i] = ready_queue[j]
            ready_queue[j] = temp
        j += 1

print('          ready queue')
print('                     ' + str(ready_queue))

t = 0
i = 0
j = 0
qtime = 0
r = ready_queue[0][4]
rem = [r]
x=ready_queue[0][3]
y=int(x)
for k in range(0, y):
    i += 1
    t += 1
b = ready_queue[0][1]
check = t + int(ready_queue[0][2])
c = check + int(iot)
ck = [c]

while len(ready_queue) > 0 or len(waiting_queue) > 0:
    if j == b:
        turnt.append(i)
        print(i)
        print('----------')
        print(ready_queue[0][0])
        print('executed')
        print('-----------')
        ready_queue.remove(ready_queue[0])
        i += 1
        t += 1
        j = 0
        print('          ready queue')
        print('                     ' + str(ready_queue))
        print('          waiting queue')
        print('                       ' + str(waiting_queue))
        print('          auxiliary queue')
        print('                         ' + str(auxiliary_queue))

        if len(ready_queue) > 0:
            b = ready_queue[0][1]
            check = t + int(ready_queue[0][2])
            c = check + int(iot)
            ck.append(c)

        if ck[0] == i:
            if len(waiting_queue) > 0:
                auxiliary_queue.append(waiting_queue[0])
                waiting_queue.remove(waiting_queue[0])
                print('          ready queue')
                print('                     ' + str(ready_queue))
                print('          waiting queue')
                print('                       ' + str(waiting_queue))
                print('          auxiliary queue')
                print('                         ' + str(auxiliary_queue))
                ready_queue.insert(0, auxiliary_queue[0])
                auxiliary_queue.remove(auxiliary_queue[0])
                check = t + int(ready_queue[0][2])
                c = check + int(iot)
                ck.append(c)
                b = ready_queue[0][1]


    elif t == check:
        print(i)
        print('          ready queue')
        print('                     ' + str(ready_queue))
        print('          waiting queue')
        print('                       ' + str(waiting_queue))
        print('          auxiliary queue')
        print('                         ' + str(auxiliary_queue))

        if len(ready_queue) > 0:
            rem.append(int(ready_queue[0][4]) - qtime)
            waiting_queue.append(ready_queue[0])
            ready_queue.remove(ready_queue[0])
            i += 1
            t += 1
            j = 0
            qtime = 0
            print('          ready queue')
            print('                     ' + str(ready_queue))
            print('          waiting queue')
            print('                       ' + str(waiting_queue))
            print('          auxiliary queue')
            print('                         ' + str(auxiliary_queue))

        if len(ready_queue) > 0:
            check = t + int(ready_queue[0][2])
            c = check + int(iot)
            ck.append(c)
            b = ready_queue[0][1]

        if ck[0] == i:
            ck.remove(ck[0])
            if len(waiting_queue) > 0:
                auxiliary_queue.append(waiting_queue[0])
                waiting_queue.remove(waiting_queue[0])
                print('          ready queue')
                print('                     ' + str(ready_queue))
                print('          waiting queue')
                print('                       ' + str(waiting_queue))
                print('          auxiliary queue')
                print('                         ' + str(auxiliary_queue))
                ready_queue.insert(0, auxiliary_queue[0])
                auxiliary_queue.remove(auxiliary_queue[0])
                check = t + int(ready_queue[0][2])
                c = check + int(iot)
                ck.append(c)
                b = ready_queue[0][1]

    elif qtime == rem[0]:
        print('          ready queue')
        print('                     ' + str(ready_queue))
        print('          waiting queue')
        print('                       ' + str(waiting_queue))
        print('          auxiliary queue')
        print('                         ' + str(auxiliary_queue))

        if len(ready_queue) > 0:
            ap = ready_queue[0]
            ready_queue.remove(ready_queue[0])
            ready_queue.append(ap)
            qtime = 0
            i += 1
            t += 1
            j = 0
            print('          ready queue')
            print('                     ' + str(ready_queue))
            print('          waiting queue')
            print('                       ' + str(waiting_queue))
            print('          auxiliary queue')
            print('                         ' + str(auxiliary_queue))

        if len(ready_queue) > 0:
            check = t + int(ready_queue[0][2])
            c = check + int(iot)
            ck.append(c)
            b = ready_queue[0][1]

        if ck[0] == i:
            ck.remove(ck[0])
            if len(waiting_queue) > 0:
                auxiliary_queue.append(waiting_queue[0])
                waiting_queue.remove(waiting_queue[0])
                print('          ready queue')
                print('                     ' + str(ready_queue))
                print('          waiting queue')
                print('                       ' + str(waiting_queue))
                print('          auxiliary queue')
                print('                         ' + str(auxiliary_queue))
                ready_queue.insert(0, auxiliary_queue[0])
                auxiliary_queue.remove(auxiliary_queue[0])
                check = t + int(ready_queue[0][2])
                c = check + int(iot)
                ck.append(c)
                b = ready_queue[0][1]

    else:
        print(i)
        i += 1
        t += 1
        if len(ready_queue) > 0:
            a=ready_queue[0][1]
            d=int(a)
            d-=1
            ready_queue[0][1] = d
            qtime += 1
            j += 1
            print('          ready queue')
            print('                     ' + str(ready_queue))
            print('          waiting queue')
            print('                       ' + str(waiting_queue))
            print('          auxiliary queue')
            print('                         ' + str(auxiliary_queue))

        if ck[0] == i:
            ck.remove(ck[0])
            if len(waiting_queue) > 0:
                auxiliary_queue.append(waiting_queue[0])
                waiting_queue.remove(waiting_queue[0])
                print('          ready queue')
                print('                     ' + str(ready_queue))
                print('          waiting queue')
                print('                       ' + str(waiting_queue))
                print('          auxiliary queue')
                print('                         ' + str(auxiliary_queue))
                ready_queue.insert(0, auxiliary_queue[0])
                auxiliary_queue.remove(auxiliary_queue[0])

avg = 0
print('turn around time of processes: ')
print(turnt)
print('          ')

for i in range(0, n):
    turnt[i] -= 0
    avg = avg + int(turnt[i])

print('average turn around time is: ' + str(avg / n))