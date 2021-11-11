# Finding the percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # for list, we cannot use mean, so use sum / len to get mean value
    test = sum(student_marks[query_name]) / len(student_marks[query_name])
    print('{0:.2f}'.format(test))
    
