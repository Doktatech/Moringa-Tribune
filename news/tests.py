from django.test import TestCase
from .models import Editor,Article,tags

class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.rewel = Editor(first_name ='Rewel',last_name ='Kinyanjui', email ='doktatech2@gmail.com')
    def test_instance (self):
        self.assertTrue(isinstance(self.rewel,Editor))   
    def test_save_method(self):
        self.rewel.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)
class ArticleTestClass(TestCase):
    def setUp(self):
        self.rewel = Editor(first_name ='Rewel',last_name ='Kinyanjui', email ='doktatech2@gmail.com')
        self.rewel.save_editor()
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.rewel)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)