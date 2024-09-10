from django.db import models

# Create your models here.
"""
This module contains the definitions for two models for the polls app.

Question - represents a question that can be answered by the user by selecting from a choice.
Choice - represents a possible choice for a question. A track is kept for the number of votes of each choice.
"""

class Question(models.Model):
    """The Question Model has two fields:
    - question_text(CharField): this is limited to 200 characters.
    - pub_date (DateTimeField): the is the date and time the question was published.

    The '__str__' method returns a suitable string representation of the object for the model.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    """
    The Choice Model has three fields:
    question (ForeignKey): this is a foreign key related to the 'Question' instance and therefore indicates which question the choice belongs to.
    choice_text (CharField): this is the text of the choice and is limited to 200 characters.
    votes (IntegerField): this is the number of votes recevied by this choice. The default is 0 votes.

    The '__str__' method returns a suitable string representation of the object for the model.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text