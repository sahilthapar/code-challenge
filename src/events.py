import time
from utils import *


class Event(object):
  """Event class

    Records an event

    Args:
        event (obj): event object

    Attributes:
        key (str): Unique identifier for event
        event_time (datetime): Event record time

    """
  def __init__(self, event):
    self.key = event.get('key')
    self.event_time = parseDate(event.get('event_time'))


class ImageEvent(Event):
  """ImageEvent extends Event class

      Records an image event

      Args:
          image_event (obj): event object

      Attributes:
          customer_id (str): Customer id of the customer who uploaded the image
          camera_make (str): Camera make of the image source
          camera_model (str): Camera model of the image source
    """
  def __init__(self, image_event):
    super(ImageEvent, self).__init__(image_event)
    self.customer_id = image_event.get('customer_id')
    self.camera_make = image_event.get('camera_make', '')
    self.camera_model = image_event.get('camera_model', '')


class SiteVisitEvent(Event):
  """SiteVisitEvent extends Event class

      Records a site visit

      Args:
          site_visit_event (obj): event object

      Attributes:
          customer_id (str): Customer id of the customer who visited the site
          tags (list): Tags for the visit
  """
  def __init__(self, site_visit_event):
    Event.__init__(self, site_visit_event)
    self.customer_id = site_visit_event.get('customer_id')
    self.tags = site_visit_event.get('tags', [])


class OrderEvent(Event):
  """OrderEvent extends Event class

      Records an order

      Args:
          order_event (obj): event object

      Attributes:
          customer_id (str): Customer id of the customer who placed an order
          total_amount (float): Total order amount
  """
  def __init__(self, order_event):
    Event.__init__(self, order_event)
    self.customer_id = order_event.get('customer_id')
    self.total_amount = parseAmount(order_event.get('total_amount', 0))


class CustomerEvent(Event):
  """CustomerEvent extends Event class

      Records an customer

      Args:
          customer_event (obj): event object

      Attributes:
          customer_id (str): Customer id of the customer who placed an order
          last_name (str): Customer's last name
          adr_city (str): Customer's city
          adr_state (str): Customer's state
          site_visits (str): Total site visits for the customer
          total_amount (float): Total order amount for the customer
          average_ltv (float): Average LTV of the customer
          latest_update (datetime): Last time the customer was updated
  """
  def __init__(self, customer_event):
    Event.__init__(self, customer_event)
    self.customer_id = customer_event.get('customer_id', None) or self.key
    self.last_name = customer_event.get('last_name', '')
    self.adr_city = customer_event.get('adr_city', '')
    self.adr_state = customer_event.get('adr_state', '')
    self.site_visits = 0
    self.total_amount = 0.0
    self.average_ltv = 0.0
    self.latest_update = None

  def increaseSiteVisit(self):
    """
    Increments the customer's site visits by 1
    :return: 
    """
    self.site_visits += 1

  def updateOrderAmount(self, order, existing_orders):
    """
    Update total order amount for the client based on an order
    Updates only if the order is new and no future updates have been received
    :param order: Order to use for update
    :param existing_orders: Existing orders for the customer
    :return: 
    """
    order_id = order.key
    if order_id in existing_orders and order.event_time > existing_orders[order_id].event_time:
      self.total_amount -= existing_orders[order_id].total_amount
      self.total_amount += order.total_amount
    elif order_id not in existing_orders:
      self.total_amount += order.total_amount

  def updateCustomerProps(self, customer_event):
    """
    Update customer attributes.
    Updates only if the update is newer than last update
    :param customer_event: Event to base the update on
    :return: 
    """
    event_time = parseDate(customer_event.get('event_time'))
    if (not self.latest_update) or (event_time >= self.latest_update):
      self.latest_update = event_time
      self.last_name = customer_event.get('last_name', '')
      self.adr_city = customer_event.get('adr_city', '')
      self.adr_state = customer_event.get('adr_state', '')

  def updateAverageLTV(self, latest_time):
    """
    Updates the average ltv of a customer based on the latest time in the datasotre
    :param latest_time: latest time in the datastore
    :return: 
    """
    d1_ts = time.mktime(latest_time.timetuple())
    d2_ts = time.mktime(self.event_time.timetuple())
    weeks = int(d1_ts - d2_ts) / (3600 * 24 * 7)
    a = (self.total_amount / self.site_visits) * (self.site_visits / weeks) if weeks else 0
    t = 10
    self.average_ltv = 52 * a * t



