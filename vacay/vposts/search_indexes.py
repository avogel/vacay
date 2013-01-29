from haystack import indexes
from vacay.vposts.models import *

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(model_attr='title')
    text = indexes.CharField(document=True, model_attr='contents')
    date_written = indexes.DateField(model_attr='date_written')

    def get_model(self):
        return Post

class TripIndex(indexes.SearchIndex, indexes.Indexable):
    name = indexes.CharField(model_attr='name')
    text = indexes.CharField(document=True, model_attr='description')

    def get_model(self):
        return Trip

# class VisitedCityIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True)

#     def get_model(self):
#         return VisitedCity

# class VisitedDayIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.DateField(document=True)

#     def get_model(self):
#     	return VisitedDay