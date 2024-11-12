import signal
import socket
import threading
import PyQWen.qwen as qwen
import config as config

signal_stop = False

def handler(signum, frame):
    global signal_stop
    signal_stop = True
    client_socket.send(b'bye')
    client_socket.close()
    print("Exited!")

signal.signal(signal.SIGINT, handler)  # Handle Ctrl+C in the main thread

client_socket = socket.socket()
qwen_response = ''

def receiver():
    global qwen_response
    while True:
        data = client_socket.recv(1024).decode()
        if data[:3] == "bye":
            client_socket.close()  # Close the connection
            print("Socket closed!")
            break
        else:
            print('Received from server: ' + data)
            if data.startswith(config.hit_sign):
                new_prompt = f"{config.base_prompt} {config.interactive_prompt} {qwen_response} !"
                qwen_response = qwen.call(new_prompt)  # Call QWen API
                print("New prompt: " + new_prompt)
                print("QWen response: " + qwen_response)
                if qwen_response.startswith('MP:'):
                    client_send(qwen_response)

def sender():
    while True:
        if signal_stop:
            break
        message = input('> ')
        if message:
            client_socket.send(message.encode())

def client_start():
    global client_socket
    client_socket.connect((config.host, config.port))
    receive_thread = threading.Thread(target=receiver)
    receive_thread.start()
    # Uncomment to enable sending messages
    # send_thread = threading.Thread(target=sender)
    # send_thread.start()

def client_send(message='Empty'):
    if client_socket is None:
        print("Client socket is not initialized!")
    else:
        client_socket.send(message.encode())  # Send message
        print('Sent: ' + message)

if __name__ == '__main__':
    client_start()
    qwen_response = qwen.call(config.initial_prompt)  # Call QWen with an initial prompt
    client_send(qwen_response)
    while True:
        if signal_stop:
            break