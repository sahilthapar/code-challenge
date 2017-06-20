from events import *

def enum(**enums):
  """
  # https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
  :param enums: 
  :return: enum
  """
  return type('Enum', (), enums)

Type = enum(IMAGE='IMAGE', SITE_VISIT='SITE_VISIT', ORDER='ORDER', CUSTOMER='CUSTOMER')


def getCustomerId(event):
  """
  Get the customer id from the event
  :param event: 
  :return: id
  """
  return event.get('customer_id') or event.get('key')


def ingest(event, datastore):
  """
  Insert an event into the datastore
  :param event: 
  :param datastore: 
  :return: datastore: with inserted/updated event
  """
  customer_id = getCustomerId(event)
  customer = datastore.customers.get(customer_id, None)

  # Create new customer if it doesn't exist
  #   Ensures that new customer is created even
  #   if 'new customer' hasn't been received yet
  if not customer:
    customer = CustomerEvent(event)
    datastore.add_customer(customer)

  # Add event to the datastore based on type of event

  if event['type'] == Type.IMAGE:
    image = ImageEvent(event)
    datastore.add_image(image)
  elif event['type'] == Type.SITE_VISIT:
    site_visit = SiteVisitEvent(event)
    customer.increaseSiteVisit()  # Update site visit
    datastore.add_site_visit(site_visit)
  elif event['type'] == Type.ORDER:
    order = OrderEvent(event)
    customer.updateOrderAmount(order, datastore.orders)   # Update order amount
    datastore.add_order(order)
  elif event['type'] == Type.CUSTOMER:
    customer.updateCustomerProps(event)   # Update Customer attributes
    datastore.add_customer(customer)
  else:
    e = Event(event)
    datastore.add_event(e)

  # Update the latest time in the datastore
  datastore.updateLatestTime(event)
  return datastore






