import os
import paramiko


def upload(host, port, username, password):
    msg = '成功'
    transport = paramiko.Transport(host, port)
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    localfile = os.getcwd() + '/' + 'get_data.py'
    filepath = '/home/'
    filename = 'get_data.py'
    sftp.put(localfile, filepath + filename)
    print(msg)


def send_data(host, port, username, password):
    transport = paramiko.Transport(host, port)
    transport.connect(username=username, password=password)
    client = paramiko.SSHClient()
    client._transport = transport
    filepath = '/home/'
    filename = 'get_data.py'
    datacmd = 'python' + filepath + filename
    stdin, stdout, stderr = client.exec_command(datacmd)
    client.close()
    return stdout, stderr



