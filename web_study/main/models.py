from django.db import models

# Create your models here.
# 숫자형 : IntegerField(정수형), Floatfield(실수형)
# 문자형 : CharField, Textfield, EmailField, URLfield
# 날짜형 : DateTimeField, DateField, EmailField, URLField
# 기타유형 : BooleanField, FileField, ImageField, NullBooleanField, SlugField

# 필드속성
# Primary_key : PK 설정, PK설정이 없을경우 ID 열을 자동 생성
# max_length : 데이터 길이 설정
# blank : 공백 허용 여부 (브라우저의 데이터가 없어도 됨을 의미)
# null : null값 허용 여부 (DB에 null값을 저장 가능)
# default : 기본값 설정
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)
# Post 내용을 문자로 변환시켜줌
    def __str__(self):
        return self.postname
