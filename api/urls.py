
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, EmpleadoViewSet, CoordinadorViewSet, ServicioViewSet, ReservaDeServicioViewSet

router = DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'empleado', EmpleadoViewSet)
router.register(r'coordinador', CoordinadorViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'reservadeservicio', ReservaDeServicioViewSet)

urlpatterns = router.urls

