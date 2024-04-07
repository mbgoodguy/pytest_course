import pytest

from src.candies.schemas import CandySchema
from src.candies.service import CandiesService


# @pytest.fixture(scope="session", autouse=True)
# def setup_db():
#     print(f"{settings.DB_NAME=}")
#     assert settings.MODE == "TEST"
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)

@pytest.fixture(scope="function")
def empty_candies():
    CandiesService.delete_all()


@pytest.fixture
def candies():
    candies = [
        CandySchema(title="candy1", owner="Даниил"),
        CandySchema(title="candy2", state="eaten"),
        CandySchema(title="candy3"),
    ]
    return candies


@pytest.mark.usefixtures("empty_candies")
class TestCandies:
    def test_count_candies(self, candies):
        for candy in candies:
            CandiesService.add(candy)

        assert CandiesService.count() == 3

    def test_list_candies(self, candies):
        for candy in candies:
            CandiesService.add(candy)

        all_candies = CandiesService.list()
        for added_candy in all_candies:
            assert CandySchema(**added_candy) in candies
