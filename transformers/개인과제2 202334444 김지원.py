userId = str(input('아이디를 입력하세요:'))
if userId == 'lovePython!':
    userPwd = input('비밀번호를 입력하세요: ')
    if userPwd == 'p12345':
        print('{}님 환영합니다~!!'.format(userId))
    else:
        print('비밀번호가 틀립니다.')
else:
    print('아이디를 찾을 수 없습니다.')