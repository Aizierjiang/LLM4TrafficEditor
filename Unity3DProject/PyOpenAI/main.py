import signal
import socket
import threading
import chatgpt as chatgpt
import config as config

signal_stop = False


def handler(signum, frame):
    global signal_stop
    signal_stop = True
    client_socket.send(b'bye')
    client_socket.close()
    print("Exited!")


signal.signal(signal.SIGINT, handler)  # get Ctrl+C, only usable in main thread

client_socket = socket.socket()

gpt_response = ''


def receiver():
    global gpt_response
    while True:
        data = client_socket.recv(1024).decode()
        if(data[:3] == "bye"):
            client_socket.close()  # close the connection
            print("Socket closed!")
            break
        else:
            print('Received from server: ' + data)
            if(data[:3] == config.hit_sign):
                new_prompt = config.base_prompt + config.interactive_prompt + gpt_response + ' !'
                gpt_response = chatgpt.call(new_prompt)
                print("new:"+new_prompt)
                print("gpt:"+gpt_response)
                if(gpt_response[:3] == 'MP:'):
                    client_send(gpt_response)


def sender():
    while True:
        if signal_stop:
            break
        message = input('> ')
        if not message:
            continue
        client_socket.send(message.encode())


def client_start():
    global client_socket
    client_socket.connect((config.host, config.port))
    receive_thread = threading.Thread(target=receiver)
    receive_thread.start()
    # send_thread = threading.Thread(target=sender)
    # send_thread.start()


def client_send(message='Empty'):
    if(client_socket is None):
        print("Client is Null!")
    else:
        client_socket.send(message.encode())  # send message
        print('Sent:' + message)


if __name__ == '__main__':
    client_start()
    gpt_response = chatgpt.call()
    client_send(gpt_response)
    while True:
        if signal_stop:
            break
