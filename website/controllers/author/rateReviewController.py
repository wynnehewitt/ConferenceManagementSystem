from django.shortcuts import render, redirect
from ...models import Review, ReviewRating, Paper, Author, Reviewer

from django.contrib import messages

def rateReview(request):
    author_id = request.session["AuthorLogged"]
    if request.method == "POST":
        paper = Paper.getPaper(request.POST["paper_id"])
        reviewer = Reviewer.getReviewerByID(request.POST["reviewer_id"])
        author = Author.getAuthorByID(author_id)
        rating = request.POST["rating"]
        success = ReviewRating.createReviewRating(paper, reviewer, author, rating)
        if(success):
            messages.success(request, "Successfully submitted your rating. Thank you for your submission.")
            return redirect('rateReview')
        else:
            messages.error(request, "There was an error submitting your rating.")
            return redirect('rateReview')
    else:
        # rate review
        review_list = Review.getAllReview()
        final_review_list = []
        for review in review_list:
            paper = Paper.getPaper(review.paper_id)
            author_list = list(paper.authors.all().values_list('id', flat=True))
            authorHasReviewed = ReviewRating.objects.filter(paper_id = review.paper_id).filter(reviewer_id = review.reviewer_id).filter(author_id=author_id).count()

            if author_id in author_list and authorHasReviewed == 0:
                final_review_list.append(review)
            
        # view rated review
        reviewRating_list = ReviewRating.getAllReviewRating()
        print(reviewRating_list)
        finalReviewRating_list = []
        for reviewRating in reviewRating_list:
            print(reviewRating.paper_id)
            paper = Paper.getPaper(reviewRating.paper_id)
            print(f'paper{paper}')
            author_list = list(paper.authors.all().values_list('id', flat=True))
            print(f'author:{author_id}')
            print(f'author_list{author_list}')
            if author_id in author_list:
                print("true")
                finalReviewRating_list.append(reviewRating)

        context = {'final_review_list': final_review_list, 'finalReviewRating_list': finalReviewRating_list}
        return render(request, 'author/rateReview.html', context)

def deleteReviewRating(request, id):
    success = ReviewRating.deleteReviewRating(id)

    if(success):
        messages.success(request, f"Successfully delete reviewRating ID {id}")
    else:
        messages.error(request, f"Fail to delete reviewRating ID {id}")

    return redirect('rateReview')