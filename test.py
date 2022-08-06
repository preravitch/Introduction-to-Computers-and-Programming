import numpy as np

d= np.loadtxt("grades.tsv", delimiter='\t', dtype=float)

grades = d[:,1:]

credit = np.array([3,2,1,3,3,3])
gpa=grades*credit

sum_gpa=np.sum(gpa,axis=1)

print(sum_gpa)
