import heapq


def topXSimpleLTVCustomers(x, database):
  minh = []
  for customer_id, customer in database.customers.items():
    # Update customer.average_ltv
    customer.updateAverageLTV(database.latest_time)
    heapq.heappush(minh, (-customer.average_ltv, customer))
  return [c for ltv, c in minh[:x]]
