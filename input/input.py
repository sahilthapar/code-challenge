multiple_events = [{"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z",
                    "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
                   {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f",
                    "event_time": "2017-01-06T12:45:52.041Z",
                    "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
                   {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
                    "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
                   {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
                    "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"}]

single_event = {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z",
                "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"}

update_customer = [{"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z",
                    "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
                   {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f",
                    "event_time": "2017-01-06T12:45:52.041Z",
                    "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
                   {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
                    "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
                   {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
                    "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
                   {"type": "CUSTOMER", "verb": "UPDATE", "key": "96f55c7d8f42", "event_time": "2017-01-07T12:46:46.384Z",
                    "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"}]

update_latest_customer = [
  {"type": "CUSTOMER", "verb": "UPDATE", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z",
   "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
  {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
   "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
  {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
   "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
  {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
   "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
  {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:45.384Z",
   "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"}]

other_event_before_customer = [
  {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
   "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
  {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
   "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
  {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
   "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
  {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:45.384Z",
   "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"}]

order_update = [{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
                 "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
                {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
                 "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
                {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
                 "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
                {"type": "ORDER", "verb": "UPDATE", "key": "68d84e5d1a43", "event_time": "2017-02-06T12:55:55.555Z",
                 "customer_id": "96f55c7d8f42", "total_amount": "14.34 USD"},
                {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:45.384Z",
                 "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"}]

multiple_customers_order_site_visits = [
  {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
   "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
  {"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
   "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]},
  {"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
   "customer_id": "97f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
  {"type": "ORDER", "verb": "UPDATE", "key": "18d84e5d1a43", "event_time": "2017-01-07T12:55:55.555Z",
   "customer_id": "96f55c7d8f42", "total_amount": "14.34 USD"},
  {"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
   "customer_id": "97f55c7d8f42", "total_amount": "14.34 USD"},
  {"type": "CUSTOMER", "verb": "UPDATE", "key": "96f55c7d8f42", "event_time": "2017-01-07T12:46:45.384Z",
   "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"},
  {"type": "CUSTOMER", "verb": "NEW", "key": "97f55c7d8f42", "event_time": "2017-01-06T12:46:45.384Z",
   "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
  {"type": "SITE_VISIT", "verb": "NEW", "key": "bc05e815502f", "event_time": "2017-01-06T12:45:52.041Z",
   "customer_id": "97f55c7d8f42", "tags": [{"some key": "some value"}]},
  {"type": "IMAGE", "verb": "UPLOAD", "key": "e8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z",
   "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"},
  {"type": "ORDER", "verb": "UPDATE", "key": "68d84e5d1a43", "event_time": "2017-01-07T12:55:55.555Z",
   "customer_id": "97f55c7d8f42", "total_amount": "12.34 USD"},
  {"type": "ORDER", "verb": "NEW", "key": "18d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z",
   "customer_id": "96f55c7d8f42", "total_amount": "12.34 USD"},
  {"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:45.384Z",
   "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"},
  {"type": "CUSTOMER", "verb": "UPDATE", "key": "97f55c7d8f42", "event_time": "2017-01-14T12:45:45.384Z",
   "last_name": "Smith", "adr_city": "Middletown", "adr_state": "OH"}
  ]