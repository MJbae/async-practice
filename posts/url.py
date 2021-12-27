from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'transactions', TransactionViewSet, basename='transactions')
router.register(r'currencies', CurrencyViewSet, basename='currencies')
router.register('customers', CustomerViewSet, basename='customer')

urlpatterns = router.urls
