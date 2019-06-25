#     return res

def encode(encoding_matrix,packets):
    return np.matmul(encoding_matrix,packets)


if __name__ == "__main__":

    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65438        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            packets_to_send =  [200,300,400,500,600]
            num_of_packets = len(packets_to_send)
            num_of_encoded_packets = len(packets_to_send)
            num_of_encoded_packets_str = str(num_of_encoded_packets)
            while(len(num_of_encoded_packets_str) < 32):
                num_of_encoded_packets_str += " "
            num_of_encoded_packets_str = str.encode(num_of_encoded_packets_str)
            conn.send(num_of_encoded_packets_str)
            encoding_matrix =[]

            for i  in range(num_of_encoded_packets):
                encoding_vector = []
                for j in range(num_of_packets):
                    encoding_vector.append(randint(0,256))
                encoding_matrix.append(encoding_vector)
            encoded_packets = np.matmul(encoding_matrix, packets_to_send)
            print(encoding_matrix)
            print(encoded_packets)
            for i in range(len(encoding_matrix)):
                print("this is the i: " + str(i))
                to_be_sent = ""
                for j in range(len(encoding_matrix[i])):
                    to_be_sent += str(encoding_matrix[i][j]) +  ","
                to_be_sent = to_be_sent[:-1]
                to_be_sent += " " + str(encoded_packets[i])
                to_be_sent = str.encode(to_be_sent)
                length_of_transfer = str(len(to_be_sent))
                while(len(length_of_transfer) < 32):
                    length_of_transfer+=" "

                conn.send(str.encode(length_of_transfer))
                conn.send(to_be_sent)


