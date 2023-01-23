from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import auth
from player.models import *
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

def create_charactor(user):
    character = Character(user=user)
    character.save()
    inventory = Inventory(character=character)
    inventory.save()
    status = Status(character=character)
    status.save()

@csrf_exempt # TODO CSRF 예외 데코레이터 삭제할 수 있도록 공부...
def register(request):
    if request.method == 'POST': # TODO 매번 API 마다 method == post 확인하는 로직 쓰지 말고 클래스뷰 공부해보기!
        response = dict()
        print(request.POST['password1'])
        if request.POST['password1'] == request.POST['password2']:
            try:
                if not User.objects.filter(username=request.POST['username']).exists():
                    new_user = User.objects.create_user(
                        username=request.POST['username'], # Valid username test
                        nickname=request.POST['nickname'],
                        email=request.POST['email'], # TODO Valid email test
                        password=request.POST['password1'],
                        gender=request.POST['gender'],
                    )
                    auth.login(request, new_user) # 회원가입과 동시에 로그인 처리
                    response['result'] = 'Successed'
                    create_charactor(new_user)
                else:
                    response['result'] = 'AlreadyExists' # 같은 username이 이미 DB에 존재함
            except Exception as e:
                print(e)
                if settings.DEBUG:
                    response['result'] = f'Failed: {e}'
                else:
                    response['result'] = 'Failed' # 어떤 알수없는 이유로 실패, Exception 정보는 보안상 response로 보내지 않음
        else:
            response['result'] = 'NotMatchedPassword'
        return JsonResponse(response)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        response = dict()
        user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password']) # 사용자 입력 ID와 PW가 유효한지 체크
        if user is not None and user.is_active: # user 객체가 정상적으로 생성되었다면 로그인정보가 유효하다는 뜻, is_active는 사용가능한 상태인지 확인
            auth.login(request, user) # 로그인 처리
            response['result'] = 'SuccessedLogin'
        else:
            response['result'] = 'FailedLogin'
        return JsonResponse(response)
