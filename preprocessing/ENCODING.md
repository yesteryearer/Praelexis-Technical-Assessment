### `negative_reason_confidence` ###
- A value of `0` indicates a missing entry. This is prevalent when the sentiment is not negative.

### `negative_reason` ###
- A missing value is indicated by a `Not Applicable` value. This is prevalent where the sentiment is not negative.
- Categorical Encoding:
    {0: 'Not Applicable',
    1: 'Bad Flight',
    2: "Can't Tell",
    3: 'Late Flight',
    4: 'Customer Service Issue',
    5: 'Flight Booking Problems',
    6: 'Lost Luggage',
    7: 'Flight Attendant Complaints',
    8: 'Cancelled Flight',
    9: 'Damaged Luggage',
    10: 'longlines'}

### `tweet_location` ###
- Due to nearly a third of the values being missing, the `Unknown` category was introduced to indicate a missing value.

### `user_timezone` ###
- Due to nearly a third of the values being missing, the `Unknown` category was introduced to indicate a missing value.

### `airline_sentiment` ###
- Categorical encoding:
    {0: 'neutral', 
    1: 'positive', 
    2: 'negative'}

### `airline` ###
- Categorical encoding:
    {0: 'Virgin America',
    1: 'United',
    2: 'Southwest',
    3: 'Delta',
    4: 'US Airways',
    5: 'American'}
