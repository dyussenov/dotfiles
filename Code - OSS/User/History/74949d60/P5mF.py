"""
Do insert or update. When add new value or
update old - generate output with triggers and shipments
"""


import json
from typing import TextIO, TypedDict


# Product offer
class PartnerContent(TypedDict):
    title: str
    description: str


class ProductOfferBase(TypedDict):
    """offer.schema.json"""

    id: str  # NOT NULL


class ProductOffer(ProductOfferBase, total=False):
    """offer.schema.json"""

    price: int
    stock_count: int
    partner_content: PartnerContent


class Message(TypedDict):
    """message.schema.json"""

    trace_id: str  # NOT NULL
    offer: ProductOffer  # NOT NULL


class ListenedOpts(TypedDict):
    triggers: list[str]
    shipments: list[str]


def _parse_first_line(file: TextIO) -> tuple[int, int]:
    """Get info about number of requests and subscrided services"""

    # get first line from input and create list with elements
    fisrt_line = file.readline().split()
    number_of_services, number_of_requests = fisrt_line[0], fisrt_line[1]

    return int(number_of_services), int(number_of_requests)


def _parse_listeners(
    number_of_services: int, file: TextIO
) -> dict[int, ListenedOpts]:
    """Parse and create database of listenres"""

    listeners_db: dict[int, ListenedOpts] = {}
    for i in range(1, number_of_services + 1):
        second_line = file.readline().split()
        number_of_triggers = int(second_line.pop(0))
        number_of_shipments = int(second_line.pop(0))

        listened_opts: ListenedOpts = {"triggers": [], "shipments": []}

        for j in range(0, number_of_triggers + number_of_shipments):
            if j < number_of_triggers:
                listened_opts["triggers"].append(second_line[j])
            else:
                listened_opts["shipments"].append(second_line[j])

        listeners_db[i] = listened_opts

    return listeners_db


def get_productOffer_by_id(id: str):
    for product_offer in db:
        if product_offer["id"] == id:
            return product_offer
    else:
        return None


def map_updates_to_db(message_json: Message) -> bool:
    """Try to map and if were any changes return true"""
    id = message_json["offer"]["id"]
    db_offer = get_productOffer_by_id(id)
    updated_offer = message_json["offer"]
    changed_column = []

    if not db_offer:
        db.append(updated_offer)
        return True

    if (
        updated_offer.get("price")
        and db_offer.get("price") != updated_offer["price"]
    ):
        db_offer["price"] = updated_offer["price"]
        changed_column.append("price")

    if (
        updated_offer.get("stock_count")
        and db_offer.get("stock_count") != updated_offer["stock_count"]
    ):
        db_offer["stock_count"] = updated_offer["stock_count"]
        changed_column.append("stock_count")

    if (
        updated_offer.get("partner_content")
        and db_offer.get("partner_content") != updated_offer["partner_content"]
    ):
        if db_offer.get("partner_content"):
            if (
                updated_offer["partner_content"].get("title")
                and db_offer["partner_content"].get("title")
                != updated_offer["partner_content"]["title"]
            ):
                db_offer["partner_content"]["title"] = updated_offer[
                    "partner_content"
                ]["title"]
            if (
                updated_offer["partner_content"].get("description")
                and db_offer["partner_content"].get("description")
                != updated_offer["partner_content"]["description"]
            ):
                db_offer["partner_content"]["description"] = updated_offer[
                    "partner_content"
                ]["description"]
        else:
            db_offer["partner_content"] = updated_offer["partner_content"]
        changed_column.append("partner_content")

    if changed_column:
        return True
    return False

def send_notifications(data_to_update, users_list):
    pass

def update_and_notify(number_of_services: int, file: TextIO):
    for line in f:
        a: Message = json.loads(line)
        if map_updates_to_db(a):
            print("Update:", get_productOffer_by_id(a["offer"]["id"]))
            
        else:
            # skip
            print("THE SAME:", get_productOffer_by_id(a["offer"]["id"]))


if __name__ == "__main__":
    db: list[ProductOffer] = []

    with open("input.txt", "r") as f:
        number_of_services, number_of_requests = _parse_first_line(f)

        listeners_db = _parse_listeners(number_of_services, f)
        print("Listeners: ")
        print(listeners_db)

        update_and_notify(number_of_requests, f)
        print()
        print("Your database:")
        print(db)
