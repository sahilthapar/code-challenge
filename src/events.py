import datetime
import time


def parseDate(date_str):
  format = "%Y-%m-%dT%H:%M:%S.%f"
  return datetime.datetime.strptime(date_str.replace("Z", ""), format)

def parseAmount(amount_str):
  return float(amount_str.replace(' USD', ''))

class Event(object):
  def __init__(self, event):
    self.key = event['key']
    self.event_time = parseDate(event['event_time'])


class ImageEvent(Event):
  def __init__(self, image_event):
    super(ImageEvent, self).__init__(image_event)
    self.customer_id = image_event['customer_id']
    self.camera_make = image_event['camera_make']
    self.camera_model = image_event['camera_model']


class SiteVisitEvent(Event):
  def __init__(self, site_visit_event):
    Event.__init__(self, site_visit_event)
    self.customer_id = site_visit_event['customer_id']
    self.tags = site_visit_event['tags']


class OrderEvent(Event):
  def __init__(self, order_event):
    Event.__init__(self, order_event)
    self.customer_id = order_event['customer_id']
    self.total_amount = parseAmount(order_event['total_amount'])

class CustomerEvent(Event):
  def __init__(self, customer_event):
    Event.__init__(self, customer_event)
    self.customer_id = customer_event.get('customer_id', None) or self.key
    self.site_visits = 0
    self.total_amount = 0.0
    self.average_ltv = 0.0

  def increaseSiteVisit(self):
    self.site_visits += 1

  def updateOrderAmount(self, order, existing_orders):
    order_id = order.key
    if order_id in existing_orders and order.event_time > existing_orders[order_id].event_time:
      self.total_amount -= existing_orders[order_id].total_amount
      self.total_amount += order.total_amount
    elif order_id not in existing_orders:
      self.total_amount += order.total_amount

  def updateCustomerProps(self, customer_event):
    event_time = parseDate(customer_event.get('event_time'))
    if ((not hasattr(self, 'latest_update')) or (event_time >= self.latest_update)):
      self.last_name = customer_event.get('last_name', '')
      self.adr_city = customer_event.get('adr_city', '')
      self.adr_state = customer_event.get('adr_state', '')
      self.latest_update = event_time

  def updateAverageLTV(self, latest_time):
    d1_ts = time.mktime(latest_time.timetuple())
    d2_ts = time.mktime(self.event_time.timetuple())
    weeks = int(d1_ts - d2_ts) / (3600 * 24 * 7)
    weeks = 1 if weeks == 0 else weeks
    a = (self.total_amount / self.site_visits) * (self.site_visits / weeks)
    t = 10
    self.average_ltv = 52 * a * t



