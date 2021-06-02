# service, dataset 필요:
# dataset 에서 pre-defined structure 안에 service 이용해서 model 만드는 작업
import pandas as pd
from titanic.models.service import Service
from titanic.models.dataset import Dataset
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


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
        this.id = this.test['PassengerId']
        # self.print_this(this)
        this = service.embarked_nominal(this)
        # self.print_this(this)
        this = service.drop_feature(this, 'Cabin', 'Ticket')
        # self.print_this(this)
        this = service.title_nominal(this)
        # self.print_this(this)
        this = service.drop_feature(this, 'Name')
        this = service.gender_nominal(this)
        this = service.drop_feature(this, 'Sex')
        # self.print_this(this)
        this = service.age_ordinal(this)
        this = service.drop_feature(this, 'Age')
        this = service.fare_band_nominal(this)
        this = service.drop_feature(this, 'Fare')
        # this = service.drop_feature(this, 'SibSp')
        self.print_this(this)
        # Service.fare_examining(this)
        return this

    def learning(self, train, test) -> object:
        this = self.modelling(train, test)
        print(f"Klearn SVC algorithm's accuracy: {self.service.accuracy_by_svm(this)}%")
        print(list(this.label))
        clf = RandomForestClassifier()
        clf = clf.fit(this.train, this.label)
        print(list(clf.predict(this.test)))
        print(this.test)

    def summit(self, train, test):
        this = self.modelling(train, test)
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./data/submission.csv', index=False)

    @staticmethod
    def print_this(this):
        print('*' * 50)
        print(f'train type: {type(this.train)}이다.')
        print(f'train column\n|->{this.train.columns}이다.')
        print(f"train's table\n {this.train.head()}")
        print(f'train null 갯수\n{this.train.isnull().sum()}개')
        print(f'test type: {type(this.test)}이다.')
        print(f'test column\n|->{this.test.columns}이다.')
        print(f"test's table\n{this.train.head()}")
        print(f'test null 갯수\n{this.test.isnull().sum()}개')
        print('*' * 50)
