import subprocess
import json


class Container(object):
    name = None
    Status = None
    Running = None
    Paused = None
    Restarting = None
    OOMKilled = None
    Dead = None
    Pid = None
    ExitCode = None
    Error = None
    StartedAt = None
    FinishedAt = None

    def __init__(self, name):
        self.Name = name
        self._update()

    def _update(self):
        for attr, val in inspect(self.Name).iteritems():
            setattr(self, attr, val)

    def stop(self):
        process = stop(self.Name)
        process.wait()
        self._update()

    def start(self):
        process = start(self.Name)
        process.wait()
        self._update()


def inspect(name):
    params = ['docker', 'inspect', '-f="{{json .State}}"', name]
    process = subprocess.Popen(
        params,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    output = process.stdout.read()
    process.terminate()
    return json.loads(output)


def run(name, volumes=None, ports=None, **kwargs):
    params = ['docker', 'run', '-d']
    if volumes is not None and type(volumes) is list:
        params += map(lambda a: ['-v'] + a, volumes)
    if ports is not None and type(ports) is list:
        params += map(lambda a: ['-p'] + a, ports)
    if kwargs is not None and type(kwargs) is dict:
        for k,v in kwargs.iteritems():
            params += ["-"+k, v]
    params += [name]
    print params
    return subprocess.Popen(
        params,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


def start(name):
    params = ['docker', 'start', name]
    return subprocess.Popen(
        params,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


def stop(name, force=False):
    params = ['docker', 'stop']
    if force:
        params += ['-f']
    params += [name]
    return subprocess.Popen(
        params,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


def new_mysql_box():
    process = run('mysql', e='MYSQL_ROOT_PASSWORD=admin')
    name = process.stdout.read().strip()
    process.terminate()
    return name


def stop_mysql_box(name):
    return stop(name)


def get_mysql_boxes():
    params = ['docker', 'ps', '-a', '-q', '-f=[IMAGE=mysql]']
    process = subprocess.Popen(
        params,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    boxes = process.stdout.read().strip().split("\n")

    return [Container(box) for box in boxes]


def version():
    params = ['docker', 'version']
    process = subprocess.Popen(
        params,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out = process.stdout.read()
    process.terminate()
    return out
