import socket
import numpy  as np
import  time


if __name__ == "__main__":

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65438        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        num_packets = s.recv(32)
        num_packets = int(bytes.decode(num_packets))
        decoding_matrix=[]
        encoded_packets=[]
        print(num_packets)
        for i in range(num_packets):
            bytes_to_recv = int(bytes.decode(s.recv(32)))
            encoded_pakcet = bytes.decode(s.recv(bytes_to_recv))
            split_encoded_packet = encoded_pakcet.split(" ")
            # print(split_encoded_packet[0])
            coefficients =  split_encoded_packet[0].split(",")
            decoding_vector = []
            for c in range(len(coefficients)):
                decoding_vector.append(int(coefficients[c]))
            encoded_packets.append(int(split_encoded_packet[1]))
            decoding_matrix.append(decoding_vector)
        print(encoded_packets)
        print(decoding_matrix)
        time.sleep(1)
        x = np.linalg.solve(decoding_matrix,encoded_packets)
        print(x)


