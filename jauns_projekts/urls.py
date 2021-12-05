"""jauns_projekts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import uzdevumi.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show-hello', uzdevumi.views.show_hello),
    path('show-html', uzdevumi.views.show_html),
    path('show-datetime', uzdevumi.views.show_datetime),
    path('show-name', uzdevumi.views.show_name),
    path('university', uzdevumi.views.university),
    path('motivate', uzdevumi.views.motivate),
    path('visit-new', uzdevumi.views.visit_new),
    path('add-visit', uzdevumi.views.add_visit),
    path('add-visit/csv', uzdevumi.views.upload_csv_row_to_db),
    path('visit/<int:visit_id>', uzdevumi.views.get_visit, name='get-visit'),
    path('filter-visits/visitor', uzdevumi.views.filter_visits_by_visits),
    path('', uzdevumi.views.get_all_visits),
]
