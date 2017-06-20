import datetime


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