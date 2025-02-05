import express from 'express';
import { connectToDB } from "./services/database.service";
import { router } from "./routes/productRoutes";
import cors from 'cors';
//  const corsOptions = {
    //  origin: 'http://localhost:3000', 
    //  methods: ['GET', 'POST', 'PUT', 'DELETE'], 
    //  allowedHeaders: ['Content-Type', 'Authorization'], 
    //  credentials: true, 
//  };
//app.use(cors(corsOptions));

const app = express();
app.use(cors());
const port = 5000;

connectToDB()
    .then(() => {
        app.use("/", router);
        app.listen(port, () => {
            console.log(`Server started at http://localhost:${port}`);
        });
    })
    .catch((error: Error) => {
        console.error("Database connection failed", error);
        process.exit();
    });
// npm run build
// npm start
