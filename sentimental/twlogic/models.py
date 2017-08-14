from django.db import models

# Create your models here.


class Twacount(models.Model):
    acount = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return ("@"+self.acount)


class Twcomment(models.Model):
    Twid = models.CharField(max_length=200, primary_key=True)
    acount = models.ForeignKey(Twacount, verbose_name='acount')
    comment = models.CharField(max_length=140)
    retweet_count = models.IntegerField(blank=True, null=True)
    retweeted = models.BooleanField(default=False)
    created_at = models.CharField(max_length=200)
    negative = models.FloatField()  # 0
    positive = models.FloatField()  # 1
    neutral = models.FloatField()   # 2
    query = models.CharField(max_length=140)

    def sentiment(self):
        neg = self.negative
        pos = self.positive
        neu = self.neutral
        if neg > pos and neg > neu:
            return 'NE'
        else:
            if pos > neg and pos > neu:
                return 'PO'
            else:
                return 'NT'

    def __unicode__(self):
        return self.comment + " Polarity:" + self.sentiment()
