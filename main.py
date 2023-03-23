import os
from tabulate import tabulate


#FCFS CODE
def fcfs():
  burst_time = []
  waiting_time = []
  turnaround_time = []
  Process = []
  b = 0
  wt = 0
  tt = 0

  while True:
    try:
      process_num = int(
        input('Enter Total Number of Processes [minumum: 3 and maximum: 10]:'))
    except ValueError:
      print('Please enter a number [minumum: 3 and maximum: 10].\n')
      continue
    if process_num < 3:
      print('Enter a valid number [minumum: 3 and maximum: 10].\n')
      continue
    elif process_num > 10:
      print('Enter a valid number [minumum: 3 and maximum: 10].\n')
      continue
    else:
      pass

    print('\nEnter Process Burst Time [minimum: 1 and maximum: 15]:')

    for c in range(process_num):
      while True:
        try:
          x = int(input("Burst time of Process " + str(c + 1) + ': '))
          if x < 1:
            print(
              'Invalid burst time. Enter a number [minumum: 1 and maximum: 15].\n'
            )
            continue
          elif x > 15:
            print(
              'Invalid burst time. Enter a number [minumum: 1 and maximum: 15].\n'
            )
            continue
          burst_time.append(x)
          break
        except ValueError:
          print("Invalid input. Please enter a valid number.\n")

    while (b < process_num):
      tt += burst_time[b]
      waiting_time.append(wt)
      turnaround_time.append(tt)
      Process.append(b + 1)
      wt += burst_time[b]
      b += 1

    headers = ["Process", "Burst Time", "Waiting Time", "Turnaround Time"]
    table = zip(Process, burst_time, waiting_time, turnaround_time)
    print("\n")
    print(tabulate(table, headers=headers, tablefmt="grid"))

    print('\nGantt Chart:\n')
    table = "+"
    table2 = "|"
    c = [1]
    for a in burst_time:
      d = int(a / 2)
      e = float(a / 2)
      if a <= 1:
        b = 1
        f = 0
      else:
        if d == e:
          b = d - 1
          f = d
        elif d != e:
          b = d
          f = d
      print(str(" " * b) + str("P" + str(c[0])) + str(" " * f), end="")
      table = table + (str("-") * int(a))
      table2 = table2 + (str(" ") * int(a))
      table = table + "+"
      table2 = table2 + "|"
      c[0] = c[0] + 1
    print("\n")
    print(table)
    print(table2)
    print(table)
    print("0", end="")
    for a in range(len(burst_time)):
      z = len(str(turnaround_time[a]))
      if z == 1:
        b = str(" ") * int(burst_time[a])
      elif z == 2:
        b = str(" ") * int(burst_time[a] - 1)
      elif burst_time[a] <= 1:
        b = str(" ") * int(1)

      print(str(b) + str(turnaround_time[a]), end="")
    print("\n")

    avg_wt = float("{:.2f}".format(sum(waiting_time) / len(waiting_time)))
    avg_tt = float("{:.2f}".format(
      sum(turnaround_time) / len(turnaround_time)))
    print('\nAverage Waiting Time: ' + str(avg_wt) + ' ms' +
          '\nAverage Turnaround Time: ' + str(avg_tt) + ' ms')
    break


#end of fcfs


