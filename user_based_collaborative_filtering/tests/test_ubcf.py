from ..user_based_CF import collaborative_filtering


def test_input(input_data):
    assert type(input_data) is dict
    assert len(input_data) > 0


def test_init(input_data):
    assert 1 == 1
