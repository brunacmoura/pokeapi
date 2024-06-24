import requests


def get_berry_data(pokeapi_base_url: str):
    response = requests.get(f"{pokeapi_base_url}?limit=100")

    if response.status_code != 200:
        return None, None

    berries = response.json()['results']
    growth_times = []

    for berry in berries:
        berry_detail = requests.get(berry['url']).json()
        growth_times.append(berry_detail['growth_time'])

    return growth_times, [berry['name'] for berry in berries]
