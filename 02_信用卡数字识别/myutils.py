import cv2

def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0

    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    # 用一个最小的矩形，把找到的形状包起来x,y,h,w
    boundingBoxes = [cv2.boundingRect(c) for c in cnts] 
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))

    return cnts, boundingBoxes


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    '''
        cv2.resize函数修改图像尺寸时，需要输入修改的尺寸（高和宽都需要）
        自定义resize函数，可以只接受宽（或高）一个参数，而另外一个会按比例放大或缩小 
    '''
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    # 如果只设置了高（或宽），就按同比例缩小
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized