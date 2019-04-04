# schemas.py
from app import ma
from app.models import Tweet

class ProductSchema(ma.Schema):
    class Meta:
        model = Tweet
        fields = ('id', 'text') # These are the fields we want in the JSON!

tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)
