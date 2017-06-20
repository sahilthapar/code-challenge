from utils import parseDate

class Datastore():
  """Datastore class

    Stores in-memory event data

    Args:

    Attributes:
        latest_time (datetime): Latest event time recorded
        customers (dict): {customer_id: customer} Contains all customers info
        orders (dict): {key: order} Contains all orders info
        site_visits (dict): {key: site_visit} Contains all site visits information
        images (dict): {key: image} Contains all images info
        events (dict): {key: event} Contains all other event types

    """
  def __init__(self):
    self.latest_time = parseDate("1970-01-01T00:00:00.000000")
    self.customers = {}
    self.orders = {}
    self.site_visits = {}
    self.images = {}
    self.events = {}

  def updateLatestTime(self, event):
    """
    Updates latest time of the datastore
    :param event: 
    :return: 
    """
    self.latest_time = max(self.latest_time, parseDate(event.get('event_time')))

  def add_customer(self, customer):
    """
    Adds a new customer to the datastore
    :param event: 
    :return: 
    """
    self.customers[customer.customer_id] = customer

  def add_order(self, order):
    """
    Adds a new order to the datastore
    :param event: 
    :return: 
    """
    self.orders[order.key] = order

  def add_site_visit(self, site_visit):
    """
    Adds a new site visit to the datastore
    :param event: 
    :return: 
    """
    site_visit_key = site_visit.key + site_visit.customer_id + str(site_visit.event_time)
    self.site_visits[site_visit_key] = site_visit

  def add_image(self, image):
    """
    Adds a new image to the datastore
    :param event: 
    :return: 
    """
    image_key = image.key + image.customer_id
    self.images[image_key] = image

  def add_event(self, event):
    """
    Adds a new event (other event types) to the datastore
    :param event: 
    :return: 
    """
    self.events[event.key] = event
