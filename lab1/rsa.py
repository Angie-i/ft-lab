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

def multiplicative_inverse(e, phi):
    remainder_prev = e       
    remainder_curr = phi     
    coeff_prev = 1           
    coeff_curr = 0           
    while remainder_curr != 0:
        quotient = remainder_prev // remainder_curr
        temp = remainder_prev
        remainder_prev = remainder_curr
      
        remainder_curr = temp - quotient * remainder_curr
        temp = coeff_prev
        coeff_prev = coeff_curr
        coeff_curr = temp - quotient * coeff_curr

    if remainder_prev != 1:
        raise ValueError("обратного не существует")

   
    d = coeff_prev % phi
    return d
  

  
  
  
def generate_keypair(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    ''' '''
