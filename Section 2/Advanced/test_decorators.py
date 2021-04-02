user = {'username': 'alt', 'access_level':'guest'}

def get_admin_password():
    return '1234'


def make_secure(func):
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return 'Not enough privilegies.'

    return secure_function

# nesse ponto, o que ocorre é o seguinte... Definimos que a função get_admin_password 
# agora é instanciada dentro de make_secure, o que a torna, após essa linha de código, segura

get_admin_password = make_secure(get_admin_password)