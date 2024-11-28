from django.urls import path, include
from .views import *
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', MovieListViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_list'),
    path('<int:pk>/', MovieDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                  'delete': 'destroy', }), name='movie_detail'),

    path('profile', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='profile_list'),
    path('profile/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                          'delete': 'destroy', }), name='profile_detail'),

    path('country/', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country_list'),
    path('country/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy', }), name='country_detail'),

    path('directory/', DirectoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='directory_list'),
    path('directory/<int:pk>/', DirectoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy', }), name='directory_detail'),

    path('actor/', ActorViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor_list'),
    path('actor/<int:pk>/', ActorViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy', }), name='actor_detail'),

    path('janre/', JanreViewSet.as_view({'get': 'list', 'post': 'create'}), name='janre_list'),
    path('janre/<int:pk>/', JanreViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy', }), name='janre_detail'),


    path('movielanguage/', MovieLanguageViewSet.as_view({'get': 'list', 'post': 'create'}), name='movielanguage_list'),
    path('movielanguage/<int:pk>/', MovieLanguageViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy', }), name='movielanguage_detail'),

    path('moments/', MomentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='moments_list'),
    path('moments/<int:pk>/', MomentsViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy', }), name='moments_detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy', }), name='rating_detail'),

    path('favoritemovie/', FavoriteMovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='favoritemovie_list'),
    path('favoritemovie/<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy', }), name='favoritemovie_detail'),

    path('favorite/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite_list'),
    path('favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                                  'delete': 'destroy', }), name='favorite_detail'),


    path('history/', HistoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='history_list'),
    path('history/<int:pk>/', HistoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy', }), name='history_detail')


]