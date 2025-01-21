import express from 'express';
import { connectToDB } from "./services/database.service";
import { router } from "./routes/productRoutes";

const app = express();
const port = 3000;

connectToDB()
    .then(() => {
        app.use("/products", router);

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
