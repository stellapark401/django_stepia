from titanic.views.controller import Controller
from titanic.templates.plot import Plot
from titanic.models.service import Service


if __name__ == '__main__':
    controller = Controller()
    plot = Plot('train.csv')

    while True:
        mn = int(input('-show raw data\t\t1\n-data visualization\t2\n-modeling\t\t\t3\n-machine learning\t4\n'
                       '-machine releasing\t5\n-exit\t\t\t\t0'))
        if mn == 1:
            plot.test()
        elif mn == 2:
            plot.draw_survived_dead()
            plot.draw_by_ticket()
            plot.draw_by_embarked()
            plot.draw_by_sex()
        elif mn == 3:
            df = controller.modelling('train.csv', 'test.csv')
        elif mn == 4:
            controller.learning('train.csv', 'test.csv')
        elif mn == 5:
            controller.summit('train.csv', 'test.csv')
        elif mn == 0:
            break
        else:
            print("you've picked a wrong number.")
