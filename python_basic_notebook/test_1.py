import sys
def main():
  if len(sys.argv) != 3:          # check if number of arguments meet requirements
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]            # assignment arguments
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()