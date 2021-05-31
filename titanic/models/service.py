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
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis=1)
        this.test = this.test.drop([feature], axis=1)
        return this
