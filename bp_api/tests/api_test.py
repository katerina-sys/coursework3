import pytest

import main


class TestApi:
    post_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    @pytest.fixture
    def app_instance(self):
        return main.app.test_client()

    # Статус-код всех постов (тест)
    def test_all_posts_correct_status(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        assert result.status_code == 200

    #Проверка есть ли ключи у всех постов
    def test_all_posts_has_correct_keys(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        list_of_posts = result.get_json()

        for post in list_of_posts:
            assert post.keys() == self.post_keys, "Неверные ключи у полученного словаря"


    # Статус-код одного поста (тест)
    def test_single_post_correct_status(self, app_instance):
        result = app_instance.get("/api/posts/1/", follow_redirects=True)
        assert result.status_code == 200

    # Статус-код несуществующего поста (тест)
    def test_post_is_none_correct_status_404(self, app_instance):
        result = app_instance.get("/api/posts/0/", follow_redirects=True)
        assert result.status_code == 404

    # Есть ли у элемента нужные ключи
    def test_single_post_has_correct_keys(self, app_instance):
        result = app_instance.get("/api/posts/1/", follow_redirects=True)
        post = result.get_json()
        post_keys = set(post.keys())
        assert post_keys == self.post_keys
