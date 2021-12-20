from car_registration import car
from rider_registration import Rider
from welcome import Greet
from distance_between import distance
from tripconclusion import desired_loc
if __name__=="__main__":
    cabdriver=car()
    cabrider=Rider()
    DriverCount=int(input("Nuber of Drivers: "))
    for k in range(DriverCount):
        name=input("enter your Name: ")
        cab_number=input("Enter your Cab_NUMBER: ")
        mobile_no=int(input("Enter your PH_NUMBER: "))
        Available=input("Press<yes> if you are available else <no>: ")
        x1= int(input("Enter your X location: "))
        x2= int(input("Enter your Y locaion: "))
        Driver=cabdriver.driver_info(name,cab_number,mobile_no,Available,x1,x2)
        print("Driver details:", Driver)
    print("Enter Rider Details")
    name=str(input("Type Your NAME: "))
    mobile_no=int(input("enter your number: "))
    AVAILABLE=input("TYPE <yes> to book a ride:")
    y1=int(input("Type your x Co_ordinates: "))
    y2=int(input("Type your y Co_ordinates: "))
    rider=cabrider.rider_info(name,mobile_no,AVAILABLE,y1,y2)
    print("rider Details", rider)
    alldrivers=cabdriver.historyofdrivers()
    allriders=cabrider.historyofrides()
    entry = input("Provide your Input here: ")
    if entry == "check":
        print(" THANK you for Booking with us , Please enter your the location you want to go:")
        d1=int(input("enter x co_ordinates: "))
        d2=int(input("enter y co_ordinates: "))
        value=999999999
        cab_registered=None
        for i in range(len(alldrivers)):
            s=distance(alldrivers[i]["x1"], alldrivers[i]["x2"],allriders[0]["y1"],allriders[0]["y2"])
            print("This driver ", alldrivers[i]["name"], "is", s, "KM from you")
            if s<value:
                value=s
                cab_registered=alldrivers[i]
        print("as the driver is close so", cab_registered, "will reach your location")

        for j in range(len(allriders)):
            v= desired_loc(allriders[0]["y1"], allriders[0]["y2"], d1, d2)
            print("your destination has arrived")
            amount = 2
            print("Pay the Amount of Rs. ", v*amount*(s/10))

    while True:
        print("History of your Rides type<HISTORY>: ")
        print("To quit type <EXIT>: ")
        entry = input("enter Your Input here: ")
        if entry=="HISTORY":
            print(alldrivers,allriders)

        if entry == "EXIT":
            print("Thank You, visit Again!")
            break
