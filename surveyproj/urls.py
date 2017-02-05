from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # questionnaire urls
    url(r'q/', include('questionnaire.urls')),

    url(r'^take/(?P<questionnaire_id>[0-9]+)/$', 'questionnaire.views.generate_run'),
    # url(r'^$', 'questionnaire.page.views.page', {'page_to_render' : 'index'}),
    url(r'^complete$', 'questionnaire.page.views.page', {'page_to_render' : 'complete'}),
    url(r'^$', RedirectView.as_view(url='/take/1')),
    url(r'^(?P<lang>..)/(?P<page_to_trans>.*)\.html$', 'questionnaire.page.views.langpage'),
    url(r'^(?P<page_to_render>.*)\.html$', 'questionnaire.page.views.page'),
    url(r'^setlang/$', 'questionnaire.views.set_language'),
)