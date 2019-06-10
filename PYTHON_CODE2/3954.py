M, C, I = list(map(int, input().split()))

programs = list(input())

input_li = list(input())

memory_list = [0] * M

dict = {}

from collections import deque
q = deque()
for _ in range(len(programs)):
    if programs[_] == '[':
        q.append(_)
    elif programs[_] == ']':
        st = q.pop()
        ed = _

        dict[st] = ed
        dict[ed] = st

print(input_li)
print(dict)
pointer = 0
pdx = 0
t = 0


def minus():
    global pdx
    memory_list[pointer]-=1
    pdx+=1

def plus():
    global pdx
    memory_list[pointer]+=1
    pdx+=1

def move_pointer_to_left():
    global pointer, pdx
    pointer -=1
    if pointer == -1:
        pointer = M-1

    pdx += 1

def move_pointer_to_right():
    global pointer, pdx
    pointer +=1
    if pointer == M:
        pointer = 0

    pdx += 1

def teleport_to_close():
    global pdx

    if memory_list[pointer] == 0:
        pdx = dict[pdx]
    else:
        pdx += 1

def teleport_to_open():
    global pdx
    if memory_list[pointer] != 0:
        pdx = dict[pdx]
    else:
        pdx += 1

def print_number():
    global pdx
    pdx += 1

def read_string_and_save_to_memory():
    global pdx
    try:
        _ = input_li.pop(0)
        memory_list[pointer] = ord(_)
    except:
        memory_list[pointer] = 255

    pdx += 1

# while(True):
#
#     if t >= 50000000:
#         print('Loops')
#         break
#     if pdx == C:
#         print('Terminates')
#         break
#
#     ip = programs[pdx]
#     # print(ip)
#
#     if ip =='-':
#         minus()
#     elif ip == '+':
#         plus()
#     elif ip == '<':
#         move_pointer_to_left()
#     elif ip == '>':
#         move_pointer_to_right()
#     elif ip == '[':
#         # print('st',pdx,memory_list[pointer])
#         teleport_to_close()
#     elif ip == ']':
#         # print('ed',pdx,memory_list[pointer])
#         teleport_to_open()
#     elif ip == '.':
#         print_number()
#     elif ip == ',':
#         read_string_and_save_to_memory()
#
#     # print('pdx: ',pdx,'pointer: ',pointer)
#     # print(memory_list[:10])
#     t += 1