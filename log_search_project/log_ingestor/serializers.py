from .models import Log
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import LogDocument


class LogDocumentSerializer(DocumentSerializer):
    class Meta(object):
        """Meta options."""

        model = Log
        document = LogDocument
        fields = (
            "level",
            "message",
            "resourceId",
            "timestamp",
            "traceId",
            "spanId",
            "commit",
            "parentResourceId",
        )
