from threading import Thread
import cv2, socket, time, numpy as np


host = ''
port = 9000
locaddr = (host, port)

# Send/Receive response
tello_address = ('192.168.10.1', 8889)
# Receive video stream
video_address = ('192.168.10.1', 11111)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(locaddr)


# Capture default camera
cap = cv2.VideoCapture(0)

# Set the upper and lower bounds for object mask
l_b = np.array([95, 50, 20])
u_b = np.array([130, 255, 255])


def recv():
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\nExit . . .\n')
            break


def trackmotion():
    while True:
        # Read frames from default camera
        _, frame1 = cap.read()
        _, frame2 = cap.read()
        _, frame3 = cap.read()

        # Convert frame3 from BGR to HSV for masking
        hsv = cv2.cvtColor(frame3, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, l_b, u_b)
        # Combine mask to frame?
        res2 = cv2.bitwise_and(frame2, frame2, mask=mask)
        res1 = cv2.bitwise_and(frame1, frame1, mask=mask)

        # Find (absolute) difference between first and second frame
        diff = cv2.absdiff(res1, res2)
        # Convert BGR to Grayscale to find contours
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        # Apply blur to reduce noise
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # Find threshold
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        # Fill in blanks?
        dilated = cv2.dilate(thresh, None, iterations=3)

        # Find  contours
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # Draw contours as rectangles onto original frame
        x = 0
        y = 0
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            # Ignore contours with an area lower than this
            if cv2.contourArea(contour) < 500:
                continue
            # Draw the rectangle
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Print some text
            cv2.putText(frame1, "Status: {}, Coordinates: X = {}, Y = {}".format('Movement', x, y), (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # Draw the frame
        cv2.imshow("feed", frame1)
        cv2.imshow('res', res1)

        # Assign value inside frame2, to frame1
        frame1 = frame2
        res1 = res2

        # Refresh frame2
        _, frame2 = cap.read()

        # Center the coordinates by setting the middle point as 0
        x = x - 640
        y = y - 360

        x2 = 0; y2 = 0
        # Pause frame for 16ms. This is 30~ FPS (60 is 16.66... 30 is 33.33...)
        cv2.waitKey(16)

        cmd = "stop".encode('utf-8')

        # If x or y default to -640, -320 (from no movement)
        # Set them to the last known value to repeat the movement
        if x == -640:
            x = x2
        if y == -320:
            y = y2

        # If x or y are within these bounds, do the following move
        if x < -200:
            x2 = x
            cmd = "cw 50".encode('utf-8')
        elif x > 200:
            x2 = x
            cmd = "ccw 50".encode('utf-8')
        elif x < 200 & x > -200:
            cmd = "stop".encode('utf-8')
        if y != -320:
            if y > 250:
                y2 = y
                cmd = "emergency".encode('utf-8')

        sendcmd = sock.sendto(cmd, tello_address)

print('Tello: command takeoff land flip forward back left right \r\n'
      '       up down cw ccw speed speed?\r\n')
print('\nend -- quit demo.\r\n')

# Create threads for talking to the Tello
recvThread = Thread(target=recv)
recvThread.start()

# Initialize into SDK mode
msg = "command"
msg = msg.encode(encoding="utf-8")
sent = sock.sendto(msg, tello_address)

# Infinite Loop (Assume Connected to Tello)
while True:
    try:
        # Initialize into SDK mode
        msg = input("")
        if 'end' in msg:
            print('...')
            sock.close()
            break
        if 'takeoff' in msg:
            # Send data
            msg = msg.encode(encoding="utf-8")
            sent = sock.sendto(msg, tello_address)
            time.sleep(1)
            trackmotion()

    except KeyboardInterrupt:
        print('\n . . .\n')
        sock.close()
        break
