from django.conf.urls.defaults import patterns, url
from campaign import views as CampaignView

urlpatterns = patterns('campaign.views',
    url(r'^edit/(?P<pk>\w+)/$', CampaignView.editCampaign, ),
    url(r'^view/(?P<pk>\w+)/$', CampaignView.getCampaignMeps, ),
)
