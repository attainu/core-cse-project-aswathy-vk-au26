class Rider:
    def __init__(self):
        self.info=[]
    def rider_info(self,name,mobile_no,AVAILABLE,y1,y2):
        rider={"name":name,"mobile_no":mobile_no,"AVAILABLE":AVAILABLE,"y1":y1,"y2":y2}
        self.info.append(rider)
        return rider
    def historyofrides(self):
        print("data of rider is uploading:::::::")
        return self.info