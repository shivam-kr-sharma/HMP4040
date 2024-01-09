import pyvisa



# This is the code to find out the required device from the list of devices attached to this pc.
rm = pyvisa.ResourceManager()
resources = rm.list_resources()
for resource in resources:
    try:
        device = rm.open_resource(resource)
        y = device.query("*IDN?")
        y = y.lower() # to convert it in the lower case. 

        
           # Replace the string in if condition with the appropriate device name which you want to find out and use.
        
        if 'hmp4040' in y: # in the previous line of code, you converted device identity (or y) to lower case because you want to write the string in if condition in lower case.
            print("hello")     
            hmp4040 = device
            print("I am ", hmp4040, "and my identity is ", y )
    except:
        pass