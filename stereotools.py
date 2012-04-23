import cv


def grayscale(img):
    """ Returns a new grayscale image from a colour one.
    """
    grayscale = cv.CreateImage(cv.GetSize(img), 8, 1)
    cv.CvtColor(img, grayscale, cv.CV_BGR2GRAY)
    return grayscale


def normalise(img):
    """ Returns a normalised copy of a grayscale image
    """
    normalised = cv.CreateImage(cv.GetSize(img), 8, 1)
    cv.EqualizeHist(img, normalised)
    return normalised


def get_vert_edges(img, cuts=20):
    """ Returns a list (len cuts) of lists of distinct vertical edges in
        the image.

        img is a cv image from cv.LoadImage
    """
    edges = []
    end = img.height
    step = end / cuts
    start = step / 2
    for row in range(start, end, step):
        rowedges = []
        lastval = None
        for col in range(img.width):
            val = img[row, col]
            if lastval is not None and abs(val - lastval) > 70:
                rowedges.append(col)
            lastval = val
        if len(rowedges) >= 2:
            edges.append((row, rowedges))
    return edges