#SJF CODE
def sjf():
  process_burst = {}
  burst_time = []
  waiting_time = []
  turnaround_time = []
  process = []
  b = 0
  wt = 0
  tt = 0
  while True:
    try:
      process_num = int(
        input(
          'Enter Total Number of Processes [minumum: 3 and maximum: 10]: '))
    except ValueError:
      print('Please enter a number (min 3 & max 10).\n')
      continue
    if process_num < 3:
      print('Please enter a number [minumum: 3 and maximum: 10].\n')
      continue
    elif process_num > 10:
      print('Please enter a number [minumum: 3 and maximum: 10].\n')
      continue
    else:
      pass

    print('\nEnter Process Burst Time [minimum: 1 and maximum: 15]:')

    for c in range(process_num):
      while True:
        try:
          x = int(input('P[' + str(c + 1) + ']:'))
          if x < 1:
            print(
              'Invalid burst time. Enter a number [minumum: 1 and maximum: 15].\n'
            )
            continue
          elif x > 15:
            print(
              'Invalid burst time. Enter a number [minumum: 1 and maximum: 15].\n'
            )
            continue
          process_burst[c] = x
          break
        except ValueError:
          print("Invalid input. Please enter a valid number.\n")

    sort_burst = dict(sorted(process_burst.items(), key=lambda x: x[1]))
    process = list(sort_burst.keys())
    burst_time = list(sort_burst.values())
    print("\n")

    for a in range(len(burst_time)):
      process[a] = int(process[a] + 1)
      tt += int(burst_time[a])
      waiting_time.append(wt)
      turnaround_time.append(tt)
      wt += int(burst_time[a])

    headers = ["Process", "Burst Time", "Waiting Time", "Turnaround Time"]
    table = zip(process, burst_time, waiting_time, turnaround_time)
    print(tabulate(table, headers=headers, tablefmt="grid"))
    #SJF Gantt Chart
    print('\nGantt Chart:\n')
    table = "+"
    table2 = "|"
    for a in range(len(burst_time)):
      d = int(int(burst_time[a]) / 2)
      e = float(int(burst_time[a]) / 2)
      if int(burst_time[a]) <= 1:
        b = 1
        f = 0
      else:
        if d == e:
          b = d - 1
          f = d
        elif d != e:
          b = d
          f = d
      print(str(" " * b) + str("P" + str(process[a])) + str(" " * f), end="")
      table = table + (str("-") * int(burst_time[a]))
      table2 = table2 + (str(" ") * int(burst_time[a]))
      table = table + "+"
      table2 = table2 + "|"
    print("\n")
    print(table)
    print(table2)
    print(table)
    print("0", end="")
    for a in range(len(burst_time)):
      z = len(str(turnaround_time[a]))
      if z == 1:
        b = str(" ") * int(burst_time[a])
      elif z == 2:
        b = str(" ") * int(int(burst_time[a]) - 1)
      elif burst_time[a] <= 1:
        b = str(" ") * int(1)

      print(str(b) + str(turnaround_time[a]), end="")
    print("\n")
    #To calculate for Average Waiting time and TurnAround time
    avg_wt = float("{:.2f}".format(sum(waiting_time) / len(waiting_time)))
    avg_tt = float("{:.2f}".format(
      sum(turnaround_time) / len(turnaround_time)))
    print('\nAverage Waiting Time: ' + str(avg_wt) + ' ms' +
          '\nAverage Turnaround Time: ' + str(avg_tt) + ' ms')

    break


#end of SJF code


