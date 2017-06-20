import datetime


def parseDate(date_str):
  date_format = "%Y-%m-%dT%H:%M:%S.%f"
  return datetime.datetime.strptime(date_str.replace("Z", ""), date_format)


def parseAmount(amount_str):
  return float(amount_str.replace(' USD', ''))