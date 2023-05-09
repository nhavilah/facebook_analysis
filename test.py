from facebook_scraper import get_posts
import csv
import datetime
previous_30_days = datetime.datetime.today() - datetime.timedelta(days=30)

from datetime import datetime
with open('events.csv', "w", newline="") as file:
    # writer = csv.writer(file)
    for post in get_posts('thetivolibrisbane', pages=3, credentials={"nickhavilah@gmail.com", "Valkyrie001!"}, options={"comments": True}):
        datetime = datetime.strptime(str(post["time"]), '%Y-%m-%d %H:%M:%S')
        post_object = dict()
        post_object["date"] = str(datetime)[0:10]
        post_object["time"] = str(datetime)[11:]
        post_object["likes"] = post["likes"]
        post_object["shares"] = post["shares"]
        post_object["comments"] = post["comments"]

        comments_object = []
        for comment in post["comments_full"]:
            comments_object.append(comment["comment_text"])
        # writer.writerow([
        #     str(datetime)[0:10],
        #     str(datetime)[11:],
        #     post["likes"],
        #     post["post_url"],
        #     post['shares'],
        #     post["comments"],
        #     post["text"],
        #     post["comments_full"]
        # ])
        # for comment in post["comments_full"]:
        #     print("comment")
        #     print(comment["comment_text"])
    