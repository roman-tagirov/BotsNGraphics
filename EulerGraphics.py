import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time

print("Программа построения круговой диаграммы.")
print("Программа готова к использованию.")

anim = ["Идет подсчет.", "Идет подсчет..", "Идет подсчет..."]
namesData =[]
sizeData = []

def animstart():
    for i in range(2):
        print(anim[i])
        time.sleep(1)
    print(anim[-1])
de = False
debug = input("Developer Mode: True or False")
if debug == True:
    de = True

nums = int(input("Введите кол-во переменных (если указано 0, то программа завершится): "))


def process():
    for i in range(nums):
        print("Введите название переменной ",i+1," :")
        names = input()
        namesData.append(names)
        print("Введите размер, долю или величину угла переменной",i+1," :")
        size = float(input())
        sizeData.append(size)
    animstart()
    fig1, ax1 = plt.subplots()

    print("Подсчёт переменных завершен, идёт построение графика. Пожалуйста, подождите. Скорость рендера зависит от количества значений. Процесс рендера может занять до минуты.")
    time.sleep(len(namesData)/5)
    print("Построение графика завершено. Диаграмма покажется через несколько секунд.")
    ax1.pie(sizeData, labels=namesData, autopct='%1.1f%%')
    time.sleep(len(namesData)/10)
    time.sleep(2)
    plt.show()

if nums != 0:
    process()
else:
    print("Завершение..")
    exit()




