from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry
from .models import Log

PUBLISHER_INDEX = Index("cars")

PUBLISHER_INDEX.settings(number_of_shards=1, number_of_replicas=0)


@PUBLISHER_INDEX.doc_type
class LogDocument(Document):
    id = fields.IntegerField(attr="id")
    level = fields.KeywordField()
    message = fields.TextField()
    resourceId = fields.KeywordField()
    timestamp = fields.DateField()
    traceId = fields.KeywordField()
    spanId = fields.KeywordField()
    commit = fields.KeywordField()
    parentResourceId = fields.KeywordField()

    class Index:
        name = "logs"

    class Django:
        model = Log  # The model associated with this Document
