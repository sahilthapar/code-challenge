import heapq


def topXSimpleLTVCustomers(x, database):
  """
  Returns the top x customers based on simples ltv based on a heap 
  https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
  :param x: number of top customers desired
  :param database: 
  :return: top x customers based on simple ltv
  """
  minh = []
  for customer_id, customer in database.customers.items():
    customer.updateAverageLTV(database.latest_time)
    heapq.heappush(minh, (-customer.average_ltv, customer))
  return [c for ltv, c in minh[:x]]
