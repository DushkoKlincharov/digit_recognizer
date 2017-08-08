let express = require('express')
let bodyParser = require('body-parser')
let pythonShell = require('python-shell')
let app = express()

app.use(express.static('static'))
app.use(bodyParser.json())

app.set('views', './templates');
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('index', {result: 'undefined'})
})

let options = {
    mode: 'text',
    args: ['image.png'],
    pythonPath: './env/bin/python',
};

app.post('/', (req, res) => {
    req.body.image = req.body.image.replace(/^data:image\/png+;base64,/, "");
    req.body.image = req.body.image.replace(/ /g, '+');
    require("fs").writeFile("image.png", req.body.image, 'base64', function (err) {
        pythonShell.run('./tf/convert.py', options, function (err, results) {
            pythonShell.run('./tf/recognize.py', options, function (err, results) {
                //console.log(results)
                res.send(results[0]);
            });
        });
    });

})

app.listen(3000, (err) => {
    console.log('Server is running on port 3000 ...')
})
