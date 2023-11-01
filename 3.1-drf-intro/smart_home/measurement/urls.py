from django.urls import path

from measurement.views import DiscrView, OneDiscrView, MeasurementView

urlpatterns = [
    path('sensors/', DiscrView.as_view()),
    path('sensors/<pk>/', OneDiscrView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]

# TODO: зарегистрируйте необходимые маршруты
