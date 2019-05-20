# ToDoList

Individual project for Programmers 2019 Summer Coding


# 기능
- 새로운 TODO(제목과 내용) 작성
- ToDO 목록 조회
- TODO 항목의 제목과 내용을 수정
- TODO 항목을 삭제
- TODO 우선순위 설정 및 조절
- TODO 항목에 대한 완료 처리
- 마감기한이 지난 TODO에 대해 알림 노출


# 설치 및 빌드 방법

Homebrew를 설치하기 위해서는 Xcode에 포함된 Command Line Tools(개발자용 명령어 라인 도구)가 필요합니다.
</br> $ xcode-select --install # 
</br> $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
설치
</br> $ brew install pyenv

그러면 다른 창이 나타날 것입니다. 아래에서 괄호를 제외한 부분을 입력해 주세요.

(i를 누른다.)
</br> if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
</br> if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
</br> (esc를 누른다.)
</br> :wq
</br> (enter를 누른다.)
</br> 다시 원래 보던 터미널이 나타날 것입니다. 위의 과정은 터미널에게 pyenv 명령을 알아듣도록 만든 것입니다. 마지막으로 터미널을 다시 load하는 과정이 필요하니 아래 명령을 입력하세요.

$ source ~/.bash_profile

 파이썬을 설치해 줍니다.
</br> $ pyenv install 3.6.8

이제 Django를 설치해 봅시다.
</br>$ pip install django
