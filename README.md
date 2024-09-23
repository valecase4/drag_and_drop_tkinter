# Drag And Drop in Tkinter

The application is initialized showing a red widget.
User can drag it and move it within the window.

## Logic

Dragging starts with the click of the mouse. When the user clicks the mouse on the widget, the application calculates the coordinates (relative to the widget).

See logic.pdf to better understand.

On dragging (when the user drags the mouse), the application has to calculates the new coordinates for the widget. Each dragging movement consists of calculating new coordinates. The current position (x, y) is calculated using winfo_x() and winfo_y() methods.
Then the value of displacement is given by: the new position of the cursor minus the start position (which is fixed since the user clicks on the widget).

Download demo.mp4 file to see how the application works.