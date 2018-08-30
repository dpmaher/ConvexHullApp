var canvas, ch, ctx, X, Y;
X = 0;
Y = 0;
var xpts = [];
var ypts = [];
var wid = 2.5;
var hullMade = false;

function initialize_canvas() {
    canvas = document.getElementById("myCanvas");
    ctx = canvas.getContext("2d");
    ch = document.getElementById("form_hull");
     
    canvas.addEventListener("click", function (e) {
        findxy("down", e);
    }, false);

    ch.addEventListener("click", function (e) {
        convexHull(e);
    }, false);
}

function findxy(res, e) {
    if (res == "down") {
        var X = e.clientX - canvas.offsetLeft;
        var Y = e.clientY - canvas.offsetTop;
        
        if (hullMade == true)
        {
            clearCanvas();
            hullMade = false;
        }

        ctx.beginPath();
        ctx.arc(X,Y,wid,0,2 * Math.PI, false);
        ctx.fillStyle = "blue";
        ctx.fill();
        ctx.closePath();

        xpts.push(X);
        ypts.push(Y);
    }
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    xpts = [];
    ypts = [];
}

function convexHull() {
    var xhttp = new XMLHttpRequest();
    var url = '';
    var ptdata = JSON.stringify({ X : xpts, Y : ypts });

    xhttp.open("POST", url, true);
    xhttp.setRequestHeader('Content-type', 'application/json');

    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var hull = JSON.parse(this.responseText);
            var chX = hull["X"];
            var chY = hull["Y"];
            var len = chX.length;

            for (var i = 1; i < len; i++) {
                ctx.beginPath();
                ctx.moveTo(chX[i-1], chY[i-1]);
                ctx.lineTo(chX[i], chY[i]);
                ctx.strokeStyle = "red";
                ctx.lineWidth = 3;
                ctx.stroke();
            }
            if (len > 2) {
                ctx.beginPath();
                ctx.moveTo(chX[len-1], chY[len-1]);
                ctx.lineTo(chX[0], chY[0]);
                ctx.stroke();
            }
            hullMade = true;
        }
    };
    xhttp.send(ptdata);
}

