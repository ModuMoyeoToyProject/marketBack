# marketBack: 시장놀이 API 서버
back쪽 레파지토리 + 나중에 합칠예정

## 개발 환경 구축
### Windows
1. [Python](https://www.python.org/)을 설치한다.
1. [Git](https://git-scm.com/)을 설치한다.
1. [PyCharm](https://www.jetbrains.com/ko-kr/pycharm/) 또는 [VSCode](https://code.visualstudio.com/) 와 같은 IDE를 설치한다.
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

## 시스템 요구사항

* Python 3.8.16
* Django 4.1.1 (No LTS)