def is_prime(n: int) -> bool:  #алгоритм перебора делителей до кв корня 
  ''' 
  '''
  if n <= 1:
    return False
  if n == 2:
    return True 
  for i in range(2, int( n**0.5 ) + 1 ):
        if n % i == 0:
            return False
  return True


def gcd(a: int, b: int) -> int:   
  ''' '''
  while b!=0:
    a, b = b, a%b
  return a

  
def multiplicative_inverse(e: int, phi:int) -> int:
  for i in range(1,phi):
    if (d*e)%phi==1:
      return d
  raise ValueError('no inverse num')
  

  
  
  
def generate_keypair(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    ''' '''
