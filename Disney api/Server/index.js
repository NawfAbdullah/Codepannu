const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

app = express();

app.use(express.static("public"));
app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));


mongoose.connect('mongodb://localhost:27017/thedisneyAPI')

characterSchema = new mongoose.Schema({
  'name':String,
  'designedby':String,
  'img':String,
  'firstAppeared':String,
  'gender':String
})

const Character = mongoose.model("Character",characterSchema);



app.get('/',(req,res)=>{
  Character.find(function(err,character){
        if (err) {
            console.log(err);
        } else {
            res.send(character);
            }
        })
    })

app.post('/',(req,res)=>{
  const apiKey = req.query.apiKey;
    if(apiKey == 'codepannustudent'){
            b = req.body
            character = new Character({
              'name':b.name.toLowerCase(),
              'designedby':b.designedby.toLowerCase(),
              'img':b.img,
              'firstAppeared': b.firstAppeared.toLowerCase(),
              'gender':b.gender.toLowerCase()
            })
  
            Character.exists({'name':b.name.toLowerCase()}, function (err, doc) {
            if (err){
                console.log(err)
            }else{
                if(doc){
                    res.send({'message':'already exists','result':{_id:doc._id}})
                }else{
                    character.save()
                    res.send({data:'success fully added','result':{_id:character._id}})
                    }
                }
            });
       
    }else{
        res.send({response:'invalid api key'})
    }
    })

app.delete('/:id',(req,res)=>{
    apiKey = req.query.apiKey
    if(apiKey == 'codepannustudent'){
        Character.deleteOne({ _id: req.params.id },(err,result)=>{
            if(err){
                console.log(err)
                res.send(err)
              
            }else{
                 console.log(result)
                res.send({message:'Sucessfully Deleted'})
            }
        })
        
    }else{
        res.send({message:'Invalid Api key'})
    }
})

app.get('/name/:name',(req,res)=>{
    const requestedname = req.params.name;
    Character.find({'name':requestedname.toLowerCase()},(err,fruitGene)=>{
        if(err){
            console.log(err)
        }else{
            res.send(fruitGene)
        }
    })
})

app.get('/gender/:gender',(req,res)=>{
    const requestedgender = req.params.gender;
    Character.find({'gender':requestedgender.toLowerCase()},(err,gender)=>{
        if(err){
            console.log(err)
        }else{
            res.send(gender)
        }
    })
})


app.listen(3000,()=>{
  console.log('server started at port 3000')
})