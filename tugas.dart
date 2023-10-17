// Dart code for sequencegenerator
List<int> sequenceGenerator(int start, int stop) {
  List<int> result = [];
  for (int i = start; i <= stop; i++) {
    result.add(i);
  }
  return result;
}

void main() {
  print(sequenceGenerator(1, 10));

  // Dart code for fizzbuzz
  List<dynamic> fizzBuzz(int a, int b) {
    List<dynamic> result = [];
    for (int num = a; num <= b; num++) {
      if (num % 3 == 0 && num % 5 == 0) {
        result.add('FizzBuzz');
      } else if (num % 3 == 0) {
        result.add('Fizz');
      } else if (num % 5 == 0) {
        result.add('Buzz');
      } else {
        result.add(num);
      }
    }
    return result;
  }

  print(fizzBuzz(1, 20));
}