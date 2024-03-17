//Perform mathematical operations with functions
void main() {
  int num1 = 20;
  int num2 = 8;

  int result1 = add(num1, num2);
  int result2 = multiply(num1, num2);

  print("The sum of $num1 and $num2 is $result1");
  print("The product of $num1 and $num2 is $result2");
}

int add(int a, int b) {
  return a + b;
}

int multiply(int a, int b) {
  return a * b;
}
