from events import *


def enum(**enums):
  return type('Enum', (), enums)

Type = enum(IMAGE='IMAGE', SITE_VISIT='SITE_VISIT', ORDER='ORDER', CUSTOMER='CUSTOMER')


def getEvent(event):
  print Type.IMAGE
  if event['type'] == Type.IMAGE:
    return ImageEvent(event)
  elif event['type'] == Type.SITE_VISIT:
    return SiteVisitEvent(event)
  elif event['type'] == Type.ORDER:
    return OrderEvent(event)
  elif event['type'] == Type.CUSTOMER:
    return CustomerEvent(event)
  else:
    return Event(event)


def ingest(e, D):
  event = getEvent(e)
  print event
  return D
