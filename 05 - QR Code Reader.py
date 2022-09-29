import cv2
# read the QRCODE image
img = cv2.imread("site.png")

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    bb_pts = bbox.astype(int).reshape(-1, 2)
    num_bb_pts = len(bb_pts)
    for i in range(num_bb_pts):
        # draw all lines
        point1 = tuple(bb_pts[i])
        point2 = tuple(bb_pts[(i+1) % num_bb_pts])
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

# display the result
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()