let canvas = document.getElementById("myCanvas");
let ctx = canvas.getContext("2d");

function getImage() {
    return canvas.toDataURL('image/png');
}

$("#btnRecognize").click(function () {
    $("#result").html("Processing....");
    $.ajax({
        type: 'POST',
        url: '/',
        data: JSON.stringify({
            image: getImage()
        }),
        contentType: "application/json",
        dataType: 'json',
        success: function(data) {
            // console.log(data)
            $("#result").html(data.max_value);
            $("#probArray").html(JSON.stringify(data.prob_array).replace(new RegExp('"', 'g'),""))    
        }
    });
    
});

$("#btnClear").click(function () {
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0,0,canvas.clientWidth,canvas.clientHeight);
    $("#result").html("")
    $("#probArray").html("")
});

(function () {
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0,0,canvas.clientWidth,canvas.clientHeight);
    var mouse = {
        x: 0,
        y: 0
    };
    var last_mouse = {
        x: 0,
        y: 0
    };

    /* Mouse Capturing Work */
    canvas.addEventListener('mousemove', function (e) {
        last_mouse.x = mouse.x;
        last_mouse.y = mouse.y;

        mouse.x = e.pageX - this.offsetLeft;
        mouse.y = e.pageY - this.offsetTop;
    }, false);


    /* Drawing on Paint App */
    ctx.lineWidth = 30;
    ctx.lineJoin = 'round';
    ctx.lineCap = 'round';
    ctx.strokeStyle = 'black';

    canvas.addEventListener('mousedown', function (e) {
        canvas.addEventListener('mousemove', onPaint, false);
    }, false);

    canvas.addEventListener('mouseup', function () {
        canvas.removeEventListener('mousemove', onPaint, false);
    }, false);

    var onPaint = function () {
        ctx.beginPath();
        ctx.moveTo(last_mouse.x, last_mouse.y);
        ctx.lineTo(mouse.x, mouse.y);
        ctx.closePath();
        ctx.stroke();
    };

}());
