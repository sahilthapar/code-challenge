# Disclaimers

- All events are expected to have two properties at least
    - key
    - event_time
    
- Although out of sync events are handled it is still expected that event_time
are in the correct 'logical' order
    - An ORDER event's timestamp will be after a NEW CUSTOMER event's timestamp

- Only completed weeks are considered for LTV calculation
    - 10 days is still 1 week
    - Customers who have been using the website for less than 1 week are
    considered to have insufficient data and have been assigned an LTV value of 0.

- Duplicate event handling based on event verbs
    - Duplicate customers are handled as are customer updates
    - Duplicate orders are handled as are order updates
    - Each site visit is considered to be a new visit
    - Each image upload is considered to be a new upload

- History of events is not maintained
    - Only latest customer info, order info is available
    - This can be easily changed by changing the implementation of datastore to append events


# To run tests

```
cd src
python -m unittest test
```

# How to use

- Change path in src/main.py to desired input file

```
python src/main.py
```
