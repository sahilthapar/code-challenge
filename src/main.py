from ingest_topX import *
from datastore import *
from utils import inputReader

# Create datastore

datastore = Datastore()

# Ingest data
data = inputReader('./sample_input/events.txt')
for event in data:
  ingest(event, datastore)

# Top customers

X = 1
topX = topXSimpleLTVCustomers(X, datastore)

prettyPrint(topX)


