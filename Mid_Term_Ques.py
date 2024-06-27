def avg(marks):
    average=sum(marks)
    per=average/len(marks)
    return per

list=[10,20,30]
res=avg(list)
print(res)


nash=(1,4,9,16,25,36)
x =25
idx=0
for i in range(len(nash)):

    if(nash[i]==x):
        idx=i
        break

print(idx)