# Edge_Detection
Edge and Contour Detection with Roberts Cross + BFS
![Orange](https://github.com/user-attachments/assets/311bc980-b8fa-4ee9-b482-ebd4a76a658d)![contours](https://github.com/user-attachments/assets/7ed0144b-c9e8-4139-886b-29b8a58e792a)![edges](https://github.com/user-attachments/assets/19973368-c143-4d0f-9fa4-7b68a2c33d10)

1.Load a grayscale image.

2.Detect edges using the Roberts Cross operator.

3.Group connected edge pixels into contours via a breadth-first search (BFS).

roberts_cross(image)
Implements the Roberts Cross edge detector. For each pixel, it computes gradients along the two diagonal directions and combines them into a single value (0–255).

detect_contours(edge_image, threshold=10)
Scans the edge map, grouping neighboring pixels above the threshold into distinct contours. Returns a list of contours, where each contour is a list of pixel coordinates.
