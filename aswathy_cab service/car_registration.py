class car:
    def __init__(self):
        self.driver=[]
    def driver_info(self,name, cab_number, mobile_no, Available, x1, x2):
        Driver={"name":name, "cab_number":cab_number,"mobile_no":mobile_no, "Available":Available, "x1":x1, "x2":x2}
        self.driver.append(Driver)
        return Driver
    def historyofdrivers(self):
        return self.driver