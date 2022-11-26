from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import CommentForm, CreateForm
from django.urls import reverse_lazy


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

    # for category dropdown list
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


# class AddPost(generic.CreateView):
#     model = Post
#     template_name = 'create_post.html'
#     fields = '__all__'


# new to replace AddPost
def CreatePost(request):
    model = Post
    create_form = CreateForm(request.POST or None, request.FILES or None)
    context = {
        'create_form': create_form,
    }
    form_class = CreateForm

    if request.method == "POST":
        create_form = CreateForm(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.instance.author = request.user
            create_form.instance.status = 1
            blog_post = create_form.save(commit=False)

            blog_post.save()
            return redirect('home')
    else:
        create_form = CreateForm()
    return render(request, "create_post.html", context)


# View for individual category pages
def CategoryIndividual(request, categories):
    category = Post.objects.filter(category=categories.replace('-', ' '))
    return render(request, 'categories.html', {'categories': categories.title().replace('-', ' '), 'category': category})


# View for Categories page
def CategoryList(request):
    categories_list = Category.objects.all()

    return render(request, 'category_list.html', {'categories_list': categories_list})


class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = CreateForm


class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class PostDetail(View):

    # class method to get post details from server
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    # class method to allow users to comment
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            # returns an empty comment form
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
