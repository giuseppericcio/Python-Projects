import cv2
# initalize the cam
cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if bbox is not None:
        # display the image with lines
        bb_pts = bbox.astype(int).reshape(-1, 2)
        num_bb_pts = len(bb_pts)
        for i in range(num_bb_pts):
            # draw all lines
            cv2.line(img, tuple(bb_pts[i]), tuple(bb_pts[(i+1) % len(bbox)]), color=(255, 0, 0), thickness=2)
        if data:
            print("[+] QR Code detected, data:", data)
    # display the result
    cv2.imshow("img", img)    
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()