#Wed Mar 21 05:07:38 UTC 2018
#2025-11-03
import datetime as dt
x = dt.datetime.now()
yyyy = x.year
mm = x.month
dd = x.day
print(f"{'%04d'%yyyy}-{'%02d'%mm}-{'%02d'%dd}")