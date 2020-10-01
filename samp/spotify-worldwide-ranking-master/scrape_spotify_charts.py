
import pandas as pd
import os

from spotifycharts import Collector

# Initialize Collector Class with region, start date and end date
start_date = '2020-07-10'
end_date = '2020-07-15'
collector = Collector('ph',start_date, end_date)
# Start downloads
collector.start()
