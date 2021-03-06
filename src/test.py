import unittest
from ingest_topX import *
from datastore import *
from utils import *


class Test(unittest.TestCase):

  def setUp(self):
    self.D = Datastore()

  def test_new_customer_event(self):
    events = inputReader('../input/single_event.txt')
    ingest(events, self.D)
    self.assertIn("96f55c7d8f42", self.D.customers)

  def test_multiple_events(self):
    events = inputReader('../input/multiple_events.txt')
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.site_visits), 1)
    self.assertEqual(len(self.D.images), 1)
    self.assertEqual(len(self.D.orders), 1)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 12.34)

  def test_update_customer(self):
    events = inputReader('../input/update_customer.txt')
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.customers), 1)
    self.assertEqual(len(self.D.site_visits), 1)
    self.assertEqual(len(self.D.images), 1)
    self.assertEqual(len(self.D.orders), 1)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 12.34)

    self.assertEqual(self.D.customers["96f55c7d8f42"].adr_state, "OH")

  def test_update_only_latest_customer(self):
    events = inputReader('../input/update_latest_customer.txt')
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.customers), 1)
    self.assertEqual(len(self.D.site_visits), 1)
    self.assertEqual(len(self.D.images), 1)
    self.assertEqual(len(self.D.orders), 1)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 12.34)

    self.assertEqual(self.D.customers["96f55c7d8f42"].adr_state, "AK")


  def test_other_event_before_customer(self):
    events = inputReader('../input/other_event_before_customer.txt')
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.customers), 1)
    self.assertEqual(len(self.D.site_visits), 1)
    self.assertEqual(len(self.D.images), 1)
    self.assertEqual(len(self.D.orders), 1)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 12.34)

  def test_order_update(self):
    events = inputReader('../input/order_update.txt')
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.customers), 1)
    self.assertEqual(len(self.D.site_visits), 1)
    self.assertEqual(len(self.D.images), 1)
    self.assertEqual(len(self.D.orders), 1)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 14.34)

  def test_multiple_customers_orders_site_visits(self):
    events = inputReader('../input/multiple_customers_order_site_visits.txt')
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertIn("97f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.customers), 2)
    self.assertEqual(len(self.D.site_visits), 2)
    self.assertEqual(len(self.D.images), 2)
    self.assertEqual(len(self.D.orders), 2)
    self.assertIn("18d84e5d1a43", self.D.orders)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 2)
    self.assertEqual(self.D.customers["97f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 14.34)
    self.assertEqual(self.D.customers["97f55c7d8f42"].total_amount, 12.34)

    top_two = topXSimpleLTVCustomers(2, self.D)
    self.assertEqual(top_two[0].average_ltv, (52 * (14.34 / 2) * 2 * 10))
    self.assertEqual(top_two[1].average_ltv, (52 * 12.34 * 1 * 10))

  def test_multiple_customers_orders_site_visits_0_weeks(self):
    events = inputReader('../input/multiple_customers_order_site_visits_0_weeks.txt')
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertIn("97f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.customers), 2)
    self.assertEqual(len(self.D.site_visits), 2)
    self.assertEqual(len(self.D.images), 2)
    self.assertEqual(len(self.D.orders), 2)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 2)
    self.assertEqual(self.D.customers["97f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 14.34)
    self.assertEqual(self.D.customers["97f55c7d8f42"].total_amount, 12.34)

    top_two = topXSimpleLTVCustomers(2, self.D)
    self.assertEqual(top_two[0].average_ltv, 0)
    self.assertEqual(top_two[1].average_ltv, 0)

