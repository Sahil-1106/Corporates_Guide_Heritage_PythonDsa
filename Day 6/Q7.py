# Traffic Light System using match-case with Guard Condition

color = input("Enter traffic light color (red/yellow/green): ").lower()
speed = int(input("Enter current speed: "))

match color:
    case "red":
        print("Stop")
    
    case "yellow":
        print("Get Ready / Slow Down")
    
    case "green" if speed > 60:
        print("Slow down even on green")
    
    case "green":
        print("Go")
    
    case _:
        print("Invalid traffic light color")