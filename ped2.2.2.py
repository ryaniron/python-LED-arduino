import os
import serial
import csv
from statistics import mean, pstdev
from keyboard import is_pressed
import time

def main():
    #ask for port and attempt to connect
    com_port = input("Enter the COM port: ")
    if not com_port.startswith("COM"):
        com_port = "COM" + com_port
    try:
        ser = serial.Serial(com_port, 9600)
    except:
        print("Error: Could not connect to device")
    while True:
        #check if the device is connected
        try:
            ser.readline()
            ser_connected = True
        except:
            print("Error: Could not connect to device")
            ser_connected = False
            com_port = input("Enter the COM port: ")
            if not com_port.startswith("COM"):
                com_port = "COM" + com_port
                try:
                    ser = serial.Serial(com_port, 9600)
                except:
                    print("Could not connect to device")

        if ser_connected:
            print_menu()
            user_choice = input("Enter an option: ")
            try:
                user_choice = int(user_choice)
            except:
                user_choice = 10
            if(user_choice == 1):
                begin_test(ser)
            elif(user_choice == 2):
                open_file()
            elif(user_choice == 3):
                read_values(ser)
            elif(user_choice == 4):
                com_port = input("Enter the COM port: ")
                if not com_port.startswith("COM"):
                    com_port = "COM" + com_port
            elif(user_choice == 5):
                break
            else:
                print("Invalid Option")

def begin_test(ser):
    #create the file to store the test
    test_name = input("Create a name for for the test: ")
    file_name = test_name + ".csv"
    
    #create a directory
    try:
        os.mkdir(test_name+ "_dir")
        os.mkdir(test_name + '_dir/backups_dir')
    except FileExistsError:
        print("Name already in use")
        return
    except:
        print("Something went wrong")
        return

    #find the batch size
    batch_size = input("Enter the Batch Size: ")
    while True:
        try:
            batch_size = int(batch_size)
            break
        except:
            print("Invalid input")
            batch_size = input("Enter the Batch Size: ")

    #find the number of times to take the sample
    data_points = input("Enter the number of measurements: ")
    while True:
        try:
            data_points = int(data_points)
            break
        except:
            print("Invalid input")
            data_points = input("Enter the number of measurements: ")

    all_ref_data = []
    #collect each ref_data in the batch
    for i in range(batch_size):
        #create temporary file to store data
        ref_data = []
        with open(test_name +"_dir/backups_dir/ref_temp_sample_"+str(i+1)+"_"+test_name + ".csv", 'w', newline='') as temp_csvfile:
            temp_writer = csv.writer(temp_csvfile)
            temp_writer.writerow(["Reference Measurements"])
            #collect ref data
            print("Beginning Collection of Reference data for sample " + str(i+1))
            input("Press ENTER to continue...")
            for j in range(data_points):
                print("Reference measurement " + str(j+1) + "/" + str(data_points))
                #wait for enter
                input("Insert Reference, press ENTER when ready")
                #collect data and prompt user
                while True:
                    try:
                        clear_serial_buffer(ser)
                        data = ser.readline().decode().strip()
                        print(data)
                        #ask to use this data
                        use_data = input("Use this value (y/n): ")
                        if use_data == 'y':
                            ref_data.append(data)
                            temp_writer.writerow([data])
                            break
                    #device disconnection errors during test
                    except:
                        print("Something went wrong, check device")
                        com_port = input("Enter the COM port: ")
                        if not com_port.startswith("COM"):
                            com_port = "COM" + com_port
                        try:
                            ser = serial.Serial(com_port, 9600)
                        except:
                            print("Error: Could not connect to device")
            print("Completed Reference Data for Sample " + str(i+1))
            print("##########")
            all_ref_data.append(ref_data)
        print()
        print("Collection of reference data complete")

    all_sample_data = []
    for i in range (batch_size):
        #collect sample data
            sample_data = []
            with open(test_name + "_dir/backups_dir/temp_sample_"+str(i+1)+"_"+ test_name + ".csv", 'w', newline='') as temp_csvfile:
                temp_writer = csv.writer(temp_csvfile)
                print("Beginning collection of Sample data for Sample " + str(i+1))
                input("Press ENTER to continue...")
                temp_writer.writerow(["Sample Measurements"])
                for j in range(data_points):
                    print("Sample measurement " + str(j+1) + "/" + str(data_points))
                    #wait for enter
                    input("Insert sample, press ENTER when ready")
                    while True:
                        try:
                            clear_serial_buffer(ser)
                            data = ser.readline().decode().strip()
                            print(data)
                            #ask to use this data
                            use_data = input("Use this value (y/n): ")
                            if use_data == 'y':
                                sample_data.append(data)
                                temp_writer.writerow([data])
                                break
                        #device disconnection errors during test
                        except:
                            print("Something went wrong, check device")
                            com_port = input("Enter the COM port: ")
                            if not com_port.startswith("COM"):
                                com_port = "COM" + com_port
                            try:
                                ser = serial.Serial(com_port, 9600)
                            except:
                                print("Error: Could not connect to device")
                all_sample_data.append(sample_data)
            print("Completed Reference Data for Sample " + str(i+1))
            print("##########")

    print("Collection of Sample data complete")
    print("Generating File...")
    with open(test_name + "_dir/" + file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        #calculate extinction data
        sample_counter = 1
        for ref_data, sample_data in zip(all_ref_data, all_sample_data):
            extinctions = []
            for ref, sample in zip(ref_data, sample_data):
                try:
                    extinctions.append(1-(float(sample) / float(ref) ) )
                except:
                    extinctions.append(-999)
            #average of extinctions
            extinctions_avg = mean(extinctions)
            #standard deviation of extinctions
            extinctions_std = pstdev(extinctions)

            
            #sample
            writer.writerow([("Sample " + str(sample_counter))])
            #create header
            header = ["Ref Measurements", "Sample Measurements", "Extinctions", "Average", "Standard Deviation"]
            writer.writerow(header)

            #write the first row of data
            first_row = [str(ref_data.pop(0)), str(sample_data.pop(0)), str(extinctions.pop(0)), extinctions_avg, extinctions_std]
            writer.writerow(first_row)

            #write the rest of the data
            for ref, data, extinction in zip(ref_data, sample_data, extinctions):
                row = [ref, data, extinction]
                writer.writerow(row)
            sample_counter += 1
    print("File Generation Complete")

def open_file():
    name = input("Enter file name (do not include extenstion): ")
    filename = name + "_dir\\" + name + ".csv"
    print("Opening " + filename)
    #only works on windows for now
    try:
        os.startfile(filename)
    except:
        print("Error: Could not open the file.")

def read_values(ser):
    clear_serial_buffer(ser)
    #display values from the arduino real time until q is pressed
    print("Hold 'q' to quit")
    while not is_pressed("q"):
        data = ser.readline().decode().strip()
        print(data)
    #(I did it this way out of laziness)

def print_menu():
    print()
    print("##### MENU #####")
    print("(1) Begin New Test")
    print("(2) Open File")
    print("(3) Read Values")
    print("(4) Change Serial Port")
    print("(5) Exit")


def clear_serial_buffer(ser):
    #had to implement this way for strange compatibility issues
    start_time = time.time()
    while (time.time() - start_time) < 0.5:
        ser.readline()

main()