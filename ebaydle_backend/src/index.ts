import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';

const app = express();
app.use(cors());
app.use(express.json());

mongoose.connect('mongodb://localhost:27017/ebaydle', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
} as mongoose.ConnectOptions)
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error(err));
  

// app.use('/api/items', itemRoutes); //new


app.listen(5000, () => console.log('Server running on port 5000'));
