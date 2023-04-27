from instabot import Bot      #The Bot is a class 

my_bot = Bot()
#login
my_bot.login(username="city_ken.di", password="myres2000")

#follow a user or a friend
my_bot.follow("mpashogram")

#following multiple users or account : you have to pass a list of the users account name
my_bot.follow_users(["nairobi_gossip_club", "flaqo411"])

#unfollow the non followers :this unfollows those who do not follow us back
my_bot.unfollow_non_followers()

#uploadin a photo to post in your account
my_bot.upload_photo("ad6.jpeg" caption="Advert for juice")

#sending message to users
my_bot.send_message("Hello Judy", "shirowainaina")

#liking posts for a particular user
my_bot.like_user("citykendi48", amount=2)

#commenting :requires media id
user_id = my_bot.get__user_id_from_username("citykendi48")
media_id = my_bot.get_last_user_medias(user_id)
my_bot.comment(media_id, "Nice")

            








''

















