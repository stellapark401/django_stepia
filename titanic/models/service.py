# 파이썬은 일반 디렉토리 무시하니 root python package 에서 시작한다.
import pandas as pd

from titanic.models.dataset import Dataset


# 결과값을 소비자에게 보여주는 코드
class Service(object):

    dataset = Dataset()

    # csv 형태의 data 를 가져온다.
    # this is used to reference an objective to be processed
    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.f_name = payload
        return pd.read_csv(this.context + this.f_name)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this):
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        print(type(this.train['Embarked']))
        this.train['Embarked'] = this.train['Embarked'].replace('S', 1).replace('C', 2).replace('Q', 3)
        this.test['Embarked'] = this.test['Embarked'].replace('S', 1).replace('C', 2).replace('Q', 3)
        return this

    @staticmethod
    def fare_band_nominal(this):
        return this

    @staticmethod
    def title_nominal(this):
        for dataset in [this.train, this.test]:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in [this.train, this.test]:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map({'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6})
        return this

    @staticmethod
    def fare_examining(this):
        st_train = set(this.train['Fare'])
        st_test = set(this.test['Fare'])
        print(st_test)
        print(st_train)

    @staticmethod
    def gender_nominal(this):
        for data in [this.train, this.test]:
            data['Gender'] = data['Sex'].map({'male': 0, 'female': 1})
        return this

    @staticmethod
    def age_ordinal(this):
        return this

    @staticmethod
    def create_k_fold(this):
        return this
