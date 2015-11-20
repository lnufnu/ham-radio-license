with open('questionpool.txt') as f:
    lines = f.readlines()
    lines = lines[2:]
    for line in lines:
        correct_answer = line.split()[1].strip('()')
        question = f.next()
        answer_a = f.next().lstrip('A. ')
        answer_b = f.next().lstrip('B. ')
        answer_c = f.next().lstrip('C. ')
        answer_d = f.next().lstrip('D. ')
    print correct_answer
    print question
    print answer_a
