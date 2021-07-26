// Data
let data = {
    screen: {
        width: 640,
        height: 480,
        halfWidth: null,
        halfHeight: null
    },
    render: {
        delay: 30
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
            rotation: 5.0
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
const screen = document.createElement('canvas');
screen.width = data.screen.width;
screen.height = data.screen.height;
screen.style.border = "1px solid black";
document.body.appendChild(screen);

// Canvas context
const screenContext = screen.getContext("2d");

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

        // Pythagoras Theorem: a² + b² = c²
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

function clearScreen() {
    screenContext.clearRect(0, 0, data.screen.width, data.screen.height);
}

// Start
main();

function main() {
    setInterval(function() {
        clearScreen();
        rayCasting();
    }, data.render.delay);
}
