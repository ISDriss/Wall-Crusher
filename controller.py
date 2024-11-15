import serial
import serial.tools
import serial.tools.list_ports
#unused test/example code

# ser = serial.Serial("COM6", 115200, timeout=1)
# ser.write(b"Hello from python\n")

def read_controller(serial):
    answer = serial.readline()
    return answer.decode()

#list available ports
def list_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(port.device)
