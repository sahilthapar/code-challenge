class Datastore():
  def __init__(self):
    self.init_time = 0
    self.latest_time = 0
    self.customers = {}
    self.orders = {}
    self.site_visits = {}
    self.images = {}
    self.events = {}

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