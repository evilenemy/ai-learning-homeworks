def check(func):
  def wrapper(a, b):
    try:
      return func(a, b)
    except ZeroDivisionError:
      return "Denominator can't be zero"
  return wrapper

@check
def div(a, b):
  return a / b

print(div(10, 2))  # Should print 5.0
print(div(10, 0))  # Should print "ZeroDivisionError: You cannot divide by zero!"