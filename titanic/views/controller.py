# service 필요
from titanic.models.service import Service
from titanic.models.dataset import Dataset


# data handling codes
class Controller(object):

    service = Service()
    dataset = Dataset()

    def modelling(self, train, test) -> object:
        service = self.service
        this = self.preprocessing(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocessing(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        print(f'train의 type은 {type(this.train)}이다.')
        print(f'train의 column은 {this.train.columns}이다.')
        print(f'test의 type은 {type(this.test)}이다.')
        print(f'test의 column은 {this.test.columns}이다.')
        return this