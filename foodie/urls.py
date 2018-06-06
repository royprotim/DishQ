from django.conf.urls import url
import requests
from . import views
from models import Restaurant,Review

urlpatterns = [
    url(r'^$', views.index, name='index'),
]


#following script is executed once when the server starts for the very first time
r = requests.get('https://developers.zomato.com/api/v2.1/search?entity_id=4&entity_type=city&start=0&count=20&sort=rating',headers={"user-key":"2305553b33aef82dbbac6fbda05f5bc4"})

Restaurant.objects.all().delete()
for res in r.json()["restaurants"]:
	rest = Restaurant.objects.create(rest_ID=res["restaurant"]["R"]["res_id"],name=res["restaurant"]["name"],lat=res["restaurant"]["location"]["latitude"],lon=res["restaurant"]["location"]["longitude"],url=res["restaurant"]["url"],img_url=res["restaurant"]["featured_image"],rating=res["restaurant"]["user_rating"]["aggregate_rating"])
	rest.save()
	reviews = requests.get('https://developers.zomato.com/api/v2.1/reviews',params={'res_id':res["restaurant"]["R"]["res_id"],'start':0,'count':5},headers={"user-key":"2305553b33aef82dbbac6fbda05f5bc4"})
	restaurant = Restaurant.objects.get(rest_ID=res["restaurant"]["R"]["res_id"])
	for review in reviews.json()["user_reviews"]:
		rev = Review.objects.create(rest=restaurant,user=review["review"]["user"]["name"],rating=review["review"]["rating"],rev_text=review["review"]["review_text"])
		rev.save()
	print "Getting reviews for ",res["restaurant"]["name"]