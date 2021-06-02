from titanic.models.service import Service


class Test(object):

    service = Service()

    def __init__(self, f_name):
        service = self.service
        self.this = service.new_model(f_name)

    def test(self):
        print(f'The data type of Train is {type(self.this)}.')
        print(f'Columns of Train is {self.this.columns}.')
        print(f'The top 5 superior data are {self.this.head}.')
        print(f'The top 5 inferior data are {self.this.tail}.')
