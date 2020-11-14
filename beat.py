import os
from pydub import AudioSegment


def Fibonacci(n):
  if n < 0:
    print("Incorrect input")
  # First Fibonacci number is 0
  elif n == 0:
    return 0
  # Second Fibonacci number is 1
  elif n == 1:
    return 1
  else:
    return Fibonacci(n-1)+Fibonacci(n-2)


def niceSequence2(a,order):
  out = []
  
  for j in range(len(order)):
    inp = order[j]
    if order[j] == '1':
      inp = '4'
    elif order[j] == '2':
      inp = '3'
    elif order[j] == '3':
      inp = '2'
    elif order[j] == '4':
      inp = '1'
    order[j] = inp


  for i in range(4, len(a), 4):
    out.append(i-int(order[0]))
    out.append(i-int(order[1]))
    out.append(i-int(order[2]))
    out.append(i-int(order[3]))
    print(order)

  out.append(len(a)-1)

  print("the out looks like")
  print(out)
  return out


def niceSequence(a):
  out = [0]*len(a)
  j = 0
  for i in range(len(a)):
    p = Fibonacci(j)
    if p > len(a):
      out[i] = 0
    else:
      out[i] = p
      j += 1
  print("the out looks like")
  print(out)

  return out


def createDirectory(strDir):
  Dir = strDir
  if not os.path.exists(strDir):
    print(strDir + " path didn't exist, creating now")
    os.mkdir(strDir)
  return Dir


def ordercheck(str):
  if len(str) != 4:
    return False
  for i in range(len(str)):
    if int(str[i]) > 4 or int(str[i]) < 1:
      return False
  return True


def ordertolist(str):
  out = []
  if ordercheck(str):
    for i in range(len(str)):
      out.append(str[i])
  return out


def swapthisshit(file, outputfile, chunkLenght, order="1111", chunksize=1):
  if chunkLenght < 100 or chunksize > 1 or chunksize < 0.1:
    return print("dumbass")  # skip errors lol

  orderlist = ordertolist(order)
  
  temp_dir = createDirectory("temp")  # create the temporary directory
  read = AudioSegment.from_file(file, format="mp3")  # open the file
  dummy = AudioSegment.empty()  # create an empty audio thingy

  # for every <chunkLength> create a new file
  for i, chunk in enumerate(read[::chunkLenght]):
    with open(os.path.join(temp_dir, "read-%s.wav") % i, "wb") as f:
      chunk = chunk[0:chunkLenght*chunksize]
      chunk.export(f, format="wav")
      print("created dummy number" + str(i))

  # how many files have been created?
  filecount = len(os.listdir(temp_dir))

  # custom order of playing
  setofnums = []
  for i in range(filecount):
    setofnums.append(i)
  print(setofnums)

  setofnums = niceSequence2(setofnums,orderlist)  # SEQUENCE HERE       ###

  for i in range(0, len(setofnums)):

    if len(dummy) > len(dummy):  # max time
      break

    j = int(setofnums[i])
    dummy += AudioSegment.from_file(os.path.join(temp_dir,"read-%s.wav") % j, format="wav")

    # sys.stdout.write("\033[F")
    # sys.stdout.write("\033[K")
    print(str(j)+" segmented out of " + str(len(setofnums)))

  # remove all dummy files
  for i in range(0, filecount):
    #print("removing dummy number" + str(i))
    os.remove(os.path.join(temp_dir, "read-%s.wav") % i)

  print("exporting...")
  dummy.export(outputfile, format="mp3")
  print("Done!")


def main():

  try:
    swapthisshit("mega.mp3", "test1.mp3", 2000)
    # swapthisshit("giorno.mp3","test2.mp3",2500)
  except Exception:
    print("you absolute fucking dumbass")

  # playsound("test1.mp3")


if __name__ == '__main__':
  main()
