from titanic.models.service import Service
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc('font', family = font_manager.FontProperties(fname='C:\Windows\Fonts\H2GTRE.ttf').get_name())


# 데이터 시각화해서 보여주는 코드
class Plot(object):

    service: object = Service()

    def __init__(self, f_name):
        self.this = self.service.new_model(f_name)

    def test(self):
        print(f'The data type of Train is {type(self.this)}.')
        print(f'Columns of Train is {self.this.columns}.')
        print(f'The top 5 superior data are {self.this.head}.')
        print(f'The top 5 inferior data are {self.this.tail}.')

    def draw_survived_dead(self):
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        self.this['Survived'].value_counts().plot.pie(explode=(0, 0.1), autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0:dead vs 1: survived')
        ax[0].set_ylabel('')
        ax[1].set_title('0:dead vs 1: survived')
        sns.countplot('Survived', data=self.this, ax=ax[1])
        plt.show()

    def draw_by_ticket(self):
        this = self.this
        this['Survival'] = this['Survived'].replace(0, 'dead').replace(1, 'survived')
        this['seat_grade'] = this['Pclass'].replace(1, 'first class')\
            .replace(2, 'business').replace(3, 'economy')
        sns.countplot(data=this, x='seat_grade', hue='Survival')
        plt.show()

    def draw_by_sex(self):
        this = self.this
        this['Survival'] = this['Survived'].replace(0, 'dead').replace(1, 'survived')
        sns.countplot(data=this, x='Sex', hue='Survival')
        plt.show()

    def draw_by_embarked(self):
        this = self.this
        this['Survival'] = this['Survived'].replace(0, 'dead').replace(1, 'survived')
        this['Boarded from'] = this['Embarked'].replace('C', 'Cherbourg')\
            .replace('S', 'Southampton').replace('Q', 'Queenstown')
        sns.countplot(data=this, x='Boarded from', hue='Survival')
        plt.show()
