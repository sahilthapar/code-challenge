import unittest
from ingest import *
from topXSimpleLTVCustomers import *
from datastore import *


class Test(unittest.TestCase):

  def setUp(self):
    self.D = Datastore()

  def test_new_customer_event(self):
    e = {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z",
         "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"}
    ingest(e, self.D)
    self.assertIn("96f55c7d8f42", self.D.customers)

  def test_multiple_events(self):
    events = [{"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z",
                "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
               {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
                "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
               {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
                "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
               {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
                "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"}]
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
    events = [{"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
              {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
               "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
              {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
               "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
              {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
               "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
              {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"}]
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
    events = [{"type": "CUSTOMER", "verb": "UPDATE", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
              {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
               "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
              {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
               "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
              {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
               "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
              {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:45.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"}]
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

  def test_update_only_latest_customer(self):
    events = [{"type": "CUSTOMER", "verb": "UPDATE", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
              {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
               "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
              {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
               "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
              {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
               "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
              {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:45.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"}]
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

    self.assertEqual(self.D.customers["96f55c7d8f42"].adr_state, "AK")


  def test_other_event_before_customer(self):
    events = [{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
               "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
              {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
               "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
              {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
               "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
              {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:45.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"}]
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
    events = [{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
               "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
              {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
               "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
              {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
               "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
              {"type": "ORDER", "verb": "UPDATE", "key": "68d84e5d1a43", "event_time": "2017-02-06T12:55:55.555Z",
               "customer_id": "96f55c7d8f42", "total_amount": "14.34 USD"},
              {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:45.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"}]
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
    events = [{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
               "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
              {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
               "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
              {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
               "customer_id": "97f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
              {"type": "ORDER", "verb": "UPDATE", "key": "18d84e5d1a43", "event_time": "2017-02-06T12:55:55.555Z",
               "customer_id": "96f55c7d8f42", "total_amount": "14.34 USD"},
              {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
               "customer_id": "97f55c7d8f42", "total_amount": "14.34 USD"},
              {"type": "CUSTOMER", "verb": "UPDATE", "key": "96f55c7d8f42", "event_time": "2017-02-06T12:46:45.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"},
              {"type": "CUSTOMER", "verb": "NEW", "key": "97f55c7d8f42", "event_time": "2017-01-06T12:46:45.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
              {"type": "SITE_VISIT", "verb": "NEW", "key": "bc05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
               "customer_id": "97f55c7d8f42", "tags": [{"some key": "some value"}]},
              {"type": "IMAGE", "verb": "UPLOAD", "key": "e8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
               "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
              {"type": "ORDER", "verb": "UPDATE", "key": "68d84e5d1a43", "event_time": "2017-02-06T12:55:55.555Z",
               "customer_id": "97f55c7d8f42", "total_amount": "12.34 USD"},
              {"type": "ORDER", "verb": "NEW", "key": "18d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
               "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
              {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:45.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
              {"type": "CUSTOMER", "verb": "UPDATE", "key": "97f55c7d8f42", "event_time": "2017-02-06T12:46:45.384Z",
               "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"}
              ]
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

    


