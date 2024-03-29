from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import logging

from lib.db import pool, query_wrap_object

tracer = trace.get_tracer("home.activities")


class HomeActivities:
  def run(cognito_user_id=None):
    print("====home-activities")
    # logger.info("HomeActivities")
    # with tracer.start_as_current_span("home-activities-mock-data"):
    #   span = trace.get_current_span()
    #   now = datetime.now(timezone.utc).astimezone()
    #   span.set_attribute("app.now", now.isoformat())
    #   span.set_attribute("app.result_length", len(results))


    sql = query_wrap_object("""
    SELECT * FROM activities
    """)
    print("SQL!------------")
    print(sql)
    print("SQL------------")

    with pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql)
          # this will return a tuple
          # the first field being the data
      json = cur.fetchone()
      print("-1----")
      print(json[0])
      return json[0]
      return results