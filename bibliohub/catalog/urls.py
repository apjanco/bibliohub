from django.urls import path
from . import views
from .views import SearchResultsView, HomePageView
urlpatterns = [
    path('', views.index, name='index'),
    # path('books/', views.BookListView.as_view(), name='books'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('home/', HomePageView.as_view(),name='home'),
    # path('author_search/', AuthorSearchResultsView.as_view(), name='author_search_results'),
]