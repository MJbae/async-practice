from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'dogs', DogViewSet, basename='dogs')
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'owners', CustomerViewSet, basename='owners')

urlpatterns = router.urls
