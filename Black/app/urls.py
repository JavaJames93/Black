from rest_framework import routers

from django.urls import path
from app.views import DataFileView, DataFileDetails

# router = routers.DefaultRouter()
# router.register('api/data', DataFileViewset, 'data')
# # url(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())

# urlpatterns = router.urls

urlpatterns = [
    path('', DataFileView.as_view()),
    path('/<int:pk>', DataFileDetails.as_view())
]
