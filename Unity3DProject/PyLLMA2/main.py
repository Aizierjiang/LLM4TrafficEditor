import signal
import socket
import threading
import PyLLMA2.llma2 as llma2
import config as config

signal_stop = False
client_socket = socket.socket()
gpt_response = ''

def handler(signum, frame):
    global signal_stop
    signal_stop = True
    client_socket.send(b'bye')
    client_socket.close()
    print("Exited!")

signal.signal(signal.SIGINT, handler)  # Handle Ctrl+C in the main thread

def receiver():
    global gpt_response
    while True:
        data = client_socket.recv(1024).decode()
        if data[:3] == "bye":
            client_socket.close()  # Close the connection
            print("Socket closed!")
            break
        else:
            print('Received from server: ' + data)
            if data.startswith(config.hit_sign):
                new_prompt = f"{config.base_prompt} {config.interactive_prompt} {gpt_response} !"
                gpt_response = llma2.call(new_prompt)  # Call LLMA2 API with the new prompt
                print("New prompt: " + new_prompt)
                print("LLMA2 response: " + gpt_response)
                if gpt_response.startswith('MP:'):
                    client_send(gpt_response)

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
    gpt_response = llma2.call(config.initial_prompt)  # Call LLMA2 with an initial prompt
    client_send(gpt_response)
    while True:
        if signal_stop:
            break