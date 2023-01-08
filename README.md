# marketBack: 시장놀이 API 서버

back쪽 레파지토리 + 나중에 합칠예정


## 개발 환경 구축


### Windows

1. [Python](https://www.python.org/), [Git](https://git-scm.com/), [PyCharm](https://www.jetbrains.com/ko-kr/pycharm/) 또는 [VSCode](https://code.visualstudio.com/)를 설치한다.
1. Git Bash 터미널을 실행한다.
1. 본 레포지토리를 다운로드한다.
    ```
    git clone https://github.com/ModuMoyeoToyProject/marketBack
    ```
1. 레포지토리에서 IDE를 실행한다. 또는, Bash 터미널에서 레포지토리 내부로 이동한다.
    ```
    cd marketBack # 터미널에서 본 레포지토리 내부로 이동
    ```
1.  IDE 내장 터미널 또는 Bash 터미널에서 다음 절차를 진행한다.
    ```
    python -m venv venv # Python 가상환경 생성
    source venv/Scripts/activate # 가상환경 활성화
    python -m pip install -U pip # pip 패키지 매니저 버전 업그레이드
    pip install -r requirements.txt # Django 및 관련 Python 패키지 설치
    ```
1. Dumpdata로부터 데이터베이스 생성
    ```
    cd BackServer # Django 프로젝트 폴더로 이동 후,
    ```
    하단의 [초기 데이터베이스 백업 및 생성](#초기-데이터베이스-백업-및-생성)에서 `Dumpdata로부터 데이터베이스 생성` 실행
1. IDE에서 Django 서버를 실행시키거나, Bash 터미널에서 수동으로 실행
    ```
    python manage.py runserver 8000 # 8000 포트로 Django 내장 웹서버 런칭
    ```

### Mac

1. Mac을 Apple 홈페이지에서 구매한다.
1. 배송 올 때까지 기다린다. (...)


### Docker

1. [VSCode](https://code.visualstudio.com/)를 설치한다.
1. Docker가 설치된 호스트에 연결한다.
1. VSCode Integrated Terminal(Bash)에서 다음 명령을 차례로 실행한다.
    ```
    git clone https://github.com/ModuMoyeoToyProject/marketBack # 본 레포지토리 다운로드
    cd marketBack # 본 레포지토리 내부로 이동
    docker compose up -d # 개발 컨테이너 생성 및 시작
    ```
1. VSCode에서 해당 컨테이너로 Attach 한다.
1. Dumpdata로부터 데이터베이스 생성
    ```
    cd BackServer # Django 프로젝트 폴더로 이동 후,
    ```
    하단의 [초기 데이터베이스 백업 및 생성](#초기-데이터베이스-백업-및-생성)에서 `Dumpdata로부터 데이터베이스 생성` 실행
1. VSCode로부터 Django 내장 웹서버를 런칭한다.

## 데이터베이스 관리용 Django Admin site

* [http://localhost:8000](http://localhost:8000)

    ![2023-01-04 09 39 29](https://user-images.githubusercontent.com/28856527/210464121-24d336f5-26ad-4698-999b-ae880740e061.png)

* Superuser login
    * username: root
    * password: 1


## 초기 데이터베이스 백업 및 생성

### 데이터베이스 덤프
    ```
    python manage.py dumpdata account.user --indent 4 -o account/migrations/init_user.json # Current user data && \
    python manage.py dumpdata auth.group --indent 4 -o account/migrations/init_auth.group.json # Current group data && \
    python manage.py dumpdata account.group --indent 4 -o account/migrations/init_account.group.json # Current group data && \
    python manage.py dumpdata db --indent 4 -o db/migrations/dumpdata.json && \
    python manage.py dumpdata player --indent 4 -o player/migrations/dumpdata.json && \
    python manage.py dumpdata system --indent 4 -o system/migrations/dumpdata.json
    ```
### Dumpdata로부터 데이터베이스 생성
    ```
    rm db.sqlite3 # Delete current DB && \
    python manage.py makemigrations && \
    python manage.py migrate # Create empty DB && \
    python manage.py loaddata account/migrations/init_user.json && \
    python manage.py loaddata account/migrations/init_auth.group.json && \
    python manage.py loaddata account/migrations/init_account.group.json && \
    python manage.py loaddata db/migrations/dumpdata.json && \
    python manage.py loaddata player/migrations/dumpdata.json && \
    python manage.py loaddata system/migrations/dumpdata.json
    ```
### For more information, Refer to [dumpdata](https://docs.djangoproject.com/en/4.1/ref/django-admin/#dumpdata) and [loaddata](https://docs.djangoproject.com/en/4.1/ref/django-admin/#loaddata)


## Visualize ER-Diagram

### Docker

1. Install dependencies.
    ```
    apt update && apt install -y graphviz
    pip install django-extensions pydotplus # These are contained in the requirements.txt
    ```
1. Create Model Digram and save to png file.
    ```
    python manage.py graph_models -ago ERD.png --arrow-shape normal --color-code-deletions --rankdir BT -X AbstractUser,LogEntry,Group,Permission,ContentType,Session,AbstractBaseUser,PermissionsMixin,AbstractBaseSession
    ```
1. For more information, Refer to [Graph models](https://django-extensions.readthedocs.io/en/latest/graph_models.html#example-usage)


## i18n support

1. Install [gettext/iconv](https://mlocati.github.io/articles/gettext-iconv-windows.html) or `apt update && apt install -y gettext`
1. Wrapping string using `from django.utils.translation import ugettext_lazy as _`
1. Create initial translation file
    ```
    python manage.py makemessages -l en
    python manage.py makemessages -l ko
    ```
    or,
    ```
    python manage.py makemessages -a
    ```
1. Compile translation file(\*.po) to binary file(\*.mo).
    ```
    python manage.py compilemessages
    ```
1. Restart django server
