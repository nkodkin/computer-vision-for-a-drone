import cv2
import math
import matplotlib.pyplot as plt


def get_coordinates(image_path):
    image = cv2.imread(image_path)
    original_image = image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 200)
    contours, hierarchy = cv2.findContours(
        edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=False)
    item = sorted_contours[0]
    M = cv2.moments(item)
    x, y, w, h = cv2.boundingRect(item)

    xcoordinate1 = x
    xcoordinate2 = x + w
    xcoordinate_center = int(M['m10']/M['m00'])

    ycoordinate1 = y
    ycoordinate2 = y + h
    ycoordinate_center = int(M['m01']/M['m00'])

    return (xcoordinate1, ycoordinate1, xcoordinate2, ycoordinate2, xcoordinate_center, ycoordinate_center)


def overlay_images(image_1, image_2):
    img1 = cv2.imread(image_1)
    img2 = cv2.imread(image_2)
    dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0.0)
    return dst


def direction_of_movement(image_1, image_2):
    img1_x1, img1_y1, img1_x2, img1_y2, img1_center_x, img1_center_y = get_coordinates(
        image_1)
    img2_x1, img2_y1, img2_x2, img2_y2, img2_center_x, img2_center_y = get_coordinates(
        image_2)
    d_y = (img2_y1 - img1_y1)
    d_x = (img2_x1 - img1_x1)

    if d_y <= 0 and d_x > 0:
        alpha = abs(math.atan(d_y / d_x))
        degrees_alpha = math.degrees(alpha)
    elif d_y > 0 and d_x > 0:
        alpha = abs(math.atan(d_y / d_x))
        degrees_alpha = math.degrees(alpha)
        degrees_alpha = 90 + degrees_alpha
        alpha = math.pi - alpha
    elif d_y > 0 and d_x < 0:
        alpha = abs(math.atan(d_y / d_x))
        degrees_alpha = math.degrees(alpha)
        degrees_alpha = 180 + degrees_alpha
        alpha = math.pi + alpha
    elif d_y <= 0 and d_x < 0:
        alpha = abs(math.atan(d_y / d_x))
        degrees_alpha = math.degrees(alpha)
        degrees_alpha = 270 + degrees_alpha
        alpha = math.pi*2 + alpha
    else:
        alpha = 0
        degrees_alpha = 0

    print(f'radians_alpha: {alpha}\ndegrees_alpha: {degrees_alpha}')
    return (alpha, degrees_alpha, img1_center_x, img1_center_y, img2_center_x, img2_center_y)


def show_images(image_1, image_2):
    alpha, degrees_alpha, img1_center_x, img1_center_y, img2_center_x, img2_center_y = direction_of_movement(
        image_1, image_2)
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.subplots_adjust(top=0.78)
    fig.suptitle('Moving an object', fontsize=14, fontweight='bold')
    ax.set_title(f'radians_alpha: {alpha}\ndegrees_alpha: {degrees_alpha}')
    ax.set_xlabel('x_axis')
    ax.set_ylabel('y_axis')
    plt.arrow(img1_center_x,
              img1_center_y,
              img2_center_x-img1_center_x,
              img2_center_y-img1_center_y,
              width=0.1,
              shape='full',
              length_includes_head=True,
              head_width=4,
              head_length=4)
    img = overlay_images(image_1, image_2)
    plt.imshow(img)
    fig.savefig("test_img/image.png")


if __name__ == '__main__':
    show_images("test_img/image1.png", "test_img/image2.png")
