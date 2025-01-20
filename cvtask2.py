import cv2

def load_and_preprocess(image_path):
    
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return cv2.GaussianBlur(image, (5, 5), 0)

def detect_changes(before_path, after_path, threshold=30):
    
    before = load_and_preprocess(before_path)
    after = load_and_preprocess(after_path)
    dif = cv2.absdiff(before, after)
    _, change_mask = cv2.threshold(dif, threshold, 255, cv2.THRESH_BINARY)
    return change_mask

def main(before_path, after_path):
    
    change_mask = detect_changes(before_path, after_path)
    print(f"Changes detected: {cv2.countNonZero(change_mask)} pixels")
    cv2.imshow('Changes', change_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


main('coral1.jpg', 'coral2.jpg')
