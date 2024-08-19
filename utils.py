import cv2

ALLOWED_EXTENSIONS = {"png", "webp", "jpg", "jpeg", "gif"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def processImage(filename, operation):
    img = cv2.imread(f"uploads/{filename}")
    if operation == "cgray":
        imgOut = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        newFileName = f"static/{filename}"
        cv2.imwrite(newFileName, imgOut)
        return filename
    if operation == "cpng":
        newFileName = f"static/{filename.split('.')[0]}.png"
        cv2.imwrite(newFileName, img)
        return newFileName
    if operation == "cwebp":
        newFileName = f"static/{filename.split('.')[0]}.webp"
        cv2.imwrite(newFileName, img)
        return newFileName
    if operation == "cjpg":
        newFileName = f"static/{filename.split('.')[0]}.jpg"
        cv2.imwrite(newFileName, img)
        return newFileName
