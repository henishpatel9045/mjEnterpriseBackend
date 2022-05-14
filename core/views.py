from . import models, serializers
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

# Create your views here.

# @api_view(["GET"])
# def site_info(req):
#     if req.method == "GET":
#         try:
#             data = models.SiteInfo.objects.first()
#             res = serializers.SiteInfoSerializer(data)
#             return Response(res.data)
#         except models.SiteInfo.DoesNotExist:
#             return Response({'detail': "No record in the database"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception:
#             return Response("Unknown exception occur.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#     else:
#         return Response("Only get method allowed on this endpoint.", status=status.HTTP_405_METHOD_NOT_ALLOWED)


class SiteInfoViewSet(ListModelMixin, GenericViewSet):
    queryset = models.SiteInfo.objects.all()
    serializer_class = serializers.SiteInfoSerializer

        
# @api_view(["GET"])
# def about_images(req):
#     if req.method == "GET":
#         try:
#             data = models.AboutImage.objects.all()
#             res = serializers.AboutImageSerializer(data, many=True)
#             return Response(res.data)
#         except models.AboutImage.DoesNotExist:
#             return Response({'detail': "No record in the database"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception:
#             return Response("Unknown exception occur.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
#     else:
#         return Response("Only get method allowed on this endpoint.", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        

class AboutImageViewSet(ListModelMixin, GenericViewSet):
    queryset = models.AboutImage.objects.all()
    serializer_class = serializers.AboutImageSerializer
    