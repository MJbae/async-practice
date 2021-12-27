from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'owners', CustomerViewSet, basename='owners')
router.register(r'', CarViewSet, basename='cars')

urlpatterns = router.urls
