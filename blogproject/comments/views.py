from django.http import HttpResponseRedirect
from django.urls import reverse
from comments.models import Comment

def comment(request,post_id):
    post_id = int(post_id)
    post0 = request.POST
    name = post0['name']
    text = post0['comment']
    com = Comment()
    com.name = name
    com.text = text
    com.post_id = post_id
    com.save()
    return HttpResponseRedirect(reverse('blog:detail', args=(post_id,)))
