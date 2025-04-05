from .. import db  # Make sure this points to your initialized db instance
from dal.models.review import Review


# DAL: Get reviews for a dish
def get_reviews_dal(dishid):
    try:
        reviews = Review.query.filter_by(dishid=dishid).all()
        result = [
            {
                "id": review.id,
                "email": review.email,
                "resid": review.resid,
                "dishid": review.dishid,
                "rating": review.rating,
                "review": review.review
            }
            for review in reviews
        ]
        return result, 200
    except Exception as e:
        return {'message': 'Error fetching reviews', 'error': str(e)}, 500


# DAL: Post a new review
def post_review_dal(args):
    try:
        review = Review(
            email=args['email'],
            resid=args.get('resid'),  # Optional, can be None
            dishid=args['dishid'],
            rating=args['rating'],
            review=args['review']
        )
        db.session.add(review)
        db.session.commit()
        return {'message': 'Review submitted successfully'}, 201
    except Exception as e:
        db.session.rollback()
        return {'message': 'Failed to submit review', 'error': str(e)}, 500
