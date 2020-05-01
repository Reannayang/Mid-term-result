with open('report.txt','r',encoding= 'utf-8') as f:
    report_all = f.readlines()
    report_all = [l.strip() for l in report_all]
print(report_all)

def sum_mean(v='a 85 75'):
    cell = v.split(sep=' ')
    sum_cell = 0
    for i in range(1,len(cell)):
        sum_cell += int(cell[i])
        mean_cell = sum_cell/(len(cell)-1)
    cell.append(str(sum_cell))
    cell.append(str('%.2f'%(mean_cell)))
    return cell

sums = []
for i in report_all[1:]:
    sums.append(sum_mean(i))
print(sums)
def ranking(ip = ['2','1','3']):
    return int(ip[-2])

sums2 = sorted(sums,key=ranking,reverse=True)
print(sums2)
for i in range(len(sums2)):
    sums2[i] = [str(i+1)]+  sums2[i]
print(sums2)

means =['0','Mean']
for j in range(2,len(sums2[1])):
    sub_sum = 0
    for i in sums2:
        sub_sum += float(i[j])
        sub_mean = sub_sum/len(sums2)
    means.append(str('%.2f'% sub_mean))
print(means)

def failed(ips=['1','2','80','1','10', '3','4','99']):
    for i in range(2,len(ips)-2):
        if float(ips[i]) < 60.0:
            ips[i]='不及格'
    return ips
sums3 = [failed(i) for i in sums2]
print(sums3)
subjects = [i for i in report_all[0].split(sep=' ')]
subjects.append('总分')
subjects.append('均分')
subjects.insert(0,'名次')
sums3.insert(0,subjects)
sums3.insert(1,means)
print(sums3)
def join_rows(list = ['a','b','c']):
    rows = ' '.join(j for j in list)
    return rows
result_data = [join_rows(i) for i in sums3]
print(result_data)
with open('result.txt','w',encoding='utf-8') as f:
    for i in result_data:
        f.write(i)
        f.write('\n')
    f.close()
