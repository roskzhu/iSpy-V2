import os
import cv2
import json
import psycopg2
from psycopg2 import sql


# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="your_database",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)
cursor = conn.cursor()

# Upload image to the correct location in the database
def upload(name, image, num):
    """
        :type name: str
              image: List[List[List[int]]] (numpy array)
              num: int
        :rtype: N/A
    """
    # Convert NumPy array to bytea for storage
    image_data = psycopg2.Binary(cv2.imencode('.jpg', image)[1].tobytes())

    # Insert image data into the database
    cursor.execute(
        "INSERT INTO images (name, num, image_data) VALUES (%s, %s, %s)",
        (name, num, image_data)
    )

    conn.commit()
    return

# Adds index to specified label in labels table
def add_label(index, label):
    """
        :type index: int
              label: str
        :rtype: N/A
    """
    # Insert or update label information in the database
    cursor.execute(
        "INSERT INTO labels (index, label) VALUES (%s, %s) ON CONFLICT (label) DO UPDATE SET index = EXCLUDED.index",
        (index, label)
    )

    conn.commit()
    return

# Adds a new person to people table
def add_person(index, name):
    """
        :type index: int
              name: str
        :rtype: N/A
    """
    # Insert or update person information in the database
    cursor.execute(
        "INSERT INTO people (index, name) VALUES (%s, %s) ON CONFLICT (name) DO UPDATE SET index = EXCLUDED.index",
        (index, name)
    )

    conn.commit()
    return

# Close the database connection when the script is done
cursor.close()
conn.close()