const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(express.static("public"));

mongoose.connect('mongodb://localhost:27017/quotes')

quotesSchema = new mongoose.Schema({
    'quote':String,
    'category':String,
    'author':String
})

const Quote = mongoose.model("Quote",quotesSchema);
app.get('/',(req,res)=>{
	Quote.find(function(err,quotes){
        if (err) {
            console.log(err);
        } else {
            res.send(quotes);
            }
        })
})

app.post('/',(req,res)=>{
	const apiKey = req.query.apiKey;
    if(apiKey == 'codepannustudent'){
            b = req.body
            quote = new Quote({
               	'quote':b.quote,
    			'author':b.author,
                "category":b.category
            })
            Quote.exists({'quote':b.quote}, function (err, doc) {
            if (err){
                console.log(err)
            }else{
                if(doc){
                    res.send({'message':'already exists','result':{_id:doc._id}})
                }else{
                    quote.save()
                    res.send({data:'success fully added','result':{_id:quote._id}})
                    }
                }
            });
       
    }else{
        res.send({response:'invalid api key'})
    }
    })

app.get('/category/:category',(req,res)=>{
    const requestedcategory = req.params.category;
    Quote.find({'category':requestedcategory.charAt(0).toUpperCase() + requestedcategory.slice(1)},(err,quote)=>{
        if(err){
            console.log(err)
        }else{
            res.send(quote)
        }
    })
});

app.get('/random',(req,res)=>{

	Quote.find(function(err,quotes){
        if (err) {
            console.log(err);
        } else {
            random_id = Math.floor((Math.random()*quotes.length))+1;
            console.log(random_id)
            res.send({'data':quotes[random_id]})
            }
        })
})

app.get('/author/:author',(req,res)=>{
    const requestedauthor = req.params.author;
    Quote.find({'author':requestedauthor.charAt(0).toUpperCase() + requestedauthor.slice(1)},(err,quote)=>{
        if(err){
            console.log(err)
        }else{
            res.send(quote)
        }
    })
});

app.get('/author-one/:author',(req,res)=>{
    const requestedauthor = req.params.author;
    Quote.find({'author':requestedauthor.charAt(0).toUpperCase() + requestedauthor.slice(1)},(err,quote)=>{
        if(err){
            console.log(err)
        }else{
        	random_id = Math.floor((Math.random()*quote.length));
            console.log(random_id)
            res.send({'data':quote[random_id]})
        }
    })
});

app.get('/category-one/:category',(req,res)=>{
    const requestedcategory = req.params.category;
    Quote.find({'category':requestedcategory.charAt(0).toUpperCase() + requestedcategory.slice(1)},(err,quote)=>{
        if(err){
            console.log(err)
        }else{
        	random_id = Math.floor((Math.random()*quote.length));
            console.log(random_id)
            res.send({'data':quote[random_id]})
        }
    })
});


app.delete('/:id',(req,res)=>{
    apiKey = req.query.apiKey
    if(apiKey == 'codepannustudent'){
        Quote.deleteOne({ _id: req.params.id },(err,result)=>{
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