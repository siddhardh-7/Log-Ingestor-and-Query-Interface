from django.urls import path
from log_ingestor.views import *

urlpatterns = [
    path("ingest/", ingest_log, name="ingest_log"),
    path("search/", PublisherDocumentView.as_view({"get": "list"})),
]
