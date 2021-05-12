from instapy import InstaPy

session = InstaPy(username="csmajorbot", password="CsMajorsRule321*")
session.login()
session.like_by_tags(["java", "python", "coding", "javascript"], amount=50)
session.set_dont_like(["naked", "nsfw", "nude"])    #don't want it to like any nsfw content
session.set_do_comment(True, percentage=10)
session.set_do_follow(True, percentage=15)
session.set_comments(["Nice!", "I love coding too :joy: !", "Java :heart_eyes:", "Python :heart_eyes:", "javascript :heart_eyes:"])
session.set_quota_supervisor(enabled=True, peak_comments_daily=200, peak_comments_hourly=20, peak_likes_daily=200,
                                 peak_likes_hourly=20, sleep_after=['likes', 'follows'])
session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=1000000,
                                    min_followers=100,
                                    min_following=50)
session.like_by_feed(amount=20, randomize=5)
session.like_by_users(["donkurayami"], amount=5)
#session.follow_user_followers(["khalil.mcfarlane"], amount=5)

session.end()