# 데이터를 가져오는 코드
# 디렉토리내의 csv 등의 파일을 가져오는 일을 한다.
from dataclasses import dataclass


@dataclass
class Dataset(object):
    # context 는 파일 경로 등을 지정할 변수
    context: str
    f_name: str
    train: str
    test: str
    # passenger id 는 정수지만, 외부로 들락이는 값은 str 으로 지정한다.
    id: str
    label: str

    @property
    # self._ 의 언더바는 접근을 제한하는 명령이다. private 과 유사
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def f_name(self) -> str: return self._f_name

    @f_name.setter
    def f_name(self, f_name): self._f_name = f_name

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label
