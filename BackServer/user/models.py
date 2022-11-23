from django.db import models
'''1.모델 작성 후 forms.py로 이동'''

class User(models.Model):
    GenderChoices = [(None,'성별 선택'),('Men','남성'),('Women','여성')]
    userName = models.CharField(max_length = 255)
    birthday=models.DateField(auto_now=False, null=True, blank=True)
    userGender = models.CharField(max_length = 10,choices = GenderChoices,default = '성별 선택')
    nickname = models.CharField(max_length = 30)
    password = models.CharField(max_length = 255)
    emailAddress= models.EmailField(max_length = 30)
    
    def __str__(self):
        return self.userName