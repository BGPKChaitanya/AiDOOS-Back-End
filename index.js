const express = require("express");
const cors = require("cors");
const app = express();
app.use(cors());
const fs = require("fs");

const PythonShell = require("python-shell").PythonShell;

let extractData;

PythonShell.run("extract.py", null, function (err) {
  if (err) throw err;
  // console.log("finished");
  fs.readFile("resume_data.txt", "utf8", (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
    extractData = data;
  });
});

app.get("/", (req, res) => {
  res.send(extractData);
});

app.listen(3005, () => {
  console.log("Server Connected");
});
