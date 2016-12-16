import pytest 
from django.contrib.auth.models import AnonymousUser
from django.test.client import RequestFactory
from mixer.backend.django import mixer
from posts.views import post_list, post_detail
pytestmark = pytest.mark.django_db



class TestPostListView:
    
    def test_list_of_posts(self):
        objs = mixer.cycle(3).blend('posts.Post',  title=( t for t in ('Entry One', 'Entry Two', 'Entry Three')))
        req = RequestFactory().get('/', objs=objs)
        req.user = AnonymousUser()
        resp = post_list(req)
        assert 'Entry Three' in str(resp.content), 'Should return a list of posts'
        assert 'Entry Two' in str(resp.content),''
        assert 'Entry One' in str(resp.content),''
        
class TestPostDetailView:
    def test_template(self):
        obj = mixer.blend('posts.post')
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = post_detail(req, slug=obj.slug)
        assert resp.status_code == 200, 'Should render the index.html template'

    def test_detail_pages(self):
        obj = mixer.blend('posts.post', title='Entry One', slug='entry-one')
        req = RequestFactory().get(obj.get_absolute_url())
        req.user = AnonymousUser()
        resp = post_detail(req, slug=obj.slug)
        assert 'Entry One' in str(resp.content), 'Should get the slug of a post'
        
        

        
        