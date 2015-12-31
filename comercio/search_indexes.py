import datetime
from haystack import indexes
from comercio.models import Comercio


class ComercioIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    fecha = indexes.DateTimeField(model_attr='fecha')

    def get_model(self):
        return Comercio

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(fecha__lte=datetime.datetime.now())
