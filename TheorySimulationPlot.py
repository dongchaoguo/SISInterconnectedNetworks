import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np

#读取txt格式文件中的邻接矩阵，建立一个list结构，其每个元素也均为list
def readmatrix():
    file = open("A1.txt", "r")
    row = file.readlines()
    list_text = []
    for line in row:
        line = list(line.strip().split(' '))
        s = []
        for i in line:
            s.append(int(i))
        list_text.append(s)
    print(list_text)
    return list_text


def plotfunc1(df):
    fig = plt.figure(facecolor='#BBBBBB', frameon=True)
    plt.plot(df['time'], df['infectionfraction'], linestyle='--', color="blue")
    plt.title('infect vs time')
    plt.xlabel(r'$\tau$')
    plt.ylabel(r'infection fraction $y_{\infty}$')


# Time evolution diagram
# Infection fraction y(t) VS time t
def plotfunc2(parameters):
    # 添加节点的方式建立图结构（无边）
    datafile = r'simulationtimeevolve1f.csv'
    df = pd.read_csv(datafile)
    print(df.head())
    # fig = plt.figure(figsize=(18,18),dpi=480,facecolor='#BBBBBB', frameon=True)
    # fig = plt.figure(facecolor='#BBBBBB', frameon=True)
    # fig = plt.figure()
    plt.plot(df['time'], df['infectionfraction'], linestyle='--', color="blue", linewidth=0.5)

    # plt.title('infect vs time')
    x1 = [0, 1000]
    y1 = [0.595282639*40, 0.595282639*40]
    plt.plot(x1,y1, linestyle='-', color='red', linewidth=4)

    font_dict = dict(fontsize=16, color='k', family='Times New Roman', weight='light')
    plt.xlabel(r'time $t$', fontdict=font_dict)
    plt.ylabel(r'infection number $y(t)$', fontdict=font_dict)
    # plt.xlim((0,200))
    # plt.ylim((0,260))
    # plt.xticks(np.arange(0,200,20))
    # plt.xticks(np.arange(0,1,0.01))
    plt.legend(labels=['single run of simulation', 'steady-state of model'])
    # plt.legend(Labels=['Simulation'])
    font_dict = dict(fontsize=10, color='k', family='Times New Roman', weight='light')
    plt.text(410, 5,
             r'$N=40$, $\beta_{11}=0.4$, $\beta_{12}=\beta_{21}=\beta_{22}=0.02$, ' + "\n" + '$\delta_{11}=\delta_{22}=1$, $\epsilon=10^{-3}$',
             fontdict=font_dict, bbox={'alpha': 0.1, 'pad': 10})

    plt.axis([-10, 1000, 0, 40])
    plt.minorticks_on()
    plt.show()
    # with open('timeevole.csv',mode='r',encoding='utf-8-sig') as f:
    #     reader=csv.reader(f)
    #     header=next(reader)
    #     for rowseq in reader:
    #         print('{}{}:{}={}'.format(header[0], rowseq[0], header[1], rowseq[1]))

# infection fraction as a function of effective infection rate
def plotfunc3(parameters):
    simdatafile1 = r'simulation1e.csv'
    theorydatafile1 = r'theory1b.csv'
    simdatafile2 = r'simulation2e.csv'
    theorydatafile2 = r'theory2a.csv'
    simdf1 = pd.read_csv(simdatafile1)
    theorydf1 = pd.read_csv(theorydatafile1)
    print(simdf1.head())
    print(theorydf1.head())
    simdf2 = pd.read_csv(simdatafile2)
    theorydf2 = pd.read_csv(theorydatafile2)
    print(simdf2.head())
    print(theorydf2.head())

    l1 = plt.scatter(simdf1['beta'], simdf1['infectionfraction'], marker='o', alpha=0.3, c='blue')
    l2 = plt.plot(theorydf1['beta'], theorydf1['infectionfraction'], linewidth=1, linestyle='-.', color="blue")
    l3 = plt.scatter(simdf2['beta'], simdf2['infectionfraction'], marker='d', alpha=0.3, c='red')
    l4 = plt.plot(theorydf2['beta'], theorydf2['infectionfraction'], linewidth=1, linestyle='--', color="red")

    font_dict = dict(fontsize=16, color='k', family='Times New Roman', weight='light')
    plt.xlabel(r'infection rate $\beta_{11}$', fontdict=font_dict)
    plt.ylabel(r'infection fraction $y_{\infty}$', fontdict=font_dict)
    plt.legend(labels=['NoN-NIMFA', 'NoN-NIMFA', r'Simulation $\beta_{12}=0.02$', r'Simulation $\beta_{12}=0.04$'], loc=4)
    font_dict = dict(fontsize=10, color='k', family='Times New Roman', weight='light')
    plt.text(0.1, 0.8, r'$N=40$, $\beta_{12}=\beta_{21}$, ' + r'$\beta_{22}=0.02$, ' +'$\delta_{11}=\delta_{22}=1$, $\epsilon=10^{-3}$' + "\n" + 'Markers are simulations. Curves are theoretical solutions.', fontdict=font_dict, bbox={'alpha': 0.1, 'pad': 10})
    plt.axis([0, 0.5, 0, 1])
    plt.minorticks_on()
    plt.show()


def main():
    #添加节点的方式建立图结构（无边）
    plotfunc2('test.csv')


if __name__ == '__main__':
    main()


# https://www.osgeo.cn/matplotlib/gallery/lines_bars_and_markers/scatter_demo2.html#sphx-glr-gallery-lines-bars-and-markers-scatter-demo2-py
#https://zhuanlan.zhihu.com/p/41781440
# https://matplotlib.org/2.0.2/api/pyplot_api.html#matplotlib.pyplot.plot