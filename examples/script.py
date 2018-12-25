import subprocess
##proc = subprocess.Popen(['java', 'GetString', 'sljdf'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
##out, err1 = proc.communicate()


##try:
##    completed = subprocess.run(
##        ['java', 'GetString', 'Yoni Cohen'],
##        check=True,
##        shell=True,
##        stdout=subprocess.PIPE,
##    )
##except subprocess.CalledProcessError as err:
##    print('ERROR:', err)
##else:
##    print('returncode:', completed.returncode)
##    print('Have {} bytes in stdout: {!r}'.format(
##        len(completed.stdout),
##        completed.stdout.decode('utf-8'))
##    )

try:
    outputPy = subprocess.check_output(['python', 'exPy.py', 'arg from py'], shell=True)
    outputCpp = subprocess.check_output(['exCpp.exe', 'arg from cpp'], shell=True)
    outputJava = subprocess.check_output(['java', 'GetString', 'arg from java'], shell=True)
except Exception as err:
    print('ERROR:', err)
else:
    print(outputPy.decode('utf-8'))
    print(outputCpp.decode('utf-8'))
    print(outputJava.decode('utf-8'))
