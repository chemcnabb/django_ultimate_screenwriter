from django.conf.urls import patterns, include, url
from django.conf import settings
from common.views import HomeView, ProfileView
from screenwriter.views import ScreenwriterView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^screenplay/$', ScreenwriterView.as_view()),
    url(r'^screenplay/(?P<screenplay_slug>[-\w]+)/$', ScreenwriterView.as_view()),

    # url(r'^blog/', include('blog.urls')),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/profile/$', ProfileView.as_view()),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns("",
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
)