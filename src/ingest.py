from events import *
from datastore import *


def enum(**enums):
  return type('Enum', (), enums)

Type = enum(IMAGE='IMAGE', SITE_VISIT='SITE_VISIT', ORDER='ORDER', CUSTOMER='CUSTOMER')


def getCustomerId(event):
  return (event.get('customer_id') or event.get('key'))


def ingest(event, datastore):
  # Check if the customer already exists

  customer_id = getCustomerId(event)
  customer = datastore.customers.get(customer_id, None)

  if event['type'] == Type.IMAGE:
    image = ImageEvent(event)
    return datastore.add_image(image)
  elif event['type'] == Type.SITE_VISIT:
    site_visit = SiteVisitEvent(event)
    customer.increaseSiteVisit()
    return datastore.add_site_visit(site_visit)
  elif event['type'] == Type.ORDER:
    order = OrderEvent(event)
    customer.addOrderAmount(event)
    return datastore.add_order(order)
  elif event['type'] == Type.CUSTOMER:
    customer = CustomerEvent(event)
    return datastore.add_customer(customer)
  else:
    e = Event(event)
    return datastore.add_event(e)






