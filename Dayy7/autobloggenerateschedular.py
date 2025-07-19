# How generate blog using python with scheduler and store in mongodb
# Module 1 - Create blog using python
# Module 2 -Add blog in mongodb

from pymongo import MongoClient
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import time

client = MongoClient("mongodb://localhost:27017/")
db = client["blog"]
collection = db["blogs"]


# create a function to publish the post based on schedule status
def publish_post(post):
    collection.update_one(
        {"_id": post["_id"]}, {"$set": {"status": "posted", "posted_at": datetime.now}}
    )
    # Check for due posts


def check_scheduled_posts():
    now = datetime.now()
    due_posts = collection.find(
        {"scheduled_time": {"$lte": now}, "status": "scheduled"}
    )


blog__ = {
    "title": "It is my first Blog",
    "created": datetime.now(),
    "scheduled_time": datetime(2025, 7, 15, 14, 0),  # Adjust to your desired time
    "status": "scheduled",
}


collection.insert_one(blog__)
collection.create_index("title", unique=True)

# Start scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(
    check_scheduled_posts, "interval", seconds=30
)  # check every 30 seconds
scheduler.start()
# Keep the script running
try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    print("Scheduler stopped.")
