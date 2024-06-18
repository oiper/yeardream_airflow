def get_sftp():
    print('sftp 작업을 시작합니다')
    

def regist(name, sex, *args):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')


def regist2(name, sex, *args, **kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')
    email = kwargs['email'] or 'empty'
    phone = kwargs['phone'] or 'empty'
    if email:
        print(email)
    if phone:
        print(phone)

    kwargs_interval_start = kwargs.get('data_interval_start')
    print(kwargs_interval_start)
    interval_end = kwargs.get('data_interval_end')
    print(interval_end)