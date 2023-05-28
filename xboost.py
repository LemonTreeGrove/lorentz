import math


def gamma(v):
  return math.sqrt(1/(1-(v**2)))


def boost(v, event):
  result = []
  y = gamma(v)
  result.append(y*(event[0] - v*event[1]))
  result.append(y*(event[1] - v*event[0]))
  result.append(event[2])
  result.append(event[3])
  return result


def time_dialation(v):
  t = [t, 0, 0, 0]
  t_prime = boost(v, t)
  return t_prime[0]


print(time_dialation(.5))
