// Data
let data = {
    screen: {
        width: 640,
        height: 480,
        halfWidth: null,
        halfHeight: null
    },
    minimap: {
        width: 480,
        height: 480,
        unit: 48
    },
    rayCasting: {
        incrementAngle: null,
        precision: 64
    },
    player: {
        fov: 60,
        halfFov: null,
        x: 2,
        y: 2,
        angle: 90,
        speed: {
            movement: 0.5,
            rotation: 8.0
        }
    },
    key: {
        up: "KeyW",
        down: "KeyS",
        left: "KeyA",
        right: "KeyD"
    },
    map: [
        [1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,1,1,0,1,0,0,1],
        [1,0,0,1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1,0,0,1],
        [1,0,0,1,0,1,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1],
    ]
}

// Calculated data
data.screen.halfWidth = data.screen.width / 2;
data.screen.halfHeight = data.screen.height / 2;
data.rayCasting.incrementAngle = data.player.fov / data.screen.width;
data.player.halfFov = data.player.fov / 2;

// Canvas
const screen = document.getElementById("screen");
const screenContext = screen.getContext("2d");
// Minimap
const minimap = document.getElementById("minimap");
const minimapContext = minimap.getContext("2d");

document.addEventListener('keydown', (event) => {
    let keyCode = event.code;

    if (keyCode === data.key.up) {
        let playerCos = Math.cos(degreeToRadians(data.player.angle)) * data.player.speed.movement;
        let playerSin = Math.sin(degreeToRadians(data.player.angle)) * data.player.speed.movement;
        let newX = data.player.x + playerCos;
        let newY = data.player.y + playerSin;

        // Collision test
        if (data.map[Math.floor(newY)][Math.floor(newX)] == 0) {
            data.player.x = newX;
            data.player.y = newY;
        }
    } else if (keyCode === data.key.down) {
        let playerCos = Math.cos(degreeToRadians(data.player.angle)) * data.player.speed.movement;
        let playerSin = Math.sin(degreeToRadians(data.player.angle)) * data.player.speed.movement;
        let newX = data.player.x - playerCos;
        let newY = data.player.y - playerSin;

        // Collision test
        if (data.map[Math.floor(newY)][Math.floor(newX)] == 0) {
            data.player.x = newX;
            data.player.y = newY;
        }
    } else if (keyCode === data.key.left) {
        data.player.angle -= data.player.speed.rotation;
    } else if (keyCode === data.key.right) {
        data.player.angle += data.player.speed.rotation;
    }
    drawMinimap();
});

function rayCasting() {
    let rayAngle = data.player.angle - data.player.halfFov;

    for (let rayCount = 0; rayCount < data.screen.width; rayCount++) {

        // Ray data
        let ray = {
            x: data.player.x,
            y: data.player.y
        }

        // Ray path incrementers
        let rayCos = Math.cos(degreeToRadians(rayAngle)) / data.rayCasting.precision;
        let raySin = Math.sin(degreeToRadians(rayAngle)) / data.rayCasting.precision;

        // Wall checking
        let wall = 0;
        while (wall == 0) {
            ray.x += rayCos;
            ray.y += raySin;
            wall = data.map[Math.floor(ray.y)][Math.floor(ray.x)];
        }

        // Draw ray
        minimapContext.beginPath();
        minimapContext.moveTo(
            data.player.x * data.minimap.unit,
            data.player.y * data.minimap.unit
        );
        minimapContext.lineTo(ray.x * data.minimap.unit, ray.y * data.minimap.unit);
        minimapContext.strokeStyle = "orange";
        minimapContext.stroke();

        // Pythagoras Theorem:  c² = a² + b²
        // Formula: distance² = (player x - ray x)² + (player y - ray y)²
        let distance = Math.sqrt(
            Math.pow(data.player.x - ray.x, 2) +
            Math.pow(data.player.y - ray.y, 2)
        );

        // Fish eye fix
        // Formula: adjacent side = hypotenuse * COS(ray angle - player angle)
        distance = distance * Math.cos(degreeToRadians(rayAngle - data.player.angle));

        // Wall height
        let wallHeight = Math.floor(data.screen.halfHeight / distance);

        // Calc wall color by distance
        rgb_color = 255 / (1 + distance * distance * 0.2)

        // Draw sky
        drawLine(rayCount, 0, rayCount, data.screen.halfHeight - wallHeight, "cyan");
        // Draw wall
        // drawLine(rayCount, data.screen.halfHeight - wallHeight, rayCount, data.screen.halfHeight + wallHeight, "red");
        drawLine(rayCount, data.screen.halfHeight - wallHeight, rayCount, data.screen.halfHeight + wallHeight, `rgb(${rgb_color},${rgb_color},${rgb_color})`);
        // Draw floor
        drawLine(rayCount, data.screen.halfHeight + wallHeight, rayCount, data.screen.height, "green");

        // Increment
        rayAngle += data.rayCasting.incrementAngle;
    }
}

function drawMinimap() {
    // Clear minimap
    minimapContext.clearRect(0, 0, data.minimap.width, data.minimap.height);

    // Floor
    minimapContext.beginPath();
    minimapContext.rect(0, 0, data.minimap.width, data.minimap.height);
    minimapContext.fillStyle  = "green";
    minimapContext.fill();

    // Map
    for (let y = 0; y < data.map.length; y++) {
        for (let x = 0; x < data.map[y].length; x++) {
            if (data.map[y][x] == 1) {
                minimapContext.beginPath();
                minimapContext.rect(
                    x * data.minimap.unit,
                    y * data.minimap.unit,
                    x + data.minimap.unit,
                    y + data.minimap.unit
                );
                minimapContext.fillStyle  = "cyan";
                minimapContext.fill();
            }
        }
    }

    // Player
    minimapContext.beginPath();
    minimapContext.arc(
        data.player.x * data.minimap.unit,
        data.player.y * data.minimap.unit,
        10,
        0,
        2 * Math.PI,
        false
    );
    minimapContext.fillStyle  = "red";
    minimapContext.fill();

    // Player direction
    minimapContext.beginPath();
    minimapContext.moveTo(
        data.player.x * data.minimap.unit,
        data.player.y * data.minimap.unit
    );
    minimapContext.lineTo(
        (data.player.x * data.minimap.unit) + 30 * Math.cos(degreeToRadians(data.player.angle)),
        (data.player.y * data.minimap.unit) + 30 * Math.sin(degreeToRadians(data.player.angle))
    );
    minimapContext.strokeStyle = "yellow";
    minimapContext.stroke();
}

function clearScreen() {
    screenContext.clearRect(0, 0, data.screen.width, data.screen.height);
}

// Main function
function draw() {
    clearScreen();
    rayCasting();
    requestAnimationFrame(draw);
}

// Start
drawMinimap();
draw();
