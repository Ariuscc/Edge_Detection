import cv2
import math
from collections import deque

def roberts_cross(image):

    height, width = image.shape
    

    edges = image.copy()
    

    for y in range(height - 1):
        for x in range(width - 1):

            gx = int(image[y, x]) - int(image[y+1, x+1])

            gy = int(image[y, x+1]) - int(image[y+1, x])
            

            val = math.sqrt(gx * gx + gy * gy)
            

            if val > 255:
                val = 255
            
            edges[y, x] = int(val)
    

    for x in range(width):
        edges[height - 1, x] = 0
    for y in range(height):
        edges[y, width - 1] = 0
    
    return edges

def detect_contours(edge_image, threshold=10):

    height, width = edge_image.shape
    

    visited = [[False]*width for _ in range(height)]
    

    contours = []
    

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    for y in range(height):
        for x in range(width):

            if edge_image[y, x] > threshold and not visited[y][x]:

                queue = deque()
                queue.append((y, x))
                visited[y][x] = True
                

                contour_points = []
                
                while queue:
                    cy, cx = queue.popleft()
                    contour_points.append((cy, cx))
                    

                    for dy, dx in directions:
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < height and 0 <= nx < width:
                            if (edge_image[ny, nx] > threshold and
                                not visited[ny][nx]):
                                visited[ny][nx] = True
                                queue.append((ny, nx))
                

                contours.append(contour_points)
    
    return contours

def main():

    image = cv2.imread("./Orange.png", 0)
    if image is None:
        print("couldn't load image.")
        return

    edges = roberts_cross(image)

    contours = detect_contours(edges, threshold=10)

    contour_image = edges.copy()
    height, width = contour_image.shape
    contour_image[:, :] = 0
    for contour in contours:
        for (cy, cx) in contour:
            contour_image[cy, cx] = 255

    cv2.imwrite("original.png", image)
    cv2.imwrite("edges.png", edges)
    cv2.imwrite("contours.png", contour_image)

    cv2.imshow("Original image", image)
    cv2.imshow("Edges (Roberts Cross)", edges)
    cv2.imshow("Contours (po BFS)", contour_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
