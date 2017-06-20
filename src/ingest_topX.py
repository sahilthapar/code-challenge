import heapq

from events import *
from utils import getCustomerId, enum

Type = enum(IMAGE='IMAGE', SITE_VISIT='SITE_VISIT', ORDER='ORDER', CUSTOMER='CUSTOMER')

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


def topXSimpleLTVCustomers(x, database):
  """
  Returns the top x customers based on simples ltv based on a heap 
  https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
  :param x: number of top customers desired
  :param database: 
  :return: top x customers based on simple ltv
  """
  minh = []
  for customer_id, customer in database.customers.items():
    customer.updateAverageLTV(database.latest_time)
    heapq.heappush(minh, (-customer.average_ltv, customer))
  return [c for ltv, c in minh[:x]]





