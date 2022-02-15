import urllib.request
import csv
import argparse
import datetime
import logging

def downloadData(url):
    with urllib.request.urlopen(url) as response:
       web_data = response.read().decode('utf-8')

    return web_data


def processData(file_content):
    user_data = {}

    for data_info in file_content.split("\n"):
        if len(data_info) == 0:
            continue

    identifier, name, birthday = data_info.split(",")
    if identifier == "id":
        id_int = int(identifier)
    try:
        true_birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")
        person_data[id_int] = (name, true_birthday)
    except ValueError as e:
        print(f"error parsing {birthday}")

    return user_data


def displayPerson(id, userData):
    try:
        name, birthday = userData[id]
        print(f"Person #{id} is {name} with a birthday of {birthday:%Y-%m-%d}")
    except KeyError:
        print(f"No user found with that id")


def main(url):
    print(f"Running main with URL = {url}...")
    detail = downloadData(url)
    print(detail)
    while True:
        id = int(input("Enter an ID:"))
        if id > 0:
            print(id)
            break
        else:
            print("No user found with that id")
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)

