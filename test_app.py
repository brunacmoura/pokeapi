import pytest
from app import app
from poke_statistics import calculate_statistics


@pytest.fixture
def growth_times():
    return [1, 2, 3, 4, 5]


def test_should_return_calculated_statistics(growth_times):
    stats = calculate_statistics(growth_times)
    assert stats["min_growth_time"] == 1
    assert stats["max_growth_time"] == 5
    assert stats["mean_growth_time"] == pytest.approx(3.0)
    assert stats["median_growth_time"] == 3
    assert stats["variance_growth_time"] == pytest.approx(2.5)
    assert stats["frequency_growth_time"] == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_should_return_all_berry_stats(client):
    rv = client.get('/berry/allBerryStats')
    assert rv.status_code == 200
    response_data = rv.get_json()
    assert 'berries_names' in response_data
    assert 'min_growth_time' in response_data
    assert 'median_growth_time' in response_data
    assert 'max_growth_time' in response_data
    assert 'variance_growth_time' in response_data
    assert 'mean_growth_time' in response_data
    assert 'frequency_growth_time' in response_data
