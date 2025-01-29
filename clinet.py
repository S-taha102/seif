
from vidgear.gears import NetGear
import cv2



client = NetGear(address="", port="5454", protocol="tcp",pattern=1,receive_mode=True,logging=True)



while True:

    
    frame = client.recv()

    
    if frame is None:
        break

    
    cv2.imshow(" Frame", frame)

    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("e"):
        break

cv2.destroyAllWindows()
client.close()