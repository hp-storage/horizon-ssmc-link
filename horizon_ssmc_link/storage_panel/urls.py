# (c) Copyright [2015] Hewlett-Packard Development Company, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from django.conf.urls import patterns
from django.conf.urls import url

# from openstack_dashboard.dashboards.admin.volumes.volumes \
#     import views
from horizon_ssmc_link.storage_panel import views

VIEWS_MOD = ('horizon_ssmc_link.storage_panel.views')
# VIEWS_MOD = ('dashboards.admin.volumes.volumes.views')

urlpatterns = patterns(
    VIEWS_MOD,
    # url(r'^(?P<volume_id>[^/]+)/update_status$',
    #     views.UpdateStatusView.as_view(),
    #     name='update_status'),
    url(r'^$',
        views.IndexView.as_view(),
        name='index'),
    url(r'^(?P<volume_id>[^/]+)/link_to_volume/$',
        views.LinkVolumeView.as_view(),
        name='link_to_volume'),
    url(r'^(?P<volume_id>[^/]+)/link_to_cpg/$',
        views.LinkVolumeCPGView.as_view(),
        name='link_to_cpg'),
    url(r'^(?P<volume_id>[^/]+)/link_to_domain/$',
        views.LinkVolumeDomainView.as_view(),
        name='link_to_domain'),
    url(r'^create_endpoint/$',
        views.CreateEndpointView.as_view(),
        name='create_endpoint'),
    url(r'^(?P<service_id>[^/]+)/edit_endpoint/$',
        views.EditEndpointView.as_view(),
        name='edit_endpoint'),
)
