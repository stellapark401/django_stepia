# 파이썬은 일반 디렉토리 무시하니 root python package 에서 시작한다.
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
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
        this.train['Embarked'] = this.train['Embarked'].replace('S', 1).replace('C', 2).replace('Q', 3)
        this.test['Embarked'] = this.test['Embarked'].replace('S', 1).replace('C', 2).replace('Q', 3)
        return this

    @staticmethod
    def fare_band_nominal(this):
        this.train['Fare'] = this.train['Fare'].fillna(0)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4, labels=[2, 4, 6, 8])
        # bins = list(pd.qcut(this.train['Fare'], 4, labels=[1, 2, 3, 4], retbins=True))[1]
        this.test['Fare'] = this.test['Fare'].fillna(0)
        this.test['FareBand'] = pd.cut(this.test['Fare'], bins=(-0.001, 7.9104, 14.4542, 31., 512.3292), labels=[2, 4, 6, 8])
        # print(list(this.test['FareBand']))
        # (-0.001, 7.9104, 14.4542, 31., 512.3292)
        return this

    @staticmethod
    def title_nominal(this):
        for dataset in this.train, this.test:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in this.train, this.test:
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
        for data in (this.train, this.test):
            data['Age'] = data['Age'].fillna(-0.5)
            bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
            labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
            data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels)
            data['AgeGroup'] = data['AgeGroup'].map({'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5, 'Adult': 6, 'Senior': 7})
        return this

    @staticmethod
    def create_k_fold():
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def accuracy_by_svm(this):
        score = cross_val_score(SVC(), this.train, this.label, cv=KFold(n_splits=10, shuffle=True, random_state=0)
                                , n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)
