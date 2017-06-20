from utils import parseDate

class Datastore():
  def __init__(self):
    self.latest_time = parseDate("1970-01-01T00:00:00.000000")
    self.customers = {}
    self.orders = {}
    self.site_visits = {}
    self.images = {}
    self.events = {}

  def updateLatestTime(self, event):
    self.latest_time = max(self.latest_time, parseDate(event.get('event_time')))

  def add_customer(self, customer):
    self.customers[customer.customer_id] = customer

  def add_order(self, order):
    self.orders[order.key] = order

  def add_site_visit(self, site_visit):
    self.site_visits[site_visit.key] = site_visit

  def add_image(self, image):
    self.images[image.key] = image

  def add_event(self, event):
    self.events[event.key] = event
