import pytest
from unittest.mock import Mock, patch
from blog import Blog

api_response = [
    {'userId': 1, 'id': 1, 'title': 'Titulo teste 1', 'body': 'Conteudo do blog 1'},
    {'userId': 2, 'id': 2, 'title': 'Titulo teste 2', 'body': 'Teste de conteudo do blog 2'}
]

@pytest.fixture
def mock_requests_get():
    with patch('blog.requests.get') as mock_get:
        yield mock_get

@pytest.fixture
def blog_instance(mock_requests_get):
    mock_requests_get.return_value.json.return_value = api_response
    return Blog()

def test_posts(blog_instance):
    result = blog_instance.posts()
    assert result == api_response

def test_post_by_user_id(blog_instance, mock_requests_get):
    mock_requests_get.return_value.json.return_value = api_response[0]
    result = blog_instance.post_by_user_id(1)
    assert result == api_response[0]