#SRTF CODE
def srtf():
  processNum = []
  processes = []
  arrivalTime = []
  arrivalTime2 = []
  burstTime = []  #unchanged
  burstTime2 = []  #for the whole process of subtracting etc
  firstOccurProcessNum = []
  firstOccurence = []
  responseTime = []
  duplicates_index = []  #saves the index of duplicates
  nonzero_index = []  # saves the index of non zero bursttime
  not_index = []
  nonzero_burstTime = []  #saves non zero bursttimes
  completionTime = []
  turnaroundTime = []
  waitingTime = []
  currentBurst = [0, 0]  #value #index
  current_time = 0
  sjf_current = [0]
  sjf_index = []
  sjf_arrival = []
  duplicateburst_arrivalindex = []
  duplicateburst_arrival = []
  gantt = []

  def ProcessCount():  #getting the total number of processes
    while True:
      try:
        x = int(
          input(
            "Enter the number of processes (minimum of 5 and maximum of 10): ")
        )
        if 5 <= x <= 10:
          for a in range(x):
            processes.append(a + 1)
          return x
        else:
          print(
            "Invalid input. Number of processes must be between 5 and 10.\n")
      except ValueError:
        print("Invalid input. Only integers are allowed.\n")

  def BurstTime(process):  #getting the burst times
    b = 1
    print("\n")
    print(
      "Enter the number of burst time on each process (minimum of 5 and maximum of 15)."
    )
    for a in range(process):
      while True:
        try:
          processNum.append(b)
          x = int(input("Burst time of Process " + str(b) + ": "))
          if 5 <= x <= 15:
            firstOccurence.append(0)
            burstTime.append(x)
            burstTime2.append(x)
            completionTime.append(0)
            process -= 1
            b += 1
            break
          else:
            print("\nInvalid input. Burst time must be between 5 and 15.\n")
        except ValueError:
          print("Invalid input. Only integers are allowed.\n")

  def ArrivalTime(process):  #getting the arrival times
    b = 1
    print("\n")
    print(
      "Enter the number of arrival time on each process (minimum of 0 and maximum of 12)."
    )
    for a in range(process):
      while True:
        try:
          x = int(input("Arrival time of Process " + str(b) + ": "))
          if 0 <= x <= 12:
            arrivalTime.append(x)
            arrivalTime2.append(x)
            process -= 1
            b += 1
            break
          else:
            print("\nInvalid input. Arrival time must be between 0 and 12.\n")
        except ValueError:
          print("Invalid input. Only integers are allowed.\n")

  def DuplicateIndex(list,
                     item):  #gets the index of the duplicate arrival time
    for idx, value in enumerate(list):
      if value == (item):
        duplicates_index.append(idx)
    return duplicates_index

  def CompareBursttime(
      list, duplicatecount, i,
      indexList):  #gets the burst time of the same arrival time
    min_number = None
    index = 0  #index of final min_number
    for a in range(duplicatecount):
      x = indexList[a]
      if min_number is None:
        min_number = list[x]
        index = x
      elif min_number is not None:
        if list[x] < min_number:
          min_number = list[x]
          index = x
        elif list[x] > min_number:
          min_number = min_number
          index = index
    currentBurst[1] = index
    if min_number is not None:
      if currentBurst[0] == 0:
        Process(burstTime2, index, i)
      elif currentBurst[0] <= min_number and currentBurst[0] != 0:
        if currentBurst[0] == min_number and currentBurst[0] != 0:
          if burstTime2.count(currentBurst[0]) > 1:
            for idx, value in enumerate(
                burstTime2):  #for same burst time different arrival
              if value == (currentBurst[0]):
                duplicateburst_arrivalindex.append(idx)
            for a in duplicateburst_arrivalindex:
              duplicateburst_arrival.append(arrivalTime2[a])
            y = duplicateburst_arrival.index(min(duplicateburst_arrival))
            z = duplicateburst_arrivalindex[y]
            burstTime2[z] -= 1
            currentBurst[0] = burstTime2[z]
            currentBurst[1] = z
            gantt.append(z)
            if (currentBurst[1] not in firstOccurProcessNum):
              firstOccurProcessNum.append(currentBurst[1])
              firstOccurence[currentBurst[1]] = i
            if burstTime2[z] == 0:
              completionTime[z] = i + 1
            duplicateburst_arrival.clear()
            duplicateburst_arrivalindex.clear()
          else:
            Process2(currentBurst, 0, i)
        elif currentBurst[0] < min_number and currentBurst[0] != 0:
          Process2(currentBurst, 0, i)
      elif currentBurst[0] > min_number:
        Process(burstTime2, index, i)

  def Process(list, x, i):  #x for index of bursttime, i for current time
    if list[x] < 1:
      print("Finished")
    elif list[x] > 0:
      list[x] -= 1
      currentBurst[0] = list[x]
      gantt.append(x)
      CompareCurrent(list[x], x, i)
      if list[x] == 0:
        completionTime[x] = i + 1

  def Process2(list, x, i):  #x for index of bursttime, i for current time
    if list[x] < 1:
      print("Finished")
    elif list[x] > 0:
      y = burstTime2.index(list[x])
      list[x] -= 1
      burstTime2[y] = list[x]
      gantt.append(y)
      CompareCurrent(list[x], y, i)
      if list[x] == 0:
        completionTime[y] = i + 1

  def NonZeroBurst():  #getting the non-zero burst times
    for a in range(len(nonzero_index)):
      x = nonzero_index[a]
      y = burstTime2[x]
      nonzero_burstTime.append(y)
    z = min(nonzero_burstTime)  #minimum burst time
    b = nonzero_burstTime.index(z)
    c = nonzero_index[b]
    gantt.append(c)
    CompareCurrent(burstTime2[c])

  def Duplicates(i):  #deals with 2 or more same arrival time
    y = int(arrivalTime2.count(i))  #count of same arrival time x
    if y > 1:
      DuplicateIndex(arrivalTime2, i)
      CompareBursttime(burstTime2, y, i, duplicates_index)
      duplicates_index.clear()
    elif y == 1:
      x = arrivalTime2.index(i)
      CompareCurrent1(burstTime2[x], x, i)

  def CompareCurrent(
    next_burst, index, i
  ):  #comparing the current selected burst time to the next lowest burst time
    if currentBurst[0] < 1:
      currentBurst[0] = next_burst
      currentBurst[1] = index
    elif currentBurst[0] > 0:
      if currentBurst[0] > next_burst:
        currentBurst[0] = next_burst
        currentBurst[1] = index
      elif currentBurst[0] < next_burst:
        currentBurst[0] = currentBurst[0]
        currentBurst[1] = currentBurst[1]
      elif currentBurst[0] == next_burst:
        currentBurst[0] = currentBurst[0]
        if arrivalTime2[currentBurst[1]] > arrivalTime2[index]:
          currentBurst[1] = index
        elif arrivalTime2[currentBurst[1]] < arrivalTime2[index]:
          currentBurst[1] = currentBurst[1]

    if currentBurst[1] not in firstOccurProcessNum:
      firstOccurProcessNum.append(currentBurst[1])
      firstOccurence[currentBurst[1]] = i

  def CompareCurrent1(
    next_burst, index, i
  ):  #comparing the current selected burst time to the next lowest burst time
    if currentBurst[0] < 1:
      currentBurst[0] = next_burst
      currentBurst[1] = index
    elif currentBurst[0] > 0:
      if currentBurst[0] > next_burst:
        currentBurst[0] = next_burst
        currentBurst[1] = index
      elif currentBurst[0] < next_burst:
        currentBurst[0] = currentBurst[0]
        currentBurst[1] = currentBurst[1]
      elif currentBurst[0] == next_burst:
        currentBurst[0] = currentBurst[0]
        if arrivalTime2[currentBurst[1]] > arrivalTime2[index]:
          currentBurst[1] = index
        elif arrivalTime2[currentBurst[1]] < arrivalTime2[index]:
          currentBurst[1] = currentBurst[1]

    if 0 in burstTime2:
      burstTime_nonzero = burstTime2.copy()
      d = burstTime2.count(0)
      for a in range(d):
        burstTime_nonzero.remove(0)
      x = min(burstTime_nonzero)
      burstnonzero_index = []
      arrivalnonzero = []
      arrivalnonzero_index = []
      if currentBurst[0] != x:
        for a, value in enumerate(burstTime2):
          if value == x:
            burstnonzero_index.append(a)
        print(burstnonzero_index)

        for a in burstnonzero_index:
          arrivalnonzero.append(arrivalTime[a])
        y = min(arrivalnonzero)
        z = arrivalnonzero.index(y)
        currentBurst[1] = burstnonzero_index[z]
        currentBurst[0] = burstTime2[currentBurst[1]]

        arrivalnonzero.clear()
        burstnonzero_index.clear()

    if currentBurst[0] < 1:
      print("Finished")
    elif currentBurst[0] > 0:
      gantt.append(currentBurst[1])
      burstTime2[currentBurst[1]] -= 1
      currentBurst[0] = burstTime2[currentBurst[1]]
      if currentBurst[1] not in firstOccurProcessNum:
        firstOccurProcessNum.append(currentBurst[1])
        firstOccurence[currentBurst[1]] = i
      if burstTime2[currentBurst[1]] == 0:
        completionTime[currentBurst[1]] = i + 1

  def SJF(list, len):  #sjf part for srtf
    for a in range(len):
      if list[a] > 0:
        sjf_index.append(a)

  def SJF_CompareBursttime(
      list, duplicatecount, i,
      indexList):  #gets the burst time of the same arrival time for sjf
    min_number = None
    index = 0  #index of final min_number
    for x in sjf_index:
      if min_number is None:
        min_number = list[x]
        index = x
      elif min_number is not None:
        if list[x] < min_number:
          min_number = list[x]
          index = x
        elif list[x] > min_number:
          min_number = min_number

    y = list.count(min_number)
    sjfburst_index = []
    if y > 1:
      for idx, value in enumerate(list):
        if value == min_number:
          sjfburst_index.append(idx)
      for a in sjfburst_index:
        sjf_arrival.append(arrivalTime[a])
      x = min(sjf_arrival)
      z = sjf_arrival.index(x)
      zz = sjfburst_index[z]
      index = zz
      sjf_arrival.clear()
      sjfburst_index.clear()

    for a in range(burstTime2[index]):
      gantt.append(index)
    completionTime[index] = burstTime2[index] + sjf_current[0]
    if index not in firstOccurProcessNum:
      firstOccurProcessNum.append(index)
      firstOccurence[index] = sjf_current[0]
    sjf_current[0] += burstTime2[index]
    burstTime2[index] = burstTime2[index] - burstTime2[index]

  def TurnaroundTime():  #computation of turnaround time
    for a in range(len(burstTime)):
      x = (completionTime[a] - arrivalTime[a])
      turnaroundTime.append(x)

  def ATT():  #printing and computation of average turnaround time
    print("Average Turnaround Time:  ", "{:.2f}".format(
      (sum(turnaroundTime)) / len(turnaroundTime)) + " ms")

  def WaitingTime():  #computation of waiting time
    for a in range(len(burstTime)):
      x = (turnaroundTime[a] - burstTime[a])
      waitingTime.append(x)

  def AWT():  #printing and computation of average waiting time
    print("Average Waiting Time:  ", "{:.2f}".format(
      (sum(waitingTime)) / len(waitingTime)) + " ms")

  def ResponseTime():  #computation of response time
    for a in range(len(arrivalTime)):
      x = (firstOccurence[a] - arrivalTime[a])
      if x < 0:
        responseTime.append(0)
      else:
        responseTime.append(x)

  #main srtf computation
  def Main(i, maxArrival):  #i is the current time
    i = min(arrivalTime)
    while i <= maxArrival:
      if i in arrivalTime2:
        Duplicates(i)
        i += 1

      elif i not in arrivalTime2:
        for idx, value in enumerate(arrivalTime2):
          if value < (i):
            if burstTime2[idx] > 0:
              not_index.append(idx)
        CompareBursttime(burstTime2, len(not_index), i, not_index)
        not_index.clear()
        i += 1
      sjf_current[0] = i

    for a in range(len(burstTime2)):
      j = burstTime2.count(0)
      k = len(burstTime2)
      l = k - j
      if j != k:
        SJF(burstTime2, k)
        SJF_CompareBursttime(burstTime2, l, sjf_current[0], sjf_index)
        i += 1
      sjf_index.clear()

  def Table():  #printing of srtf table
    print("\n")
    headers = [
      "Processes", "Arrival Time", "Burst Time", "Completion Time",
      "Turnaround Time", "Response Time", "Waiting Time"
    ]
    table = zip(processes, arrivalTime, burstTime, completionTime,
                turnaroundTime, responseTime, waitingTime)
    print(tabulate(table, headers=headers, tablefmt="grid"))

  def GanttChart():  #srtf gantt chart
    print("\nGantt Chart:")
    gantt_count = []
    process = []
    table = "+"
    table2 = "|"
    x = min(arrivalTime)
    table = table + (str("-") * int(x))
    table2 = table2 + (str(" ") * int(x))
    table = table + "+"
    table2 = table2 + "|"
    for a in range(len(gantt)):
      if len(gantt_count) == 0:
        gantt_count.append(1)
        process.append("P" + str(gantt[a] + 1))
        table = table + "-"
        table2 = table2 + " "
      elif gantt[a] != gantt[a - 1]:
        gantt_count.append(1)
        process.append("P" + str(gantt[a] + 1))
        table = table + "+-"
        table2 = table2 + "| "
      elif gantt[a] == gantt[a - 1]:
        gantt_count[len(gantt_count) - 1] += 1
        table = table + "-"
        table2 = table2 + " "
    print("\n")
    print(str(" ") * int(x), end="")
    for a, value in enumerate(process):
      b = int(((gantt_count[a]) - 1) / 2)
      if b <= 0:
        b = int(0)
      print(str(" " * (b + 1)) + str(value) + str(" " * b), end='')
    print("\n")
    print(table + "+")
    print(str(table2) + "|")
    print(table + "+")

    print("0" + (str(" ") * int(x)), end="")
    print(min(arrivalTime), end='')
    for a in range(len(gantt_count)):
      c = gantt_count[a] - 1
      if gantt_count[a] == 1:
        c = 1
      if a == 0:
        nums = min(arrivalTime) + gantt_count[a]
      else:
        nums += gantt_count[a]
        z = len(str(nums))
        if z == 1:
          c = gantt_count[a]
        elif z == 2:
          c = gantt_count[a] - 1
      print(str(" " * c) + str(nums), end='')

    print("\n")

  #Calling functions to print on the terminal
  BurstTime(ProcessCount())
  ArrivalTime(len(burstTime))
  d = int(max(arrivalTime))
  Main(current_time, d)
  TurnaroundTime()
  WaitingTime()
  ResponseTime()
  Table()
  GanttChart()
  AWT()
  ATT()


