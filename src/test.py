import unittest
import sys
from ingest import *
from topXSimpleLTVCustomers import *
from datastore import *
sys.path.insert(0, '../input')
from input import *


class Test(unittest.TestCase):

  def setUp(self):
    self.D = Datastore()

  def test_new_customer_event(self):
    e = single_event
    ingest(e, self.D)
    self.assertIn("96f55c7d8f42", self.D.customers)

  def test_multiple_events(self):
    events = multiple_events
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertIn("ac05e815502f", self.D.site_visits)
    self.assertIn("d8ede43b1d9f", self.D.images)
    self.assertIn("68d84e5d1a43", self.D.orders)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 12.34)

  def test_update_customer(self):
    events = update_customer
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.customers), 1)
    self.assertIn("ac05e815502f", self.D.site_visits)
    self.assertIn("d8ede43b1d9f", self.D.images)
    self.assertIn("68d84e5d1a43", self.D.orders)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 12.34)

    self.assertEqual(self.D.customers["96f55c7d8f42"].adr_state, "OH")

  def test_update_only_latest_customer(self):
    events = update_latest_customer
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.customers), 1)
    self.assertIn("ac05e815502f", self.D.site_visits)
    self.assertIn("d8ede43b1d9f", self.D.images)
    self.assertIn("68d84e5d1a43", self.D.orders)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 12.34)

    self.assertEqual(self.D.customers["96f55c7d8f42"].adr_state, "AK")


  def test_other_event_before_customer(self):
    events = other_event_before_customer
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.customers), 1)
    self.assertIn("ac05e815502f", self.D.site_visits)
    self.assertIn("d8ede43b1d9f", self.D.images)
    self.assertIn("68d84e5d1a43", self.D.orders)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 12.34)

  def test_order_update(self):
    events = order_update
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.customers), 1)
    self.assertIn("ac05e815502f", self.D.site_visits)
    self.assertIn("d8ede43b1d9f", self.D.images)
    self.assertIn("68d84e5d1a43", self.D.orders)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 14.34)

  def test_multiple_customers_orders_site_visits(self):
    events = multiple_customers_order_site_visits
    for e in events:
      ingest(e, self.D)

    # Check all events were added
    self.assertIn("96f55c7d8f42", self.D.customers)
    self.assertIn("97f55c7d8f42", self.D.customers)
    self.assertEqual(len(self.D.customers), 2)
    self.assertIn("ac05e815502f", self.D.site_visits)
    self.assertIn("bc05e815502f", self.D.site_visits)
    self.assertIn("d8ede43b1d9f", self.D.images)
    self.assertIn("e8ede43b1d9f", self.D.images)
    self.assertIn("68d84e5d1a43", self.D.orders)
    self.assertIn("18d84e5d1a43", self.D.orders)

    # Check Customer site visits were increased
    self.assertEqual(self.D.customers["96f55c7d8f42"].site_visits, 2)
    self.assertEqual(self.D.customers["97f55c7d8f42"].site_visits, 1)

    # Check if Order Amount is added
    self.assertEqual(self.D.customers["96f55c7d8f42"].total_amount, 14.34)
    self.assertEqual(self.D.customers["97f55c7d8f42"].total_amount, 12.34)

    top_two = topXSimpleLTVCustomers(2, self.D)
    self.assertEqual(top_two[0], (-52 * (14.34 / 2) * 2 * 10, '96f55c7d8f42', ))
    self.assertEqual(top_two[1], (-52 * 12.34 * 1 * 10, '97f55c7d8f42'))


