from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Test(object):

    dataset: object = Dataset()
    service: object = Service()

    def __init__(self, f_name):
        service = self.service
        this = self.dataset
        this.train = service.new_model(self.f_name)
        self.f_name = f_name

    def test(self):
        this = self.this
        print(f'The data type of Train is {type(this.train)}.')
        print(f'Columns of Train is {this.train.columns}.')
        print(f'The top 5 superior data are {this.train.head}.')
        print(f'The top 5 inferior data are {this.train.tail}.')
