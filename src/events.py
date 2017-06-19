import datetime

format = "%Y-%m-%dT%H:%M:%S.%f"


class Event(object):
  def __init__(self, event):
    self.key = event['key']
    self.event_time = datetime.datetime.strptime(event['event_time'].replace("Z", ""), format)


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
    self.total_amount = order_event['total_amount']

class CustomerEvent(Event):
  def __init__(self, customer_event):
    Event.__init__(self, customer_event)
    self.customer_id = self.key
    self.last_name = customer_event['last_name']
    self.adr_city = customer_event['adr_city']
    self.adr_state = customer_event['adr_state']
    self.site_visits = 0
    self.total_amount = 0.0
    self.average_ltv = 0.0

  def fromOtherEvent(self, event):
    Event.__init__(self, event)
    self.customer_id = self['key']

  def increaseSiteVisit(self):
    self.site_visits += 1

  def addOrderAmount(self, event):
    self.total_amount += float(event['total_amount'].replace(' USD', ''))

