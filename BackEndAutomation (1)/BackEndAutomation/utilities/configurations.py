import configparser
import mysql.connector
from mysql.connector import Error

"""
configparser for reading configuration files (like .ini files).
mysql.connector for connecting and working with a MySQL database.
Error to handle database connection errors.
"""


def getConfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config


# connect_config a Dictionary
connect_config = {
    "user": getConfig()["SQL"]["user"],
    "password": getConfig()["SQL"]["password"],
    "host": getConfig()["SQL"]["host"],
    "database": getConfig()["SQL"]["database"],
}
"""
Source: Reads values from the [SQL] section of the properties.ini file using the getConfig() function.
"""


def getPassword():
    return "Srinath19830G"


def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)


def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row
