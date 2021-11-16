from task_4_function import currency_rates
import sys
request = sys.argv[1:]

for x in request:
    currency_rates(x)