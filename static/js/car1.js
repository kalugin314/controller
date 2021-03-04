socket = io.connect('localhost:9090');
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
canvas.width = 700;
canvas.height = 700;
var rX = 0;
var rY = 0;
ctx.fillStyle = "green";
ctx.fillRect(0, 0, 100, 100);
document.addEventListener('keypress', (event) => {
  const keyName = event.keyCode;
  console.log(keyName);
  if (keyName == 100) {
    if (rX < 600) {
        ctx.clearRect(rX, rY, 100, 100);
        rX += 10;
        cngpos(rX, rY)
    }
  }
  if (keyName == 97) {
    if (rX > 0) {
        ctx.clearRect(rX, rY, 100, 100);
        rX -= 10;
        cngpos(rX, rY)
    }
  }
  if (keyName == 119) {
    if (rY > 0) {
        ctx.clearRect(rX, rY, 100, 100);
        rY -= 10;
        cngpos(rX, rY)
    }
  }
  if (keyName == 115) {
    if (rY < 600) {
        ctx.clearRect(rX, rY, 100, 100);
        rY += 10;
        cngpos(rX, rY)
    }
  }
});
function cngpos(pX, pY) {
    ctx.fillStyle = "green";
    ctx.fillRect(pX, pY, 100, 100);
}
function sleep(ms) {
        var unixtime_ms = new Date().getTime();
        while(new Date().getTime() < unixtime_ms + ms) {}
    }
socket.on('message', function(msg) {
    console.log("0");
    socket.send("0");
    sleep(1000);
});
socket.send("0");
