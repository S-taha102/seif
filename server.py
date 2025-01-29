
from vidgear.gears import VideoGear
from vidgear.gears import NetGear



stream = VideoGear(source=0).start()

server = NetGear(address="", port="5454",  protocol="tcp", pattern=1, logging=True)


while True:

    try:
        
        frame = stream.read()

        
        if frame is None:
            break

        

        
        server.send(frame)

    except KeyboardInterrupt:
        break


stream.stop()
server.close()