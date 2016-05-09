def donuts(count):
    c = count
    msg = ""
    if c > 9:
        msg = "Many"
    else:
        msg = str(c)
    return 'Number of donuts: ' + msg

def main():
  print(donuts)
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

  print

if __name__ == '__main__':
  main()
