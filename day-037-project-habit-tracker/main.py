from datetime import *
import os
import requests

USERNAME = "your_username"
TOKEN = os.environ.get("TOKEN_PIXELA")
GRAPH_ID = "graph_id"

pixela_endpoint = "https://pixe.la/v1/users"

HEADERS = {
        "X-USER-TOKEN": TOKEN
    }


def create_account():
    """Create a new Pixela account passing the data from constants."""
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_graph():
    """Create a new graph within the account passing the data from constants."""
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Graph Name",
        "unit": "Unit",
        "type": "int",
        "color": "color"
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print(response.text)


def post_pixel(quantity: str):
    """Post a new pixel in the graph for today, passing the constants as data."""
    today = datetime.now()

    pixel_config = {
        "date": today.strftime("%Y%m%d"),
        "quantity": quantity
    }

    response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}", json=pixel_config, headers=HEADERS)
    response.raise_for_status()


def update_pixel(quantity: str):
    """Update a pixel in the graph for yesterday's date."""
    yesterday = (date.today() - timedelta(days=1)).strftime("%Y%m%d")

    pixel_update = {
        "quantity": quantity
    }

    response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}",
                            json=pixel_update,
                            headers=HEADERS)
    response.raise_for_status()


def delete_pixel():
    """Delete a pixel in the graph for yesterday's date."""
    today = date.today().strftime("%Y%m%d")

    response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}", headers=HEADERS)
    response.raise_for_status()


# --------------- CALL FUNCTION BELOW -------------------------
# create_account()
# create_graph()
# post_pixel()
# update_pixel()
# delete_pixel()
