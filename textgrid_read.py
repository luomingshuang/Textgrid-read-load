#coding:utf-8
import textgrid
import glob
import os

tg = textgrid.TextGrid()
path = './biaozhu2'
txt = 'biaozhu.txt'
tgfiles = glob.glob(os.path.join(path, '*.TextGrid'))
#print(tgfiles)
#i = 0
# for tgfile in tgfiles:
#     tg.read(tgfile)
#     a = tg.tiers
#     print(tgfile, a[i])
#     i += 1
# tg.read(tgfiles[0])
# a = tg.tiers
# print(a[0][1])
# print(a[1][1])
f = open(txt, 'w')
for idx in range(len(tgfiles)):
    #a = None
    tg.read(tgfiles[idx])
    a = tg.tiers
    #print(a)
    f.write(tgfiles[idx]+'\n')
    #print('file:', a[1])
    #print(len(a))
    #for idx in range(int(len(a)/2)):
    #idx = 2*i    #print(a[0])
        #print(idx)
    for m in range(len(a[idx*2])):
        mintime = a[idx*2][m].minTime
        maxtime = a[idx*2][m].maxTime
        text = a[idx*2][m].mark
        #if not str(text) is None:
                #print(idx, int(idx+len(a)/2))
                #print(len(a))
                #print(int(idx+len(a)/2))
                #print(len(a[idx]), len(a[int(idx+len(a)/2)]), m)
        speaker = a[idx*2+1][m].mark
        print(str(mintime) +" " +str(maxtime) + ' ' + str(text) + ' ' + str(speaker))
        txts = str(mintime) +" " +str(maxtime) + ' ' + str(text) + ' ' + str(speaker)
        f.write(txts+'\n')
    f.write('\n')
# a["TEXT"]
f.close()