import express from 'express';
import cors from 'cors';
import { execFile } from 'child_process';
const app = express();

app.use(cors({
  origin: "*",
}));

app.get('/water/:ph/:hard/:sol/:chlor/:sul/:cond/:org/:tri/:tur', (req, res) => {
    // return res.send(users[req.params.userId]);
    // return res.send("Hello" + req.params.userId);
    let ret;
    execFile('python3', ['main.py', ""+req.params.ph, ""+req.params.hard, ""+req.params.sol, ""+req.params.chlor, ""+req.params.sul, ""+req.params.cond, ""+req.params.org, ""+req.params.tri, ""+req.params.tur], 
        (error, stdout, stderr) => {
        if (error) {
          throw error;
          }
        ret =  res.send(stdout);
    });
    return ret;
});

app.listen(6969, () =>
  console.log(`Listening on port ${6969}!`),
);
