from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from . import models, serializers

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


def csrf(req):
    return JsonResponse({"csrf": get_token(req)})


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
    

class OffersViewSet(ListModelMixin, GenericViewSet):
    queryset = models.Offers.objects.filter(is_listed=True).all()
    serializer_class = serializers.OffersSerializer
