# Exercise #1
# Using Trello API documentation and Python requests module implement functions for the following actions:
#
# Creating a new Board (you can reuse function from the lecture)
# Creating a new List on a Board
# Creating a new Card in this list
# Updating a description on the card
# Deleting created card
# Archiving the list

import requests

APIKEY = "15626714d4dbeb54f064c5b86a881006"
TOKEN = "a16515fa84517ba837f27a3ef16ace4c4d538a4a59a1a56c18598d817eff0485"

URL = "https://api.trello.com/"


def get_user_boards():
    """
    This function returns information about all boards that the user has access to
    :return: list of dict
    """
    endpoint = "1/members/me/boards"
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=URL + endpoint, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    # print(response_json)
    return response_json


def get_board_lists(id_board):
    """
    This function returns information about all boards that the user has access to
    :return: list of dict
    :param id_board: id of the board with lists
    """
    endpoint = "1/boards/{}/lists".format(id_board)
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=URL + endpoint, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    # print(response_json)
    return response_json


def get_list_cards(id_list):
    """
    This function returns information about all boards that the user has access to
    :return: list of dict
    :param id_list: id of the list with cards
    """
    endpoint = "1/lists/{}/cards".format(id_list)
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=URL + endpoint, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    # print(response_json)
    return response_json


def get_board_id(name):
    """
    Returns the id of the specified board
    :param name: name of the board
    :return: int
    """
    id = None
    response = get_user_boards()
    for board in response:
        if board['name'] == name:
            id = board['id']
            break

    if id is None:
        print("No board found with the name: {}".format(name))
    return id


def get_list_id(board_id, list_name):
    """
    Returns the id of the specified list
    :param board_id: id of the board with list
    :param list_name: name of the list
    :return: int
    """
    id = None
    response = get_board_lists(board_id)
    for lists in response:
        if lists['name'] == list_name:
            id = lists['id']
            break

    if id is None:
        print("No list found with the name: {}".format(name))
    return id


def get_card_id(list_id, card_name):
    """
    Returns the id of the specified card
    :param list_id: id of the list with card
    :param card_name: name of the card
    :return: int
    """
    id = None
    response = get_list_cards(list_id)
    for cards in response:
        if cards['name'] == card_name:
            id = cards['id']
            break

    if id is None:
        print("No card found with the name: {}".format(name))
    return id


def update_board(name, **kwargs):
    """
    Updates boards information
    :param name: name of the board to be updated
    :param kwargs: board's parameters to be updated. The ful list is here: https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-put
    :return: None
    """
    board_id = get_board_id(name)

    endpoint = "{}1/boards/{}".format(URL, board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    for key, value in kwargs.items():
        params[key] = value

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def update_card(list_id, name, **kwargs):
    """
    Updates boards information
    :param list_id: id of the list with card
    :param name: name of the board to be updated
    :param kwargs: board's parameters to be updated. The ful list is here: https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-put
    :return: None
    """
    card_id = get_card_id(list_id, name)

    endpoint = "{}1/cards/{}".format(URL, card_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    for key, value in kwargs.items():
        params[key] = value

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def archive_list(list_id):
    """
    Deleted the board
    :param list_id: id of the list with card
    :return:  None
    """
    endpoint = "{}1/lists/{}/closed".format(URL, list_id)
    # endpoint = "{}1/lists/me/closed".format(URL)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'value': 'true'
    }

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def delete_board(name):
    """
    Deleted the board
    :param name: board name
    :return:  None
    """
    board_id = get_board_id(name)
    endpoint = "{}1/boards/{}".format(URL, board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }

    response = requests.request(
        "DELETE",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def delete_card(list_id, name):
    """
    Deleted the board
    :param list_id: id of the list with card
    :param name: board name
    :return:  None
    """
    card_id = get_card_id(list_id, name)
    endpoint = "{}1/cards/{}".format(URL, card_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }

    response = requests.request(
        "DELETE",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def create_new_board(name):
    """
    Create a new board
    :param name: new board name
    :return: None
    """
    endpoint = "1/boards/"
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    response = requests.post(url=URL + endpoint, json=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def create_new_list(name, id_board):
    """
    Create a new list
    :param name: new list name
    :param idBoard: id of board to place new list
    :return: None
    """
    endpoint = "1/lists/"
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name,
        'idBoard': id_board
    }
    response = requests.post(url=URL + endpoint, json=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def create_new_card(name, id_list):
    """
    Create a new list
    :param name: new card name
    :param idList: id of the list to place a card
    :return: None
    """
    endpoint = "1/cards"
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name,
        'idList': id_list
    }
    response = requests.post(url=URL + endpoint, json=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


if __name__ == "__main__":
    # get_user_boards()

    # create_new_board("Test Automation")
    id_board = get_board_id("Test Automation")
    # create_new_list("Chapter 1", id_board)  # creating a new list
    id_list = get_list_id(id_board, "Chapter 1")
    # create_new_card("Paragraph 1", id_list) # creating a new card
    # get_list_cards(id_list)
    # id_card = get_card_id(id_list, "Paragraph 1")
    # update_card(id_list, "Paragraph 1", desc="This is a description of the card")
    # delete_card(id_list, "Paragraph 1")
    archive_list(id_list)

    # update_board("Test Automation", desc="Add items to finish automation")
    # delete_board("Test Automation")
