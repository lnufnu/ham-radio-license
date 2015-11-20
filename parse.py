from itertools import islice

with open('questionpool.txt') as f:
    lines = f.readlines()

line_counter = 2
offset = 8

# for question_section in islice(lines, 2, 7):

while line_counter < len(lines):
    these_lines = lines[line_counter:(line_counter+offset)]
    import ipdb; ipdb.set_trace()
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
