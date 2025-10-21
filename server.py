import http.server
import socketserver
import urllib.parse
import json
import subprocess

import csv
from io import StringIO

def dict2csv(d: dict):
    output = StringIO()
    csv_writer = csv.DictWriter(output, fieldnames=d.keys())
    csv_writer.writeheader()
    csv_writer.writerow(d)
    csv_string = output.getvalue()
    output.close()
    return csv_string

PORT = 8000

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path).path
        match parsed_path:
            case "/styles.css":
                self.send_response(200)
                self.send_header("Content-type", "text/css")
                self.end_headers()
                with open("./styles.css", "r") as file:
                    response = file.read()
                self.wfile.write(response.encode('utf-8'))

            case "/prediction.css":
                self.send_response(200)
                self.send_header("Content-type", "text/css")
                self.end_headers()
                with open("./prediction.css", "r") as file:
                    response = file.read()
                self.wfile.write(response.encode('utf-8'))

            case "/devolution.css":
                self.send_response(200)
                self.send_header("Content-type", "text/css")
                self.end_headers()
                with open("./devolution.css", "r") as file:
                    response = file.read()
                self.wfile.write(response.encode('utf-8'))

            case "/img/formula%201%20logo.svg":
                self.send_response(200)
                self.send_header("Content-type", "image/svg+xml")
                self.end_headers()
                with open("./img/formula 1 logo.svg", "r") as file:
                    response = file.read()
                self.wfile.write(response.encode('utf-8'))

            case "/prediction.html":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                with open("./prediction.html", "r") as file:
                    response = file.read()
                self.wfile.write(response.encode('utf-8'))

            case "/index.html" | "" | "/":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                with open("./index.html", "r") as file:
                    response = file.read()
                self.wfile.write(response.encode('utf-8'))

            case "/img/Imagen%20ferrari.png":
                self.send_response(200)
                self.send_header("Content-type", "image/png")
                self.end_headers()
                with open("./img/Imagen ferrari.png", "rb") as file:
                    response = file.read()
                self.wfile.write(response)

            case "/img/Imagen%20Alpine.png":
                self.send_response(200)
                self.send_header("Content-type", "image/png")
                self.end_headers()
                with open("./img/Imagen Alpine.png", "rb") as file:
                    response = file.read()
                self.wfile.write(response)

            case "/img/neumaticos.png":
                self.send_response(200)
                self.send_header("Content-type", "image/png")
                self.end_headers()
                with open("./img/neumaticos.png", "rb") as file:
                    response = file.read()
                self.wfile.write(response)

            case "/img/carrera.jpg":
                self.send_response(200)
                self.send_header("Content-type", "image/jpg")
                self.end_headers()
                with open("./img/carrera.jpg", "rb") as file:
                    response = file.read()
                self.wfile.write(response)

            case _:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                response = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Arial', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            overflow: hidden;
        }
        
        .container {
            text-align: center;
            color: white;
        }
        
        h1 {
            font-size: 4rem;
            margin-bottom: 1rem;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        }
        
        p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }
        
        #gameCanvas {
            border: 4px solid white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            background: #87CEEB;
            display: block;
            margin: 0 auto;
        }
        
        .controls {
            margin-top: 1rem;
            font-size: 0.9rem;
            color: rgba(255,255,255,0.9);
        }
        
        .score {
            margin-top: 1rem;
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        button {
            background: white;
            border: none;
            padding: 12px 24px;
            font-size: 1rem;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 1rem;
            transition: transform 0.2s;
        }
        
        button:hover {
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>404</h1>
        <p>Oops! The page got lost. Help find it!</p>
        <canvas id="gameCanvas" width="800" height="400"></canvas>
        <div class="controls">Use Arrow Keys or WASD to move and jump. Collect the missing pages!</div>
        <div class="score">Pages Found: <span id="scoreDisplay">0</span></div>
        <button onclick="location.href='/'">Go Back Home</button>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const scoreDisplay = document.getElementById('scoreDisplay');
        
        const player = {
            x: 50,
            y: 300,
            w: 30,
            h: 30,
            vx: 0,
            vy: 0,
            speed: 5,
            jumpPower: 12,
            grounded: false,
            color: '#FF6B6B'
        };
        
        const gravity = 0.5;
        const friction = 0.8;
        
        let platforms = [
            { x: 0, y: 370, w: 800, h: 30 },
            { x: 200, y: 280, w: 150, h: 20 },
            { x: 450, y: 220, w: 150, h: 20 },
            { x: 100, y: 180, w: 120, h: 20 },
            { x: 600, y: 150, w: 150, h: 20 }
        ];
        
        let pages = [];
        let score = 0;
        
        const keys = {};
        
        function spawnPage() {
            const plat = platforms[Math.floor(Math.random() * (platforms.length - 1)) + 1];
            pages.push({
                x: plat.x + plat.w / 2 - 10,
                y: plat.y - 30,
                w: 20,
                h: 25,
                collected: false
            });
        }
        
        for (let i = 0; i < 5; i++) {
            spawnPage();
        }
        
        document.addEventListener('keydown', (e) => {
            keys[e.key.toLowerCase()] = true;
            if ((e.key === 'ArrowUp' || e.key === 'w') && player.grounded) {
                player.vy = -player.jumpPower;
                player.grounded = false;
            }
        });
        
        document.addEventListener('keyup', (e) => {
            keys[e.key.toLowerCase()] = false;
        });
        
        function update() {
            // Movement
            if (keys['arrowleft'] || keys['a']) {
                player.vx = -player.speed;
            } else if (keys['arrowright'] || keys['d']) {
                player.vx = player.speed;
            } else {
                player.vx *= friction;
            }
            
            // Gravity
            player.vy += gravity;
            
            // Apply velocity
            player.x += player.vx;
            player.y += player.vy;
            
            // Boundary check
            if (player.x < 0) player.x = 0;
            if (player.x + player.w > canvas.width) player.x = canvas.width - player.w;
            
            // Platform collision
            player.grounded = false;
            for (let p of platforms) {
                if (player.x < p.x + p.w &&
                    player.x + player.w > p.x &&
                    player.y + player.h > p.y &&
                    player.y + player.h < p.y + p.h &&
                    player.vy > 0) {
                    player.y = p.y - player.h;
                    player.vy = 0;
                    player.grounded = true;
                }
            }
            
            // Collect pages
            for (let page of pages) {
                if (!page.collected &&
                    player.x < page.x + page.w &&
                    player.x + player.w > page.x &&
                    player.y < page.y + page.h &&
                    player.y + player.h > page.y) {
                    page.collected = true;
                    score++;
                    scoreDisplay.textContent = score;
                    spawnPage();
                }
            }
        }
        
        function draw() {
            // Sky
            ctx.fillStyle = '#87CEEB';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Clouds
            ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
            ctx.beginPath();
            ctx.arc(100, 50, 30, 0, Math.PI * 2);
            ctx.arc(130, 50, 40, 0, Math.PI * 2);
            ctx.arc(160, 50, 30, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.beginPath();
            ctx.arc(500, 80, 35, 0, Math.PI * 2);
            ctx.arc(535, 80, 45, 0, Math.PI * 2);
            ctx.arc(570, 80, 30, 0, Math.PI * 2);
            ctx.fill();
            
            // Platforms
            ctx.fillStyle = '#4ECDC4';
            ctx.strokeStyle = '#2C3E50';
            ctx.lineWidth = 2;
            for (let p of platforms) {
                ctx.fillRect(p.x, p.y, p.w, p.h);
                ctx.strokeRect(p.x, p.y, p.w, p.h);
            }
            
            // Pages
            for (let page of pages) {
                if (!page.collected) {
                    // Page shadow
                    ctx.fillStyle = 'rgba(0,0,0,0.2)';
                    ctx.fillRect(page.x + 2, page.y + 2, page.w, page.h);
                    
                    // Page
                    ctx.fillStyle = 'white';
                    ctx.fillRect(page.x, page.y, page.w, page.h);
                    ctx.strokeStyle = '#333';
                    ctx.lineWidth = 1;
                    ctx.strokeRect(page.x, page.y, page.w, page.h);
                    
                    // 404 text on page
                    ctx.fillStyle = '#667eea';
                    ctx.font = 'bold 10px Arial';
                    ctx.fillText('404', page.x + 2, page.y + 14);
                }
            }
            
            // Player shadow
            ctx.fillStyle = 'rgba(0,0,0,0.3)';
            ctx.fillRect(player.x + 3, player.y + 3, player.w, player.h);
            
            // Player
            ctx.fillStyle = player.color;
            ctx.fillRect(player.x, player.y, player.w, player.h);
            
            // Player face
            ctx.fillStyle = 'white';
            ctx.fillRect(player.x + 8, player.y + 8, 5, 5);
            ctx.fillRect(player.x + 17, player.y + 8, 5, 5);
            ctx.fillStyle = '#333';
            ctx.fillRect(player.x + 10, player.y + 20, 10, 3);
        }
        
        function gameLoop() {
            update();
            draw();
            requestAnimationFrame(gameLoop);
        }
        
        gameLoop();
    </script>
</body>
</html>
                """

                self.wfile.write(response.encode())


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Get the size of the data
        post_data = self.rfile.read(content_length)  # Read the data
        parsed_data = urllib.parse.parse_qs(post_data.decode('utf-8'))  # Parse the data
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        command = ["Rscript", "internal.R", json.dumps(parsed_data)]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            
            output = result.stdout
            error = result.stderr
            
            with open("./devolution.html", "r") as file:
                response = file.read()
            response = response.replace("%RESULT%", output)
            # f"""
            # <html><body><h1>POST request received!</h1>
            # <pre>{parsed_data}</pre>
            # <div style='white-space: pre-wrap;'> Rscript:\n {output}</div>
            # </body></html>"""

            if error:
                print("Error:")
                print(error)

        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
        
        # Respond with the received data
        self.wfile.write(response.encode('utf-8'))

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with ReusableTCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
