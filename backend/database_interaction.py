import os
import cv2
import json

# upload image to correct location in database
def upload(name, image, num):
    """
        :type name: str
              image: List[List[List[int]]] (numpy array)
              num: int
        :rtype: N/A
    """
    file_path = "db/imgs/" + name
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_name = name + "-" + str(num) + ".jpg"
    destination = file_path + "/" + file_name
    cv2.imwrite(destination, image)
    return

# adds index to specified label in labels.json
def add_label(index, label):
    """
        :type index: int
              label: str
        :rtype: N/A
    """
    if index == 0:
        labels_json = {}
        labels_json[label] = [index]
    else:
        with open("db/labels.json", "r") as f:
            labels_json = json.load(f)
        if label in labels_json.keys():
            labels_json[label].append(index)
        else:
            labels_json[label] = [index]
    with open("db/labels.json", "w") as f:
        json.dump(labels_json, f, indent=4)
    return

# adds a new person to people.json
def add_person(index, name):
    """
        :type index: int
              name: str
        :rtype: N/A
    """
    if index == 0:
        people_json = {}
        people_json["num_people"] = 1
        people_json["people"] = {}
        people_json["people"][name] = 0
    else:
        with open("db/people.json", "r") as f:
            people_json = json.load(f)
        people_json["num_people"] = people_json["num_people"] + 1
        people_json["people"][name] = index
    with open("db/people.json", "w") as f:
        json.dump(people_json, f, indent=4)
    return

