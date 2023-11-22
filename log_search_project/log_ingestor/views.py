import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from elasticsearch.helpers import bulk
from .documents import LogDocument
from .models import Log
from .serializers import LogDocumentSerializer
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)


@csrf_exempt
@require_POST
def ingest_log(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        log = Log(**data)
        log.save()
        # Index the log in Elasticsearch
        LogDocument().update(log)

        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})


@require_POST
def bulk_indexing(request):
    logs = Log.objects.all()
    data = [
        {
            "_op_type": "index",
            "_index": "logs",
            "_type": "_doc",
            "_id": log.id,
            "_source": {
                "level": log.level,
                "message": log.message,
                "resourceId": log.resourceId,
                "timestamp": log.timestamp,
                "traceId": log.traceId,
                "spanId": log.spanId,
                "commit": log.commit,
                "parentResourceId": log.parentResourceId,
            },
        }
        for log in logs
    ]
    bulk(client=LogDocument._doc_type.index, actions=data)
    return JsonResponse({"status": "success"})


class PublisherDocumentView(DocumentViewSet):
    document = LogDocument
    serializer_class = LogDocumentSerializer
    fielddata = True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]

    search_fields = (
        "level",
        "message",
        "resourceId",
        "timestamp",
        "traceId",
        "spanId",
        "commit",
        "parentResourceId",
    )
    multi_match_search_fields = (
        "level",
        "message",
        "resourceId",
        "timestamp",
        "traceId",
        "spanId",
        "commit",
        "parentResourceId",
    )
    filter_fields = {
        "level": "level",
        "message": "message",
        "resourceId": "resourceId",
        "timestamp": "timestamp",
        "traceId": "traceId",
        "spanId": "spanId",
        "commit": "commit",
        "parentResourceId": "parentResourceId",
    }
    ordering_fields = {
        "id": None,
    }
    ordering = ("id",)
