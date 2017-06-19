import unittest
from ingest import *

D = {}
class Test(unittest.TestCase):
  def test_image_event(self):
    e = {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"}
    self.assertEqual(ingest(e, D), D)
