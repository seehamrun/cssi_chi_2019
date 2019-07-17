from google.appengine.ext import ndb

# class Dog:
#     def __init__(self, name, age, color, bark_intensity, review):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.bark_intensity = bark_intensity
#         self.review = review

class DatabaseDog(ndb.Model):
    name = ndb.StringProperty()
    age = ndb.IntegerProperty()
    color = ndb.StringProperty()
    bark_intensity = ndb.IntegerProperty()
    review = ndb.StringProperty()
