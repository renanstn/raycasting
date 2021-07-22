/**
 * Cast degree to radian
 * @param {Number} degree
 */
 function degreeToRadians(degree) {
    let pi = Math.PI;
    return degree * pi / 180;
}

/**
 * Draw line into screen
 * @param {Number} x1
 * @param {Number} y1
 * @param {Number} x2
 * @param {Number} y2
 * @param {String} cssColor
 */
 function drawLine(x1, y1, x2, y2, cssColor) {
    screenContext.strokeStyle = cssColor;
    screenContext.beginPath();
    screenContext.moveTo(x1, y1);
    screenContext.lineTo(x2, y2);
    screenContext.stroke();
}
