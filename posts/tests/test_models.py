import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestPost:
    def test_init(self):
        obj = mixer.blend('posts.post')
        assert obj.pk == 1, 'Should save a post instance'
        
    def test_title(self):
        obj = mixer.blend('posts.post', title='Entry One')
        assert obj.title == 'Entry One'