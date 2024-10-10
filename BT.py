import bluetooth

target_name = "nano"
target_address = None
print("Performing BLE inquiry...")
nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                            flush_cache=True, lookup_class=False)

for addr, name in nearby_devices:
    print(addr, name)
    print(bluetooth.lookup_name(addr))
    if target_name == bluetooth.lookup_name(addr):
        target_address = addr
        break

if target_address is not None:
    print ("found target bluetooth device with address ", target_address)
else:
    print ("could not find target bluetooth device nearby")