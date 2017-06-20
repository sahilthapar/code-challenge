import datetime
import json


def parseDate(date_str):
  """
  Converts date string to datetime object, Expects ISO8601 format
  :param date_str: 
  :return: datetime object
  """
  date_format = "%Y-%m-%dT%H:%M:%S.%f"
  return datetime.datetime.strptime(date_str.replace("Z", ""), date_format)


def parseAmount(amount_str):
  """
    Extracts amount value from amount string
    :param amount_str: 
    :return: amount (float)
  """
  return float(amount_str.replace(' USD', ''))

def enum(**enums):
  """
  # https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
  :param enums: 
  :return: enum
  """
  return type('Enum', (), enums)

def getCustomerId(event):
  """
  Get the customer id from the event
  :param event: 
  :return: id
  """
  return event.get('customer_id') or event.get('key')


def inputReader(filepath):
  """
  To read inputs from files
  :param filepath: Path of file to read
  :return: List of events
  """
  with open(filepath) as data_file:
    data = json.load(data_file)
  return data

def prettyPrint(customers):
  """
  Pretty print top customers
  :param customers: List of customers
  :return: None
  """
  for c in customers:
    print 'Customer_ID: ', c.customer_id
    print 'Last Name: ', c.last_name
    print 'City: ', c.adr_city
    print 'State: ', c.adr_state
    print 'Total Visits: ', c.site_visits
    print 'Total Order: ', c.total_amount
    print 'LTV: ', c.average_ltv
    print "\n===========================\n\n"
