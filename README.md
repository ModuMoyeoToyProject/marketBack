# marketBack: 시장놀이 API 서버

back쪽 레파지토리 + 나중에 합칠예정


## 개발 환경 구축


### Windows

1. [Python](https://www.python.org/), [Git](https://git-scm.com/), [PyCharm](https://www.jetbrains.com/ko-kr/pycharm/) 또는 [VSCode](https://code.visualstudio.com/)를 설치한다.
1. Git Bash 터미널을 실행한다.
1. 다음 명령을 차례로 실행한다.
    ```
    git clone https://github.com/ModuMoyeoToyProject/marketBack # 본 레포지토리 다운로드
    cd marketBack # 본 레포지토리 내부로 이동
    python -m venv venv # Python 가상환경 생성
    source venv/Script/Activate # 가상환경 활성화
    pip install -r requirements.txt # Django 및 관련 Python 패키지 설치
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


## 데이터베이스 관리용 Django Admin site

* [http://localhost:8000](http://localhost:8000)

    ![2023-01-04 09 39 29](https://user-images.githubusercontent.com/28856527/210464121-24d336f5-26ad-4698-999b-ae880740e061.png)

* Superuser login
    * username: root
    * password: 1

## 시스템 요구사항

* Python 3.8.16
* Django 4.1.1 (Non LTS)


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


## Dump and load initial database

1. Dump current database
    ```
    python manage.py dumpdata --indent 4 -o dumpdata.json # Including django system database table
    ```
    or,
    ```
    python manage.py dumpdata account --indent 4 -o account/migrations/dumpdata.json && \
    python manage.py dumpdata db --indent 4 -o db/migrations/dumpdata.json && \
    python manage.py dumpdata player --indent 4 -o player/migrations/dumpdata.json && \
    python manage.py dumpdata system --indent 4 -o system/migrations/dumpdata.json
    ```
1. Restore dumpdata to Database
    ```
    rm db.sqlite3
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py loaddata dumpdata.json
    ```
    or,
    ```
    rm db.sqlite3
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py loaddata account/migrations/dumpdata.json db/migrations/dumpdata.json player/migrations/dumpdata.json system/migrations/dumpdata.json
    ```
1. For more information, Refer to [dumpdata](https://docs.djangoproject.com/en/4.1/ref/django-admin/#dumpdata) and [loaddata](https://docs.djangoproject.com/en/4.1/ref/django-admin/#loaddata)
<<<<<<< HEAD


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
=======
>>>>>>> upstream/skill_activity#7
