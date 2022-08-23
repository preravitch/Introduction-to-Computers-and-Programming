import numpy as np

d= np.loadtxt("grades.tsv", delimiter='\t', dtype=float)

grades = d[:,1:]

credit = np.array([3,2,1,3,3,3])
gpa=grades*credit

sum_gpa=np.sum(gpa,axis=1)

aver=sum_gpa/15


print('Student ID    GPA')
for i in range(20):
    print(int(d[i,0]),end='    ')
    print(f'{aver[i]:.2f}')

