# Para ver uma lista de todos os pacotes e bibliotecas que você instalou com o pip 
# usa-se o seguinte comando no terminal do VS Code: pip list

# Este comando vai listar o nome de todos os pacotes instalados e suas versões, de forma clara e organizada. 
# Se você está usando um ambiente virtual, o pip list mostrará apenas os pacotes instalados dentro daquele ambiente, 
# o que é a maneira correta de gerenciar as dependências do seu projeto.

# Para ver o que um módulo te oferece (import random, por exemplo)

# >>> import random
# >>> dir(random)
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', 
# '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
# '__name__', '__package__', '_acos', '_ceil', '_cos', '_e', '_exp', '_floor', '_inst', '_log', '_log2', 
# '_pi', '_random', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 
# 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 
# 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 
# 'uniform', 'vonmisesvariate', 'weibullvariate']

# from random import randint - Posso importar somento o método
#teste1 = randint(0,100) e usar ele
# ou importar o random e chamar de outra forma

import random

teste1 = random.randint(0,100)
print(teste1)
print()

