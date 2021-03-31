class File:
  results_arr = []
  positive_arr = []
  negative_arr = []
  positive = 'positive.txt'
  negative = 'negative.txt'

  def __init__(self, f, operation):
    self.f = f
    self.operation = operation

  def file_worker(self):
    file = open(self.f, 'r')
    if self.operation == '*' or self.operation == '/' or self.operation == '+' or self.operation == '-':
      for line in file:
        resultMultDiv = 1
        resultPlusMin = 0
        new_line = line.strip().split(' ')
        for i in range(len(new_line)):
          if self.operation == '*':
            resultMultDiv *= int(new_line[i])
          elif self.operation == '/':
            if i == 0:
              resultMultDiv = int(new_line[0])
            else:
              resultMultDiv = resultMultDiv / int(new_line[i])
          elif self.operation == '+':
            resultPlusMin += int(new_line[i])
          elif self.operation == '-':
            if i == 0:
              resultPlusMin = int(new_line[0])
            else:
              resultPlusMin -= int(new_line[i])
        if self.operation == '*' or self.operation == '/':
          self.results_arr.append(resultMultDiv)
        else:
          self.results_arr.append(resultPlusMin)
      file.close()

      for i in self.results_arr:
        # Ноль это не положительное и не отрицательное число
        if i < 0:
          self.negative_arr.append(i)
        elif i > 0:
          self.positive_arr.append(i)

      file = open(self.positive, 'w')
      for index in self.positive_arr:
        file.write(str(index) + '\n')
      file.close()

      file = open(self.negative, 'w')
      for index in self.negative_arr:
        file.write(str(index) + '\n')
      file.close()
      
      
      return (self.positive_arr, self.negative_arr)
    return None

A = File(input("Укажите путь к файлу: "), input("Укажите арифметическую операцию: "))
print(A.file_worker())