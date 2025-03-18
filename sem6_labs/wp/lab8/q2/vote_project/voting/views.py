# voting/views.py
from django.shortcuts import render
from .models import BookVote

def vote(request):
    if request.method == 'POST':
        choice = request.POST.get('vote_choice')
        if choice:
            # Update the vote count for the selected choice
            vote = BookVote.objects.get(choice=choice)
            vote.count += 1
            vote.save()

    # Fetch the vote counts for each choice
    total_votes = sum(vote.count for vote in BookVote.objects.all())
    if total_votes > 0:
        good_percentage = (BookVote.objects.get(choice='Good').count / total_votes) * 100
        satisfactory_percentage = (BookVote.objects.get(choice='Satisfactory').count / total_votes) * 100
        bad_percentage = (BookVote.objects.get(choice='Bad').count / total_votes) * 100
    else:
        good_percentage = satisfactory_percentage = bad_percentage = 0

    context = {
        'good_percentage': good_percentage,
        'satisfactory_percentage': satisfactory_percentage,
        'bad_percentage': bad_percentage,
        'total_votes': total_votes,
    }
    return render(request, 'voting/vote.html', context)
