from itertools import islice

with open('questionpool.txt') as f:
#    import ipdb; ipdb.set_trace()
    lines = f.readlines()
#    calling .split("\n") on readlines does not work because .split not list method
#    lines = lines.rstrip('\n') this does not work because rstrip is not list method



data_set = []
for line in lines:
    line = line.rstrip('\n')
    line = line.rstrip('\r')
    data_set.append(line)

import ipdb; ipdb.set_trace()


line_counter = 2
offset = 8

# for question_section in islice(lines, 2, 7):

while line_counter < len(data_set):
    these_lines = data_set[line_counter:(line_counter+offset)]
    for line in these_lines:
        # correct_answer = question_section[0].split()[1].strip('()')
        question = line
        answer_a = line.lstrip('A. ')
        answer_b = line.lstrip('B. ')
        answer_c = line.lstrip('C. ')
        answer_d = line.lstrip('D. ')

    offset += offset
print correct_answer
print question
print answer_a
