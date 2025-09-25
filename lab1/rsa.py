def is_prime(n: int) -> bool:  
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
        raise ValueError("обратного нет")

   
    d = coeff_prev % phi
    return d


def smallest_e(phi):
    candidate_e = 3             
    while candidate_e < phi:
        if  gcd(candidate_e, phi) == 1:
            return candidate_e 
        else:
            candidate_e = candidate_e + 2  
   
def generate_keypair(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    if p!=q and is_prime(p)==True and is_prime(q)==True:
        n=p*q
        phi=(p-1)*(q-1)
        e=smallest_e(phi)
        d=multiplicative_inverse(e,phi)
        
        return [[e,n],[d,n]]
    
