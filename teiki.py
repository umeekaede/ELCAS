import time
import subprocess
i=0
while True:
    print(i)
    print("Hello")
    subprocess.call(['rsync', '-avzP', 'iumezaki:~/ume.cc', '.'])
    #subprocess.run('rsync -avzP oumezaki:~/ume.cc .', shell=True)
    print()
    time.sleep(1)
    i+=1
