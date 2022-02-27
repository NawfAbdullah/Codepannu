const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');


const app = express();
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(express.static("public"));

mongoose.connect('mongodb://localhost:27017/thefruitsAPI')

nutritionSchema = new mongoose.Schema({
    "carbohydrates": Number,
    "protein": Number,
    "fat": Number,
    "calories": Number,
    "sugar": Number
})

fruitsSchema = new mongoose.Schema({
    "genus": String,
    "name": String,
    "id": {type:Number},
    "family": String,
    "order": String,
    "nutritions":nutritionSchema,
    "category":String
})

const Fruit = mongoose.model("Fruit",fruitsSchema);

app.get('/',(req,res)=>{
        Fruit.find(function(err,fruits){
        if (err) {
            console.log(err);
        } else {
            res.send(fruits);
            }
        })
    })

app.get('/genus/:genus',(req,res)=>{
    const requestedGenus = req.params.genus;
    Fruit.find({'genus':requestedGenus.charAt(0).toUpperCase() + requestedGenus.slice(1)},(err,fruitGene)=>{
        if(err){
            console.log(err)
        }else{
            res.send(fruitGene)
        }
    })
})


app.get('/family/:family',(req,res)=>{
    const requestedfamily = req.params.family;
    Fruit.find({'family':requestedfamily.charAt(0).toUpperCase() + requestedfamily.slice(1)},(err,fruitGene)=>{
        if(err){
            console.log(err)
        }else{
            res.send(fruitGene)
        }
    })
})

app.get('/name/:name',(req,res)=>{
    const requestedname = req.params.name;
    Fruit.find({'name':requestedname.charAt(0).toUpperCase() + requestedname.slice(1)},(err,fruitGene)=>{
        if(err){
            console.log(err)
        }else{
            res.send(fruitGene)
        }
    })
})


app.get('/order/:order',(req,res)=>{
    const requestedorder = req.params.order;
    Fruit.find({'order':requestedorder.charAt(0).toUpperCase() + requestedorder.slice(1)},(err,fruitGene)=>{
        if(err){
            console.log(err)
        }else{
            res.send(fruitGene)
        }
    })
});

app.get('/category/:category',(req,res)=>{
    const requestedcategory = req.params.category;
    Fruit.find({'category':requestedcategory.charAt(0).toUpperCase() + requestedcategory.slice(1)},(err,fruitGene)=>{
        if(err){
            console.log(err)
        }else{
            res.send(fruitGene)
        }
    })
});

app.get('/object/:id',(req,res)=>{
    Fruit.findById(req.params.id,(err,fruit)=>{
        if(err){
            res.send(err)
        }else{
            console.log(fruit)
            res.send(fruit)
        }
    })
});

app.post('/new',(req,res)=>{
    const apiKey = req.query.apiKey;
    if(apiKey == 'codepannustudent'){
            b = req.body
            fruit = new Fruit({
               "genus": b.genus,
                "name": b.name,
                "id": b.id,
                "family": b.family,
                "order": b.order,
                "nutritions":{
                    "carbohydrates": b.carbohydrates,
                    "protein": b.protein,
                    "fat": b.fat,
                    "calories": b.calories,
                    "sugar": b.sugar
            },
                "category":b.category
            })
            Fruit.exists({'name':b.name}, function (err, doc) {
            if (err){
                console.log(err)
            }else{
                if(doc){
                    res.send({'message':'already exists','result':{_id:doc._id}})
                }else{
                    fruit.save()
                    res.send({data:'success fully added','result':{_id:fruit._id}})
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
        Fruit.deleteOne({ _id: req.params.id },(err,result)=>{
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

app.listen(3000, function() {
  console.log("Server started on port 3000");
});