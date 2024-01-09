#           Below is the code for controlling the powersupply of Rhode and Schwarz HMP4040 using python commands. For more information related to the commands you can refer to the link below for the user manual.
#           https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/pdm/cl_manuals/user_manual/1178_6833_01/HMPSeries_UserManual_en_03.pdf




import pyvisa







class RSHMP4040():

    def __init__(self, address): # address = address of the device (like ASRL3::INSTR)
        """
            Initialize the power supply with the specified address

            Arguments: 
            
            Address is the name of the device as it appars in the resources list.

            For example, 'ASRL1::INSTR', 'TCPIP0::A-34461A-0000-2.local::hislip0::INSTR', 'TCPIP0::A-34461A-0000-2.local::inst0::INSTR',
             
            'USB0::0x1AB1::0x0642::DG1ZA204104808::0::INSTR', etc.
        
        """
        self.address = address
        # Add any additional initialization code here
        self.rm = pyvisa.ResourceManager()
        self.ps = self.rm.open_resource(address)



    def close(self):
        """
        This function does not take any arguments, and it closes the resource, meaning, it cuts the communication between device and the pc.
        
        """
        self.rm.close()
        print(f"Disconnected from {self.address}")



    def set_volt_and_curr(self, channel, voltage, current):    # Give the input of the state as 'ON' or 'OFF'

        """
        This function sets the voltage and current of a specific channel to a desired value.

        Arguments: 

            channel: give the channel number here as integer.
            voltage: give the voltage value as float. Or, you can also give the input 'MAX' or 'MIN', which will set the voltage to the maximum/minimum which this powersupply can afford.
            current: give the the current value as float. Or, you can also give the input 'MAX' or 'MIN', which will set the current to the maximum/minimum which this powersupply can afford.
        
        """
        self.ps.write(f'INST OUT{channel}')
        self.ps.write(f'VOLT {voltage}')
        self.ps.write(f'CURR {current}')
        self.ps.write(f'INST:NSEL {channel}')
        volt = self.ps.query("VOLT?")
        curr = self.ps.query("CURR?")
        print(f"Voltage of channel {channel} set to {volt}V and current set to {curr} A")



    def get_volt_and_curr(self, channel):
        """
            This function is used to get the value of the channel whichis already set on the device.

            Arguments:
                        Channel: enter the channel number as integer of which you want to know the values of the voltage and current.
        
        """
        self.ps.write(f'INST:NSEL {channel}')
        voltage = self.ps.query("VOLT?")  
        current = self.ps.query("CURR?")
        print(f"Voltage of channel {channel} is {voltage}V and the current is {current} A ")
        return voltage, current


   
    def set_output_state(self, channel, state):   # Give the input of the state as 'ON' or 'OFF'

        """
            This function is used to change the output state of a specific channel.

            Arguments:
                        channel: Enter the channel number as integer for which you want to change the state.
                        state: Enter the input as 'ON' or 'OFF' whichever you want.
            
        """
        self.ps.write(f'INST OUT{channel}')   # selects the channel
        self.ps.write(f'OUTP {state}')       # turning the output on or off
        print(f"Output of channel {channel} set to {state}")



    def change_volt_in_steps(self, channel, steps, change):  # Give the input of change as 'UP' or 'DOWN'
        """
            This special function is used to change the value of the voltage in steps of your choice.

            Arguments:
                        channel: enter the channel number as integer for which you want to change the value of the voltage.
                        steps: enter the voltage steps as integer or float whichever you want.
                        change: change here refers to whether you want to increase or decrease the voltage.
                        For increasing, enter the string 'UP', and for decreasing, enter the string 'DOWN'

        """

        self.ps.write(f'INST OUT{channel}')  # selects the channel
        self.ps.write(f'VOLT:STEP {steps}')   # defining the steps
        self.ps.write(f'VOLT {change}')       # selecting you wnat to increase or decrease
        print(f"Output of channel {channel} {change} by {steps} volts")




# powersupply = RSHMP4040('ASRL3::INSTR')
# powersupply.set_volt_and_curr(1,3,1)
# powersupply.set_output_state(1,'OFF')
# powersupply.get_volt_and_curr(3)
# powersupply.change_volt_in_steps(3,2, 'UP')
# powersupply.close()






