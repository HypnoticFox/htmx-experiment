import datetime
from django.utils import timezone

from polls.models import Question

def test_was_published_recently_with_old_question():
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    assert old_question.was_published_recently() == False


def test_was_published_recently_with_recent_question():
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    assert recent_question.was_published_recently() == True