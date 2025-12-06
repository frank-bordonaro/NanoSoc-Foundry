import subprocess, time, os

procs = []

def start_component(cmd, cwd=None):
    p = subprocess.Popen(cmd, shell=True, cwd=cwd)
    procs.append(p)
    print('Started:', cmd)

if __name__ == '__main__':
    start_component('python normalizer/app.py')
    time.sleep(1)
    start_component('python deception/deception_service.py')
    time.sleep(1)
    print('All started. Run simulator separately.')
