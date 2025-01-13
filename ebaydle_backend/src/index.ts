import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';
import productRoutes from './routes/productRoutes';

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());


app.use('/api/products', productRoutes); 

mongoose.connect('mongodb://localhost:27017/ebaydle', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
} as mongoose.ConnectOptions)
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error(err));
  


/*
app.get('/', (req: Request, res: Response) => {
    res.send("spaghetti monster");
});
*/

app.listen(port, () => console.log('Server running on port 5000'));