#MAIN MENU
def mainmenu():
  while True:
    try:
      print("===== Scheduling Algorithm Calculator =====" +
            "\n\n1 First Come First Served (FCFS)" +
            "\n2 Shortes Job First (SJF)" +
            "\n3 Shortest Remaining Time First (SRTF)")
      selected = int(input("\nEnter the number: "))

      if selected == 1:
        print("\n===== First Come First Served =====\n")
        fcfs()
        print("\nCalculation Successful!\n\n")
        return cont()

      elif selected == 2:
        print("\n===== Shortest Job First =====\n")
        sjf()
        print("\nCalculation Successful!\n\n")
        return cont()

      elif selected == 3:
        print("\n===== Shortest Remaining Time First =====\n")
        srtf()
        print("\nCalculation Successful!\n\n")
        return cont()

      else:
        print('Invalid input. Please select from choices 1-3.\n')
        return mainmenu()
    except ValueError:
      print('Invalid input. Please select from choices 1-3.\n')
      return mainmenu()


#RETRY FUNCTION
def cont():
  while True:
    try:
      retry = int(
        input("Would you like to try again? " + "\n1. Yes, try again." +
              "\n2. No, exit.\n"))
      if retry == 1:
        os.system("clear")
        return mainmenu()
      elif retry == 2:
        exit()
      else:
        print('Invalid input. Select from 1 or 2 only.\n')
        return cont()
    except ValueError:
      print('Invalid input. Select from 1 or 2 only.\n')
      return cont()


#for execution
mainmenu()
cont()
