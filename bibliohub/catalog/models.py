from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200,)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Class defining a book model"""
    title = models.CharField(max_length=200, help_text='Enter the title of the book')

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    isbn = models.CharField('ISBN', max_length=13)

    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    language = models.CharField(max_length=200, null=True)

    # author_full_name = models.CharField(max_length=200, help_text='Enter the author\'s name')

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'{self.title}, {self.author}'

