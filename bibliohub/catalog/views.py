from django.shortcuts import render

# Create your views here.

from catalog.models import Book, Author, Genre

from django.views import generic
from django.views.generic import TemplateView, ListView
from .models import Book

from django.db.models import Q


# class BookListView(generic.ListView):
#     """Generic class-based view for a list of books."""
#     model = Book
#     paginate_by = 10


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()

    titles = [str(elem)[2:-3] for elem in list(Book.objects.all().values_list('title'))]

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'titles': titles,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# book = Book()
# author = Author()
# author.first_name = 'Joseph'
# author.last_name = 'Pieper'
# book.author = author
# author.save()
# book.title = 'Leisure the Basis of Culture'
# book.save()


# search test views
class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            # Q(title__icontains=query) | Q(author__icontains=query)
            Q(title__icontains=query)
        )
        return object_list




