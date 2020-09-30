if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    def con(l):
        l1=[]
        for c in l:
            l1.append(float(c))
        return l1
    def ac(l):
        s = 0.0
        for c in l:
            s = s + c
        return s
    for i,j in student_marks.items():
        if query_name==i:
            print("%.2f" % round((ac(con(j)))/3,2))
